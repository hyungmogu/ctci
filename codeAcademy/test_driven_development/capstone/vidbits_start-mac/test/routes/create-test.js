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
    const itemToInsert = buildItemObject();
    beforeEach(connectDatabaseAndDropData);
    afterEach(disconnectDatabase);

    describe('POST', () => {
        it ('returns the status code of 201', async () => {
            const response = await request(app).post('/videos').type('form').send(itemToInsert);

            assert.equal(response.status, 201);
        });

        it ('stores item to database', async () => {
            console.log(itemToInsert);
            const response = await request(app).post('/videos').type('form').send(itemToInsert);
            const video = await Video.findOne({});

            assert.equal(video.title, itemToInsert.title);
            assert.equal(video.description, itemToInsert.description);
        });

        it ('returns error with no title', async () => {
            let altItemToInsert = {
              description: itemToInsert.description
            };

            const response = await request(app).post('/videos').type('form').send(altItemToInsert);

            assert.equal(response.status, 400);
            assert.include(parseTextFromHTML(response.text,'form'), 'required');
        });

        it ('preserves other fiels with no title', async () => {
            let altItemToInsert = {
                description: itemToInsert.description
            };

            const response = await request(app).post('/videos').type('form').send(altItemToInsert);
            const titleInput = findElement(response.text, '#video-title');

            assert.equal(titleInput.value, '');
            assert.include(parseTextFromHTML(response.text,'textarea'), altItemToInsert.description);
        });

        // it ('redirects to landing page on submit', async () => {
        //     const itemToInsert = buildItemObject();
        //     const response = await request(app).post('/videos').type('form').send(itemToInsert);

        //     assert.equal(response.status, 302);
        //     assert.equal(response.header.location, '/');
        // });

        // it ('shows created video on landing page', async () => {
        //     // setup
        //     const itemToInsert = buildItemObject();

        //     // exercise
        //     const response = await request(app).post('/videos').type('form').send(itemToInsert);

        //     // verify
        //     assert.include(parseTextFromHTML(), itemToInsert.title);
        //     assert.include(parseTextFromHTML(), itemToInsert.description);
        // });
    });
});