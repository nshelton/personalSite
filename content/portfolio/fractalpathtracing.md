---
layout: post
title:  "Fractal Path Tracer"
date:   2020-02-20 00:13:37 -0666
categories: 
 - unity
 - fractals

image: img/fractalpathtracing/1.jpg

---

 I decided to take my fractal rendering to the NEXT LEVEL by implementing a simple compute shader path tracer in unity.

Code Mostly Lifted from [Three Eyed Games](http://three-eyed-games.com/2018/05/12/gpu-path-tracing-in-unity-part-2/) tutorial

[Source Code on github](https://github.com/nshelton/FractalPathTracing)


# Temporal Reprojection

But then I decided to reproject frames from the past into the current buffer to improve convergence, and make it pretty much realtime



# Renders

{{<gallery fractalpathtracing >}}