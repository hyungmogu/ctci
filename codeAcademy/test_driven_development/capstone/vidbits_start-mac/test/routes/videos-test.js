const {assert} = require('chai');
const request = require('supertest');
const {jsdom} = require('jsdom');

const app = require('../../app');
const Video = require('../../models/video');

const {parseTextFromHTML, seedItemToDatabase, buildItemObject} = require('../test-utils');
const {connectDatabaseAndDropData, disconnectDatabase} = require('../database-utils');

const findElement = (htmlAsString, selector) => {
    const element = jsdom(htmlAsString).querySelector(selector);
    if (element !== null) {
      return element;
    } else {
      throw new Error('Element not found in HTML string');
    }
};

describe('Sever path /videos', () => {

    beforeEach(connectDatabaseAndDropData);
    afterEach(disconnectDatabase);

    describe('default', () => {
        it ('returns the status code of 302', async () => {
            // exercise
            const response = await request(app).get('/');
            assert.equal(response.status, 302);
        });
    });

    describe('without existing videos', () => {
        it ('returns page with empty #videos-container', async () => {
            const response = await request(app).get('/videos');
            const result = _ => {parseTextFromHTML(response.text, '.video-card')};
            assert.throw(result, Error);
        });
    });

    describe('with an existing video', ()=> {
        it ('renders the page with the item', async() => {
            const video = await seedItemToDatabase();
            const response = await request(app).get('/videos');

            const iframe = findElement(response.text, '.video-player');
            assert.equal(iframe.src, video.videoUrl);
            assert.include(parseTextFromHTML(response.text, '.video-title'), video.title);
        });
    });
});