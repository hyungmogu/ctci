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

      // exercise
      const video = new Video(expected);

      // verify
      assert.equal(video.title, expected.title);
    });
  });
});
