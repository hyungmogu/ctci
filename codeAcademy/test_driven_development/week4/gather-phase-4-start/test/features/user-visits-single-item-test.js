const {assert} = require('chai');
const {buildItemObject} = require('../test-utils');

describe('single item page', () => {
    describe('user visits detail page after creating item', () => {
        it ('shows item info', () => {
            const title = buildItemObject().title;
            const description = buildItemObject().description;
            const imageUrl = buildItemObject().imageUrl;

            //exercise
            browser.url('/items/create');
            browser.setValue('#title-input', title);
            browser.setValue('#description-input', description);
            browser.setValue('#imageUrl-input', imageUrl);
            browser.click('#submit-button');
            browser.click('.item-card a');

            // verify
            assert.include(browser.getText('#item-title'), title);
            assert.include(browser.getAttribute('.single-item-img img', 'src'), imageUrl);
            assert.include(browser.getText('.single-item-description'), description);
        });
    });
});