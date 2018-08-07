const {assert} = require('chai');
const {buildItemObject} = require('../test-utils');


describe ('create page', () => {
    describe ('visits the page', () => {
        it ('should include elements required to create form', () => {
            browser.url('/videos');
            const url = browser.getUrl();
            browser.click('a[href="/videos/create"]');

            assert.equal(browser.getAttribute('form', 'method'), 'post');
            assert.equal(browser.getAttribute('form', 'action'), url)
            assert.equal(browser.getTagName('#video-title'), 'input');
            assert.equal(browser.getTagName('#video-description'), 'textarea');
            assert.equal(browser.getValue('input[type="submit"]'), 'Save a Video');
        });
    });
    describe ('creates a new item', () => {
        it ('returns new item on landing page', () => {
            const videoToAdd = buildItemObject();

            browser.url('/videos');
            browser.click('a[href="/videos/create"]');

            browser.setValue('#video-title', videoToAdd.title);
            browser.setValue('#video-url', videoToAdd.videoUrl);
            browser.setValue('#video-description', videoToAdd.description);
            browser.click('input[type="submit"]');

            assert.include(browser.getText('.video-title'), videoToAdd.title);
            assert.include(browser.getAttribute('.video-player', 'src'), videoToAdd.videoUrl);
            assert.include(browser.getText('.video-description'), videoToAdd.description);
        });
    });
});