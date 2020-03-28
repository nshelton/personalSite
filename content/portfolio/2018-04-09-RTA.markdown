---
layout: post
title:  "Ṛta"
date:   2017-12-30 00:13:37 -0666
categories: 
 - vr
 - fractals
imageDir: /assets/img/form2
thumbnail: "thumbnail.png"
---

Realtime VR Fractal Sandbox



<iframe style="width:100%; height:500px"  src="https://www.youtube.com/embed/68MLIvqXd7w" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
Newer version with no postproc for graphics testing



Ṛta is the principle of natural order which regulates and coordinates the operation of the universe and everything within it. In the hymns of the Vedas, Ṛta is described as that which is ultimately responsible for the proper functioning of the natural, moral and sacrificial orders.

Free VR Fractal Visualizer & Manipulation Software for Vive

I am excited to share the next version of the FORM fractal visualizer, using a new compute shader surface calculation and rendering architecture. 

[Download Binary (15MB)](https://drive.google.com/open?id=1ea164UWn9x5WuYugKTxV0gwAGHqHQGtW)

*As with the first FORM, this is also beta software*

i'd love for anyone who has any feedback to email me: nshelton at gmail dot com


# *Background & Previous Work*

Raymarching is an elegant way to describe and render awesome fractals and mathematical structures but full frame raymarching quite expensive for VR, limiting the complexity of the distance field and the types of lighting and effects.  How crazy can we make them ? Below are some details.

I've made a bunch of interactive fractal shaders on many platforms and wanted to try a different approach. Here are some examples of raymarching in a fragment shader, and some optimizations.

Shadertoy KIFS (click and drag)

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/llySW1?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>
[Enhanced Sphere Tracing, Keinert et.al 2014](http://erleuchtet.org/~cupe/permanent/enhanced_sphere_tracing.pdf)

iOS OpenGL Visualizer

[Temporal Reprojection]({{ site.baseurl }}{% link _posts/2016-07-10-iOS_mandelbox.markdown %}): This is an effective technique that reuses the previous frame's depth values and projects this into the current frame to save a lot of the computation necessary. It fails when distance fields are temporally changing and generally suffers from ghosting artifacts on occlusions. [Read more about my iOS fractal visualizer here]({{ site.baseurl }}{% link _posts/2016-07-10-iOS_mandelbox.markdown %}).

![Controls](/assets/img/iOSShaders/gallery/tumblr_obcchb2olz1qav1pyo4_1280.jpg)

HTC Vive

[FORM0]({{ site.baseurl }}{% link _posts/2017-06-11-FORM.markdown %})  : This was the first app I made for VR Fractals. You could get decent frame rates if you lowered the resolution of the vive display to about 60%. 

![Controls](/assets/img/artandvr/4.png)

None of these approaches were really fast enough to get awesome fractals at consistent high frame rates on full resolution. so I needed a more scalable approximation that didn't depend on the resolution of the device.


# *Rendering Architecture*

How else can you render a distance field ? We can either do point-based splat rendering, or run marching cubes on the field to extract the isosurface (more info on this approach coming soon). Since my goal here is to render fractals, points are a better bet to get the high frequency details. Also I saw this crazy talk by Alex Evans at Media Molecule about point based rendering so I thought it would be a good idea to try to render fractals with it.

![Controls](/assets/img/form2/rendering.png)


I present a new approach for rendering raymarched distance fields, which enables complex distance field visualization at 90FPS (Expecially suited for fractals). This is accomplished by progressive point cloud computation using a compute shader, separating the rendering from the compute. This technique is also highly scalable; the buffer sizes and number of buffers can be modified at runtime. This ensures the system achieves 90FPS on any platform, or can be used for HD offline renders (100ms + per frame). 


![Controls](/assets/img/form2/buffers.png)

# *Benchmarks*

 Benchmark system was HTC Vive + 980gtx


![Controls](/assets/img/form2/benchmarks.png)


## *Sampling Pattern*

![fovea](/assets/img/form2/SamplingPattern.png)

As a bit of an optimisation, I use a [foveated](https://en.wikipedia.org/wiki/Fovea_centralis) and [stochastic](https://web.cs.wpi.edu/~matt/courses/cs563/talks/antialiasing/stochas.html) sampling pattern to determine which points to raymarch. This works pretty well for current VR headsets, but could obviously be improved with actual eye tracking. 

![fovea](/assets/img/form2/fovea.png)

## *User Interface Features*

# *3D Trackball Manipulation* 

<video width="320" height="240" autoplay loop controls>
    <source src="{{ site.baseurl }}/assets/webm/FORMTrackball.webm"  type="video/webm"  />
Your browser does not support the video tag.
</video>

Same as the trackball before, but instead of doing it in the shader, it's all accomplished by Unity hierarchy objects which makes the code super simple [TrackballControl.cs]() 

Upon letting go of either grip, unparent the point cloud back to the root. 

# *3D Fractal Transform controls* 

Fractals are created by interatively applying a transform to each point and comparing the result against a distance function. This defines the surface. All this can seem very abstract when writing a shader for a 2D screen, but in the context of VR these transformations can be visualized as interactive, grabbable 3D points. Interacting with these objects inspires a more intuitive understanding of fractal mechanics. At the very least it allows for hours of fun flying through infinitely customizable fractal landscapes. 


![Controls](/assets/img/form2/3DUI.png)


# *Basic VR Slider UI*


![Controls](/assets/img/form2/colo7.PNG)

This is more or less the [SteamVR Interaction System Linear Drive](https://github.com/ValveSoftware/steamvr_unity_plugin/blob/e3d96761982eb5e19b380dafa8abd020ca693c4d/Assets/SteamVR/InteractionSystem/Core/Scripts/LinearDrive.cs)

Where I have two menus : 

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/ll2GD3?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

*Rendering* controls the [Cosine Gradient](http://iquilezles.org/www/articles/palettes/palettes.htm) parameters

*Raymarch* controls termination criteria, some raymarching parameters, stepping ratio, etc. 

These are in groups of 4 floats that are uploaded to the compute shader as `float4`

Also comes with a handy grabber handle to move menus around.


# *Screen Compute buffer Interface*

![Controls](/assets/img/form2/BufferControls.png)

Offers basic control over the amount of compute vs rendering each frame. 

*PointSize*: controls the point sprite size. This slightly affects rendering time, and allows for filling gaps.

*Points* number of points per buffer (in thousands)

*Buffers* number of buffers to render each frame


# *Instructions*

 - Vive Only Currently
 - Run SteamVR
 - [Download Binary (15MB)](https://drive.google.com/open?id=1ea164UWn9x5WuYugKTxV0gwAGHqHQGtW)
 - Unzip, Run the app, hit space bar to cycle through presets.


# *Controls*
![Controls](/assets/img/form2/FORM2Controls.png)

 - For more advanced options look at the left controller and there are 5 menus / UI that can be toggled on and off. use the *Z* key to toggle this UI

![Controls](/assets/img/form2/VelocityCurve.png)
 - Use the thumb pads on the controller to fly. Speed is proportional to the squared distance from your thumb to the center of the pad. 
 - The flight direction is the actual world space vector from the center of the pad to the thumb.
