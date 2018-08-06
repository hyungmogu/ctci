const {jsdom} = require('jsdom');
const Video = require('../models/video');

// Create and return a sample Item object
const buildItemObject = (options = {}) => {
  const title = options.title || 'My favorite video';
  const description = options.description || 'Just the best video';
  return {title, description};
};

// Add a sample Item object to mongodb
const seedItemToDatabase = async (options = {}) => {
  const video = await Video.create(buildItemObject(options));
  return video;
};

// extract text from an Element by selector.
const parseTextFromHTML = (htmlAsString, selector) => {
  const selectedElement = jsdom(htmlAsString).querySelector(selector);
  if (selectedElement !== null) {
    return selectedElement.textContent;
  } else {
    throw new Error(`No element with selector ${selector} found in HTML string`);
  }
};

module.exports = {
  buildItemObject,
  seedItemToDatabase,
  parseTextFromHTML,
};
