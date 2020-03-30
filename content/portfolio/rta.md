---
layout: post
title:  "Ṛta"
date:   2017-12-30 00:13:37 -0666
categories: 
 - vr
 - unity
 - fractals
image: img/form2/thumbnail.jpg
---

Free VR Fractal Visualizer & Manipulation Software for Vive

{{<youtube 68MLIvqXd7w>}}

Ṛta is the principle of natural order which regulates and coordinates the operation of the universe and everything within it. In the hymns of the Vedas, Ṛta is described as that which is ultimately responsible for the proper functioning of the natural, moral and sacrificial orders.

I am excited to share the next version of the FORM fractal visualizer, using a new compute shader surface calculation and rendering architecture. 

 [ ⬇️ Download for SteamVR (15MB)](https://drive.google.com/open?id=1ea164UWn9x5WuYugKTxV0gwAGHqHQGtW)

[ ⬇️ Download for Oculus Rift (32MB)](https://drive.google.com/file/d/1xEG6LB45_u6HT1qNlwrGXG9j_FKWxFE4)

*As with the first FORM, this is also beta software*

i'd love for anyone who has any feedback to email me: nshelton at gmail dot com


# Background & Previous Work

Raymarching is an elegant way to describe and render awesome fractals and mathematical structures but full frame raymarching quite expensive for VR, limiting the complexity of the distance field and the types of lighting and effects.  How crazy can we make them ? Below are some details.

I've made many interactive fractal shaders on many platforms and wanted to try a different approach. Here are some examples of raymarching in a fragment shader, and some optimizations.

Shadertoy KIFS (click and drag)

{{<shadertoy llySW1>}}
[Enhanced Sphere Tracing, Keinert et.al 2014](http://erleuchtet.org/~cupe/permanent/enhanced_sphere_tracing.pdf)

iOS OpenGL Visualizer

[Temporal Reprojection]( {{<ref "ios_mandelbox.md">}}): This is an effective technique that reuses the previous frame's depth values and projects this into the current frame to save a lot of the computation necessary. It fails when distance fields are temporally changing and generally suffers from ghosting artifacts on occlusions. [Read more about my iOS fractal visualizer here]( {{< ref ios_mandelbox.md >}}).

![Controls](/img/iosshaders/gallery/tumblr_obcchb2olz1qav1pyo4_1280.jpg)

HTC Vive

[FORM0][Temporal Reprojection]( {{<ref "FORM.md">}})  : This was the first app I made for VR Fractals. You could get decent frame rates if you lowered the resolution of the vive display to about 60%. 

![Controls](/img/artandvr/4.jpg)

None of these approaches were really fast enough to get awesome fractals at consistent high frame rates on full resolution. so I needed a more scalable approximation that didn't depend on the resolution of the device.


# Rendering Architecture

How else can you render a distance field ? We can either do point-based splat rendering, or run marching cubes on the field to extract the isosurface (more info on this approach coming soon). Since my goal here is to render fractals, points are a better bet to get the high frequency details. Also I saw this crazy talk by Alex Evans at Media Molecule about point based rendering so I thought it would be a good idea to try to render fractals with it.

![Controls](/img/form2/rendering.jpg)


I present a new approach for rendering raymarched distance fields, which enables complex distance field visualization at 90FPS (Expecially suited for fractals). This is accomplished by progressive point cloud computation using a compute shader, separating the rendering from the compute. This technique is also highly scalable; the buffer sizes and number of buffers can be modified at runtime. This ensures the system achieves 90FPS on any platform, or can be used for HD offline renders (100ms + per frame). 


![Controls](/img/form2/buffers.jpg)

# Benchmarks

 Benchmark system was HTC Vive + 980gtx


![Controls](/img/form2/benchmarks.jpg)


# Sampling Pattern

![fovea](/img/form2/samplingpattern.jpg)

As a bit of an optimisation, I use a [foveated](https://en.wikipedia.org/wiki/Fovea_centralis) and [stochastic](https://web.cs.wpi.edu/~matt/courses/cs563/talks/antialiasing/stochas.html) sampling pattern to determine which points to raymarch. This works pretty well for current VR headsets, but could obviously be improved with actual eye tracking. 

![fovea](/img/form2/fovea.jpg)

# User Interface Features

## 3D Trackball Manipulation

{{<webm "/webm/FORMTrackball.webm">}}


Same as the trackball before, but instead of doing it in the shader, it's all accomplished by Unity hierarchy objects which makes the code super simple [TrackballControl.cs]() 

Upon letting go of either grip, unparent the point cloud back to the root. 

## 3D Fractal Transform controls

Fractals are created by interatively applying a transform to each point and comparing the result against a distance function. This defines the surface. All this can seem very abstract when writing a shader for a 2D screen, but in the context of VR these transformations can be visualized as interactive, grabbable 3D points. Interacting with these objects inspires a more intuitive understanding of fractal mechanics. At the very least it allows for hours of fun flying through infinitely customizable fractal landscapes. 


![Controls](/img/form2/3dui.jpg)


## Basic VR Slider UI


![Controls](/img/form2/colo7.jpg)

This is more or less the [SteamVR Interaction System Linear Drive](https://github.com/ValveSoftware/steamvr_unity_plugin/blob/e3d96761982eb5e19b380dafa8abd020ca693c4d/SteamVR/InteractionSystem/Core/Scripts/LinearDrive.cs)

Where I have two menus : 

{{<shadertoy ll2GD3 >}}

*Rendering* controls the [Cosine Gradient](http://iquilezles.org/www/articles/palettes/palettes.htm) parameters

*Raymarch* controls termination criteria, some raymarching parameters, stepping ratio, etc. 

These are in groups of 4 floats that are uploaded to the compute shader as `float4`

Also comes with a handy grabber handle to move menus around.


## Screen Compute buffer Interface

![Controls](/img/form2/buffercontrols.jpg)

Offers basic control over the amount of compute vs rendering each frame. 

*PointSize*: controls the point sprite size. This slightly affects rendering time, and allows for filling gaps.

*Points* number of points per buffer (in thousands)

*Buffers* number of buffers to render each frame


# Instructions

 - Vive Only Currently
 - Run SteamVR
 - [Download Binary (15MB)](https://drive.google.com/open?id=1ea164UWn9x5WuYugKTxV0gwAGHqHQGtW)
 - Unzip, Run the app, hit space bar to cycle through presets.


# Controls

![Controls](/img/form2/form2Controls.jpg)

 - For more advanced options look at the left controller and there are 5 menus / UI that can be toggled on and off. use the *Z* key to toggle this UI

![Controls](/img/form2/velocitycurve.jpg)
 - Use the thumb pads on the controller to fly. Speed is proportional to the squared distance from your thumb to the center of the pad. 
 - The flight direction is the actual world space vector from the center of the pad to the thumb.
