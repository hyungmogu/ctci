const {assert} = require('chai');
const request = require('supertest');
const {jsdom} = require('jsdom');

const app = require('../../app');

const {parseTextFromHTML, seedItemToDatabase} = require('../test-utils');
const {connectDatabaseAndDropData, diconnectDatabase} = require('../setup-teardown-utils');

const findImageElementBySource = (htmlAsString, src) => {
  const image = jsdom(htmlAsString).querySelector(`img[src="${src}"]`);
  if (image !== null) {
    return image;
  } else {
    throw new Error(`Image with src "${src}" not found in HTML string`);
  }
};

describe('Server path: /items/:id', () => {
  beforeEach(connectDatabaseAndDropData);

  afterEach(diconnectDatabase);

  // Write your test blocks below:
  describe('GET', () => {
    it ('returns 200 status code', async () => {
      // setup
      const item = await seedItemToDatabase();
      const response = await request(app).get('/items/' + item._id);
      assert.equal(response.status, 200);
    });

    it ('returns non-empty response', async () => {
      const item = await seedItemToDatabase();
      const response = await request(app).get('/items/' + item._id);
      assert.notEqual(response.text, '');
    });

    it ('renders page with info from database', async () => {
      const item = await seedItemToDatabase();
      const response = await request(app).get('/items/' + item._id);

      assert.include(parseTextFromHTML(response.text, '#item-description'), item.description);
      const imageElement = findImageElementBySource(response.text, item.imageUrl)
      assert.include(imageElement.src, item.imageUrl);
      assert.include(parseTextFromHTML(response.text, '#item-title'), item.title);
    });
  });
});
