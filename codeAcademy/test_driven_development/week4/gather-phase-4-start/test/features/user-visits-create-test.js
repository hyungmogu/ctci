const {assert} = require('chai');
const {buildItemObject} = require('../test-utils');

// Add your tests below:
describe('user visits create page', () => {
    describe('posts a new item', () => {
        it ('adds item to the collection', () => {
            const title = buildItemObject().title;
            const description = buildItemObject().description;
            const imageUrl = buildItemObject().imageUrl;

            //exercise
            browser.url('/items/create');
            browser.setValue('#title-input', title);
            browser.setValue('#description-input', description);
            browser.setValue('#imageUrl-input', imageUrl);
            browser.click('#submit-button');

            assert.include(browser.getText('body'), title);
            assert.include(browser.getAttribute('body img', 'src'), imageUrl);

        })
    })
});