const {assert} = require('chai');
const Video = require('../../models/video');

const {connectDatabaseAndDropData, disconnectDatabase} = require('../database-utils');

describe ('Model: video', () => {
  beforeEach(connectDatabaseAndDropData);
  afterEach(disconnectDatabase);

  describe('title', () => {
    it ('should be a string', () => {
      // setup
      const expected = {
        title: 1,
        description: 'hello world'
      }

      const video = new Video(expected);

      assert.equal(video.title, '1');
    });

    it ('requires title', async () => {
      const itemToInsert = {
        imageUrl: 'abcdef',
        description: 'efgh'
      };

      const item = await new Video(itemToInsert);
      item.validateSync();

      assert.equal (item.errors.title.kind, 'required');
      assert.equal(item.errors.title.message, 'Path `title` is required.');

    });
  });

  describe('videoUrl', () => {
    it ('should be a string', () => {
      const expected = "1";
      const itemToInsert = {
        title: '12345',
        videoUrl: 1,
        description: 'efgh'
      }

      const item = new Video(itemToInsert);
      assert.equal(item.videoUrl, expected);
    });

    it ('requires videoUrl', async () => {
      const itemToInsert = {
        title: 'hello world',
        description: 'efgh'
      };

      const item = await new Video(itemToInsert);
      item.validateSync();

      assert.equal (item.errors.videoUrl.kind, 'required');
      assert.equal(item.errors.videoUrl.message, 'Path `videoUrl` is required.');
    });
  });
});
