const router = require('express').Router();

const Item = require('../models/item');

router.get('/', async (req, res, next) => {
  const items = await Item.find({});
  res.render('index', {items});
});

// Add additional routes below:
router.get('/items/create', async(req,res,next) => {
  res.render('create');
});

router.post('/items/create', async(req, res, next) => {
  const item = new Item(req.body);
  item.validateSync();

  if (item.errors) {
    console.log('!!!!!HERE');
    res.status(400).render('create', {newItem: item});
  } else {
    await item.save();
    res.redirect('/');
  }
});

module.exports = router;
