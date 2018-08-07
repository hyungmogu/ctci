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

describe('Sever path /videos/:id/delete', () => {
    const itemToInsert = buildItemObject();
    beforeEach(connectDatabaseAndDropData);
    afterEach(disconnectDatabase);

    describe('POST', () => {
        it ('removes the record Change the error message', async () => {

            const video = await seedItemToDatabase({
                title: 'Change the error message'
            });

            const response = await request(app).post(`/videos/${video._id}/deletions`).type('form');
            const deletedVideo = await Video.findById(video._id);
            console.log(deletedVideo);

            assert.isNull(deletedVideo);
            assert.equal(response.header.location, `/`);
        });
    })
});