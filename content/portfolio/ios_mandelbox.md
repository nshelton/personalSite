---
layout: post
title:  "iOS mandelbox raymarcher"
date:   2016-08-10 20:32:03 -0800
categories: 
 - fractals
image: img/iosshaders/thumb.jpg
---
Mobile fractal visualizer
<!--more-->

![feedback diagram](/img/iosshaders/header.jpg)

## Towards realtime mobile raytracing ##

This was an experiment, after using [SceneKit](https://developer.apple.com/reference/scenekit) for the Bridge Engine at Occipital in iOS, to see what I could do with solely a [SCNTechnique](https://developer.apple.com/reference/scenekit/scntechnique), full-frame shader. I was really inspired by this talk by Tim Lottes about filtering methods for realtime raymarching. What kind of quality could be achieved on an iPhone6 ? 

{{<youtube WzpLWzGvFK4>}}


## Render Loop ##

I didn't implement all of the crazy stuff he mentions within the SCNTechnique, but a few were easy to do:
 - half-resolution render
 - full-resolution reconstruction filter with temporal antialiasing
 - postprocessing shader (chromatic aberration here)


![feedback diagram](/img/iosshaders/fractalfeedback.jpg)

## Reconstruction ##

This shows what is going on every frame, with shaders in boxes and buffers in parallelograms. I'll briefly describe the reconstruction algorithm here. Whenever each low-resolution raymarch is computed, we treat this as an *observation* and integrate it into the *model* using backprojection.

For every pixel in the reconstruction:

 - get the depth of the pixel in the half-res trace you just did
 - project this into the full-res model from last frame
 - sample some neighbors in the reconstruction to get a weight
    - penalize large differences from occlusions
 -  assign a new value to the reconstruction, using
    - reconstruction from last frame
    - trace from this frame
    - hueristics based on neighborhood variance 

So the result is that you do a quarter of the work (half-res trace) but because you're reconstructing at full res, you get some automatic motion blur from the feedback, and the jittering means that the noise gets evened out and the image converges pretty quickly. I need to tweak the thresholds and weights, but I was happy with the results. 

![feedback  ](/img/iosshaders/taa.jpg)
this kind of just looks like a blur here. best results come while moving the camera.

## Gallery ##
all screengrabs from my iPhone6. Not all are realtime... frame rates displayed
 
{{<gallery iosshaders>}}