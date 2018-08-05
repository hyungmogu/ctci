const {assert} = require('chai');
const request = require('supertest');
const {jsdom} = require('jsdom');

const app = require('../../app');
const Item = require('../../models/item');

const {parseTextFromHTML, buildItemObject} = require('../test-utils');
const {connectDatabaseAndDropData, diconnectDatabase} = require('../setup-teardown-utils');

const findImageElementBySource = (htmlAsString, src) => {
  const image = jsdom(htmlAsString).querySelector(`img[src="${src}"]`);
  if (image !== null) {
    return image;
  } else {
    throw new Error(`Image with src "${src}" not found in HTML string`);
  }
};

describe('Server path: /items/create', () => {
  const itemToCreate = buildItemObject();

  beforeEach(connectDatabaseAndDropData);

  afterEach(diconnectDatabase);

  // Write your describe blocks below:
  describe('GET', () => {
    it ('returns 200 status code', async () => {
      const response = await request(app).get('/items/create').send();

      assert.equal(response.status, 200);
    });

    it ('returns non-empty response', async () => {
      const response = await request(app).get('/items/create').send();
      assert.notEqual(response.text, '');
    });

    it ('returns empty input fields', async () => {
      // NOTE: use of parseTextFromHTML is justified, because if it doesn't exist, error will be thrown

      // exercise
      const response = await request(app).get('/items/create').send();
      const titleInputText = _ => {parseTextFromHTML(response.text, 'input#title-input')};
      const imageUrlInputText = _ => {parseTextFromHTML(response.text, 'input#imageUrl-input')};
      const textareaInputText = _ => {parseTextFromHTML(response.text, 'textarea#description-input')};
      // verify
      assert.doesNotThrow(titleInputText, Error);
      assert.doesNotThrow(imageUrlInputText, Error);
      assert.doesNotThrow(textareaInputText, Error);

      assert.equal(parseTextFromHTML(response.text, 'input#title-input'), '');
      assert.equal(parseTextFromHTML(response.text, 'input#imageUrl-input'), '');
      assert.equal(parseTextFromHTML(response.text, 'textarea#description-input'), '');
    });
  });

  describe('POST', () => {
    it ('returns status code of 200', async () => {
      // setup
      const title = itemToCreate.title;
      const imageUrl = itemToCreate.imageUrl;
      const description = itemToCreate.description;
      // exercise
      const response = await request(app).post('/items/create').type('form').send({title, imageUrl, description});

      // verify
      assert.equal(response.status, 200);
    });

    it ('returns non-empty response', async () => {
      // setup
      const title = itemToCreate.title;
      const imageUrl = itemToCreate.imageUrl;
      const description = itemToCreate.description;
      // exercise
      const response = await request(app).post('/items/create').type('form').send({title, imageUrl, description});
      // verify
      assert.notEqual(response.text, '');
    });

    it ('returns response with submitted text', async () => {
      const title = itemToCreate.title;
      const imageUrl = itemToCreate.imageUrl;
      const description = itemToCreate.description;
      // exercise
      const response = await request(app).post('/items/create').type('form').send({title, imageUrl, description});

      assert.include(parseTextFromHTML(response.text, 'div.item-title'), title);
      const imageElement = findImageElementBySource(response.text, imageUrl);
      assert.equal(imageElement.src, imageUrl);
      assert.include(parseTextFromHTML(response.text, 'div.item-title'), title);
    });
  });
});
