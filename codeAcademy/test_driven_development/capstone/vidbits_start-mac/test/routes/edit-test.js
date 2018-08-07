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

describe('Sever path /videos/:id/edit', () => {
    const itemToInsert = buildItemObject();
    beforeEach(connectDatabaseAndDropData);
    afterEach(disconnectDatabase);

    describe('GET', () => {
        it ('renders the form with values of the video', async () => {
            const video = await seedItemToDatabase();

            const response = await request(app).get(`/videos/${video._id}/edit`);
            const inputTitle = findElement(response.text, '#video-title');
            const inputUrl = findElement(response.text, '#video-url');
            const inputDescription = findElement(response.text, '#video-description');
            const form = findElement(response.text, 'form');

            assert.include(form.action, `/videos/${video._id}/updates`);
            assert.equal(inputTitle.value, video.title);
            assert.equal(inputUrl.value, video.videoUrl);
            assert.equal(inputDescription.value, video.description);
        });
    });

    describe('POST', () => {
        it ('redirects to show page upon updating', async () => {
            const video = await seedItemToDatabase();
            const modifiedVideo = {
                title: video.title,
                videoUrl: video.videoUrl,
                description: video.description
            };

            const response = await request(app).post(`/videos/${video._id}/updates`).type('form').send(modifiedVideo);

            assert.equal(response.status, 302);
            assert.equal(response.header.location, `/videos/${video._id}`);
        });

        it ('returns error with no title', async () => {
            const video = await seedItemToDatabase();
            let green = {
                videoUrl: video.videoUrl,
                description: video.description
            };

            const response = await request(app).post(`/videos/${video._id}/updates`).type('form').send(green);

            assert.equal(response.status, 400);
            assert.include(parseTextFromHTML(response.text,'form'), 'Path `title` is required.');
        });

        it ('returns error with no videoUrl', async () => {
            const video = await seedItemToDatabase();
            let green = {
                title: itemToInsert.title,
                description: itemToInsert.description
            };

            const response = await request(app).post(`/videos/${video._id}/updates`).type('form').send(green);

            assert.equal(response.status, 400);
            assert.include(parseTextFromHTML(response.text,'form'), 'Path `videoUrl` is required.');
        });

        it ('preserves other fields with no title', async () => {
            const video = await seedItemToDatabase();
            let green = {
                description: itemToInsert.description,
                videoUrl: itemToInsert.videoUrl
            };

            const response = await request(app).post(`/videos/${video._id}/updates`).type('form').send(green);
            const vieoUrlInput = findElement(response.text, '#video-url');
            const titleInput = findElement(response.text, '#video-title');

            assert.equal(vieoUrlInput.value, green.videoUrl);
            assert.equal(titleInput.value, '');
            assert.include(parseTextFromHTML(response.text,'textarea'), green.description);
        });

        it ('preserves other fields with no videoUrl', async () => {
            const video = await seedItemToDatabase();
            let green = {
                title: itemToInsert.title,
                description: itemToInsert.description
            };

            const response = await request(app).post(`/videos/${video._id}/updates`).type('form').send(green);
            const vieoUrlInput = findElement(response.text, '#video-url');
            const titleInput = findElement(response.text, '#video-title');

            assert.equal(vieoUrlInput.value, '');
            assert.equal(titleInput.value, green.title);
            assert.include(parseTextFromHTML(response.text,'textarea'), green.description);
        });
    })
});