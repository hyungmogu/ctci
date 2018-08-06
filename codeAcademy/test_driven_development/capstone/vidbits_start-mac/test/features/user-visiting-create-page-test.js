const {assert} = require('chai');
const {buildItemObject} = require('../test-utils');


describe ('create page', () => {
    describe ('visits the page', () => {
        it ('should include elements required to create form', () => {
            // exercise
            browser.url('/');
            const url = browser.getUrl();
            browser.click('a[href="create.html"]');
            const form = browser.getHTML('form');

            // verify
            assert.equal(browser.getAttribute('form', 'method'), 'post');
            assert.equal(browser.getAttribute('form', 'action'), url + 'videos')
            assert.equal(browser.getTagName('#video-title'), 'input');
            assert.equal(browser.getTagName('#video-description'), 'textarea');
            assert.equal(browser.getValue('input[type="submit"]'), 'Save a Video');
        });
    });
    describe ('creates a new item', () => {
        it ('adds new item on landing page', () => {
            const videoToAdd = buildItemObject();

            browser.url('/');
            browser.click('a[href="create.html"]');

            browser.setValue('', videoToAdd.title);
            browser.setValue('', videoToAdd.description);
            browser.click('input[type="submit"]');

            assert.include(browser.getText('body'), 'Create Video');
            assert.include(browser.getText('#videos-container'), videoToAdd.title);
            assert.include(browser.getText('#videos-container'), videoToAdd.description);
        });
    });
});