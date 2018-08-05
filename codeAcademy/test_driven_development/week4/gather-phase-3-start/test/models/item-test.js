const Item = require('../../models/item');
const {assert} = require('chai');
const {mongoose, databaseUrl, options} = require('../../database');

describe('Model: Item', () => {
  beforeEach(async () => {
    await mongoose.connect(databaseUrl, options);
    await mongoose.connection.db.dropDatabase();
  });

  afterEach(async () => {
    await mongoose.disconnect();
  });

  // Write your tests below:
  describe('title', () => {
    it ('should be a string', () => {
      // setup
      const expected = "1";
      const itemToInsert = {
        title: 1,
        imageUrl: 'abcdef',
        description: 'efgh'
      }

      // exercise
      const item = new Item(itemToInsert);
      assert.equal(item.title, expected);
    });

    it ('requires title', async () => {
      const itemToInsert = {
        imageUrl: 'abcdef',
        description: 'efgh'
      };

      const item = await new Item(itemToInsert);
      item.validateSync();

      assert.equal (item.errors.title.kind, 'required');
      assert.equal(item.errors.title.message, 'Path `title` is required.');

    });
  });

  describe('imageUrl', () => {
    it ('should be a string', () => {
      // setup
      const expected = "1";
      const itemToInsert = {
        title: '12345',
        imageUrl: 1,
        description: 'efgh'
      }

      // exercise
      const item = new Item(itemToInsert);
      assert.equal(item.imageUrl, expected);
    });

    it ('requires imageUrl', async () => {
      const itemToInsert = {
        title: 'hello world',
        description: 'efgh'
      };

      const item = await new Item(itemToInsert);
      item.validateSync();

      assert.equal (item.errors.imageUrl.kind, 'required');
      assert.equal(item.errors.imageUrl.message, 'Path `imageUrl` is required.');

    });
  });

  describe('description', () => {
    it ('should be a string', () => {
      // setup
      const expected = "1";
      const itemToInsert = {
        title: '12345',
        imageUrl: 'defgh',
        description: 1
      }

      // exercise
      const item = new Item(itemToInsert);
      assert.equal(item.description, expected);
    });

    it ('requires description', async () => {
      const itemToInsert = {
        title: 'hello world',
        imageUrl: 'efgh'
      };

      const item = await new Item(itemToInsert);
      item.validateSync();

      assert.equal (item.errors.description.kind, 'required');
      assert.equal(item.errors.description.message, 'Path `description` is required.');

    });
  });
});
