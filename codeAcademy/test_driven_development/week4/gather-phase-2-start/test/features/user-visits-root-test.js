const {assert} = require('chai');

describe('User visits root', () => {
  describe('without existing items', () => {
    it('starts blank', () => {
      browser.url('/');
      assert.equal(browser.getText('#items-container'), '');
    });
  });

  describe('clicking create.html', () => {
    it('can navigate to create.html', () => {
      const title = 'gather';

      browser.url('/');
      browser.click('a[href="create.html"]');

      assert.equal(browser.getText('#title'), title);
    })
  });
});
