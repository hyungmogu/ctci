const router = require('express').Router();

const Video = require('../models/video');

router.get('/', async (req,res,next) => {
    res.redirect('/videos');
});

router.get('/videos/create', async (req, res, next) => {
    res.render('create');
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
        videoUrl: item.videoUrl,
        description: item.description
    });

    video.validateSync();

    // store retrieved data to database
    if (video.errors) {
        res.status(400).render('create', {newVideo: video});
    } else {
        await video.save();
        res.redirect('/videos/' + video._id);
    }
});

router.get('/videos/:id', async (req, res, next) => {
    const videoId = req.params.id;

    // get info about the video
    const video = await Video.findById(videoId);

    // render page
    if (!video) {
        res.status('400').send();
    } else {
        res.render('show', {video: video});
    }
});

router.get('/videos/:id/edit', async (req, res, next) => {
    const videoId = req.params.id;

    const video = await Video.findById(videoId);


    if (!video) {
        res.status('400').send();
    } else {
        res.render('edit', {newVideo: video});
    }
});

router.post('/videos/:id/updates', async (req, res, next) => {
    const itemId = req.params.id;
    const {title, videoUrl, description} = req.body;
    const video = new Video({title, videoUrl, description});

    video.validateSync();

    // store retrieved data to database
    if (video.errors) {
        res.status(400).render('edit', {newVideo: video});
    } else {
        await Video.findOneAndUpdate({_id: itemId}, {title, videoUrl, description});
        res.redirect('/videos/' + itemId);
    }
});

router.post('/videos/:id/deletions', async (req, res, next) => {
    const itemId = req.params.id;

    await Video.findByIdAndRemove(itemId);

    res.redirect('/');
});


module.exports = router;