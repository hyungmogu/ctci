const {assert} = require('chai');
const {buildItemObject} = require('../test-utils');

describe('landing page', () => {
    describe('without videos', () => {
        it ('returns page with empty videos-container', () => {
            browser.url('/');
            assert.equal(browser.getText('#videos-container'), '');
        });

        it ('can navigate to videos/create.html', () => {
            browser.url('/');
            browser.click('a[href="create.html"]');

            assert.include(browser.getValue('input[type="submit"]'), 'Save a Video');
        });
    });
});