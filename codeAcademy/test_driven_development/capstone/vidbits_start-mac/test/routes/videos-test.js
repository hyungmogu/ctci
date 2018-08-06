const {assert} = require('chai');
const request = require('supertest');
const {jsdom} = require('jsdom');

const app = require('../../app');
const Video = require('../../models/video');

const {parseTextFromHTML, seedItemToDatabase, buildItemObject} = require('../test-utils');
const {connectDatabaseAndDropData, disconnectDatabase} = require('../database-utils');


describe('Sever path /', () => {

    beforeEach(connectDatabaseAndDropData);
    afterEach(disconnectDatabase);

    describe('default', () => {
        it ('returns the status code of 200', async () => {
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

    describe('with existing videos', ()=> {
        it ('renders the page with the item', async() => {
            const item = await seedItemToDatabase();

            const response = await request(app).get('/videos');

            assert.include(parseTextFromHTML(response.text, '.video-title'), item.title);
        });
    });
});