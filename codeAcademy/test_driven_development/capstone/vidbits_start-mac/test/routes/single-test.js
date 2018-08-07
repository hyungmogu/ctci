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

describe('Server path /videos/:id', () => {
    beforeEach(connectDatabaseAndDropData);

    afterEach(disconnectDatabase);

    // Write your test blocks below:
    describe('GET', () => {
      it ('returns 200 status code', async () => {
        // setup
        const video = await seedItemToDatabase();
        const response = await request(app).get('/videos/' + video._id);
        assert.equal(response.status, 200);
      });

      it ('returns non-empty response', async () => {
        const video = await seedItemToDatabase();
        const response = await request(app).get('/videos/' + video._id);
        assert.notEqual(response.text, '');
      });

      it ('renders page with info from database', async () => {
        const video = await seedItemToDatabase();
        const response = await request(app).get('/videos/' + video._id);

        assert.include(parseTextFromHTML(response.text, '.video-title'), video.title);
        assert.include(parseTextFromHTML(response.text, '.video-description'), video.description);
      });
    });
  });
