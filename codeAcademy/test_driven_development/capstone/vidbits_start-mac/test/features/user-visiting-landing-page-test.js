const {assert} = require('chai');
const {buildItemObject, seedItemToDatabase} = require('../test-utils');

const {disconnectDatabase} = require('../database-utils');
const {mongoose, databaseUrl, options} = require('../../database');

const generateUrl = function(domain) {
    return `http://${domain}/${Math.random()}`;
};


describe('landing page', () => {
    describe('without videos', () => {
        it ('returns page with empty videos-container', () => {
            browser.url('/');
            assert.equal(browser.getText('#videos-container'), '');
        });

        it ('can navigate to videos/create', () => {
            browser.url('/');
            browser.click('a[href="/videos/create"]');

            assert.include(browser.getValue('input[type="submit"]'), 'Save a Video');
        });
    });

    describe('with videos', () => {
        let video = {};
        beforeEach(async () => {
            await mongoose.connect(databaseUrl, options);
            await mongoose.connection.db.dropDatabase();
            video = await seedItemToDatabase();
        });

        afterEach(disconnectDatabase);

        it ('is shown', () => {
            browser.url('/videos');
            assert.notEqual(browser.getText('#videos-container'), '');
            assert.include(browser.getText('.video-title'), video.title);
        })

        it ('can navigate to videos/:id',  () => {
            browser.url('/videos');
            browser.click(`a[href="/videos/${video._id}"]`);
            const videoURL = browser.getAttribute('.video-player','src');
            assert.include(browser.getText('.video-title'), video.title);
            assert.equal(videoURL, video.videoUrl);
            assert.include(browser.getText('.video-description'), video.description);
        });
    });
});