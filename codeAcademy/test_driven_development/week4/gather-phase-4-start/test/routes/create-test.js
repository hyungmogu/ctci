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

    it ('stores item to database', async () => {
      const title = itemToCreate.title;
      const imageUrl = itemToCreate.imageUrl;
      const description = itemToCreate.description;
      // exercise
      const response = await request(app).post('/items/create').type('form').send({title, imageUrl, description});

      const createdItem = await Item.findOne(itemToCreate);

      assert.isNotNull(createdItem, 'No item has been found');
    });

    it ('returns to root page after request', async () => {
      // setup

      // exercise
      const itemToCreate = buildItemObject();
      const response = await request(app).post('/items/create').type('form').send(itemToCreate);

      // status code of 302 is for redirect
      assert.equal(response.status, 302);
      assert.equal(response.header.location, '/');
    });

    it ('returns error with no title', async () => {
      // setup
      let itemToInsert = {
        imageUrl: itemToCreate.imageUrl,
        description: itemToCreate.description
      };

      const response = await request(app).post('/items/create').type('form').send(itemToInsert);

      assert.equal(response.status, 400);
      assert.include(parseTextFromHTML(response.text, 'form'), 'required');
    });

    it ('returns error with no imageUrl', async () => {
      // setup
      let itemToInsert = {
        title: itemToCreate.imageUrl,
        description: itemToCreate.description
      };

      const response = await request(app).post('/items/create').type('form').send(itemToInsert);

      assert.equal(response.status, 400);
      assert.include(parseTextFromHTML(response.text, 'form'), 'required');
    });

    it ('returns error with no description', async () => {
      // setup
      let itemToInsert = {
        title: itemToCreate.title,
        imageUrl: itemToCreate.imageUrl
      };

      const response = await request(app).post('/items/create').type('form').send(itemToInsert);

      assert.equal(response.status, 400);
      assert.include(parseTextFromHTML(response.text, 'form'), 'required');
    });
  });
});
