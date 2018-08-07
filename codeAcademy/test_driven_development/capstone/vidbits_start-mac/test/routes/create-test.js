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

describe('Sever path /videos/create', () => {
    const itemToInsert = buildItemObject();
    beforeEach(connectDatabaseAndDropData);
    afterEach(disconnectDatabase);

    describe('POST', () => {
        it ('returns the status code of 302', async () => {
            const response = await request(app).post('/videos').type('form').send(itemToInsert);

            assert.equal(response.status, 302);
        });

        it ('stores item to database', async () => {
            const response = await request(app).post('/videos').type('form').send(itemToInsert);
            const video = await Video.findOne({});

            assert.equal(video.title, itemToInsert.title);
            assert.equal(video.videoUrl, itemToInsert.videoUrl);
            assert.equal(video.description, itemToInsert.description);
        });

        it ('returns error with no title', async () => {
            let altItemToInsert = {
              description: itemToInsert.description,
              videoUrl: itemToInsert.videoUrl
            };

            const response = await request(app).post('/videos').type('form').send(altItemToInsert);

            assert.equal(response.status, 400);
            assert.include(parseTextFromHTML(response.text,'form'), 'Path `title` is required.');
        });

        it ('returns error with no videoUrl', async () => {
            let altItemToInsert = {
                title: itemToInsert.title,
                description: itemToInsert.description
            };

            const response = await request(app).post('/videos').type('form').send(altItemToInsert);

            assert.equal(response.status, 400);
            assert.include(parseTextFromHTML(response.text,'form'), 'Path `videoUrl` is required.');
        });

        it ('redirects to /videos/:id on submit', async () => {
            const itemToInsert = buildItemObject();
            const response = await request(app).post('/videos').type('form').send(itemToInsert);
            const video = await Video.findOne({});

            assert.equal(response.status, 302);
            assert.equal(response.header.location, '/videos/' + video._id);
        });

        it ('preserves other fields with no title', async () => {
            let altItemToInsert = {
                description: itemToInsert.description,
                videoUrl: itemToInsert.videoUrl
            };

            const response = await request(app).post('/videos').type('form').send(altItemToInsert);
            const vieoUrlInput = findElement(response.text, '#video-url');
            const titleInput = findElement(response.text, '#video-title');

            assert.equal(vieoUrlInput.value, altItemToInsert.videoUrl);
            assert.equal(titleInput.value, '');
            assert.include(parseTextFromHTML(response.text,'textarea'), altItemToInsert.description);
        });

        it ('preserves other fields with no videoUrl', async () => {
            let altItemToInsert = {
                title: itemToInsert.title,
                description: itemToInsert.description
            };

            const response = await request(app).post('/videos').type('form').send(altItemToInsert);
            const vieoUrlInput = findElement(response.text, '#video-url');
            const titleInput = findElement(response.text, '#video-title');

            assert.equal(vieoUrlInput.value, '');
            assert.equal(titleInput.value, altItemToInsert.title);
            assert.include(parseTextFromHTML(response.text,'textarea'), altItemToInsert.description);
        });
    });
});