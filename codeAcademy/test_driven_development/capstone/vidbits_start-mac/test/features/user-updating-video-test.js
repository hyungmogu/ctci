const {assert} = require('chai');
const {buildItemObject} = require('../test-utils');


describe ('edit page', () => {
    describe ('visits the page', () => {
        it ('should modify elements', () => {
            const newTitle = 'Change the error message';
            const videoToAdd = buildItemObject();

            browser.url('/videos/create');
            browser.setValue('#video-title', videoToAdd.title);
            browser.setValue('#video-url', videoToAdd.videoUrl);
            browser.setValue('#video-description', videoToAdd.description);
            browser.click('input[type="submit"]');

            // videos/:id/edit
            browser.click('a#edit');
            browser.setValue('#video-title', newTitle);
            browser.setValue('#video-url', videoToAdd.videoUrl);
            browser.setValue('#video-description', videoToAdd.description);
            browser.click('input[type="submit"]');

            // videos/:id
            assert.include(browser.getText('.video-title'), newTitle);
            assert.include(browser.getAttribute('.video-player', 'src'), videoToAdd.videoUrl);
            assert.include(browser.getText('.video-description'), videoToAdd.description);

            browser.url('/');
            assert.notInclude(browser.getText('.video-title'), videoToAdd.title);
        });

        it ('should not have old title', () => {
            const newTitle = 'Change the error message';
            const videoToAdd = buildItemObject();

            browser.url('/videos/create');
            browser.setValue('#video-title', videoToAdd.title);
            browser.setValue('#video-url', videoToAdd.videoUrl);
            browser.setValue('#video-description', videoToAdd.description);
            browser.click('input[type="submit"]');

            // videos/:id/edit
            browser.click('a#edit');
            browser.setValue('#video-title', newTitle);
            browser.setValue('#video-url', videoToAdd.videoUrl);
            browser.setValue('#video-description', videoToAdd.description);
            browser.click('input[type="submit"]');

            browser.url('/');
            assert.notInclude(browser.getText('.video-title'), videoToAdd.title);
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