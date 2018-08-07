const {assert} = require('chai');
const {buildItemObject} = require('../test-utils');


describe ('show page', () => {
    describe ('clicks delete item', () => {
        it ('removes the item from main page', () => {
            const newTitle = 'Change the error message';
            const videoToAdd = buildItemObject();

            browser.url('/videos/create');
            browser.setValue('#video-title', videoToAdd.title);
            browser.setValue('#video-url', videoToAdd.videoUrl);
            browser.setValue('#video-description', videoToAdd.description);
            browser.click('input[type="submit"]');

            // videos/:id
            browser.click('#delete');

            assert.equal(browser.getText('#videos-container'), '');
        });
    });
});