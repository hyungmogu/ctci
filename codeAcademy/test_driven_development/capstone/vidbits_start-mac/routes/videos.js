const router = require('express').Router();

const Video = require('../models/video');

router.get('/', async (req,res,next) => {
    res.redirect('/videos');
});

router.get('/videos', async (req, res, next) => {
    const videos = await Video.find({});
    res.render('index',{videos});
});

router.post('/videos', async (req,res,next) => {
    // get title and description from req.body
    const item = req.body;
    const video = new Video({
        title: item.title,
        description: item.description
    });

    // store retrieved data to database
    if (!video.title) {
        video.validateSync();
        res.status(400).render('create', {newVideo: video});
    } else {
        await video.save();
        const videos = await Video.find({});

        // send status cost of 201
        res.status(201).render('index',{videos});
    }
});

module.exports = router;