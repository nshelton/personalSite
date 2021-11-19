---
layout: post
title:  "Growth Algorithms"
date:   2019-09-18 00:13:37 -0666
categories: 
 - generative
 - unity
image: img/growth/thumb.jpg
---

Along with fractals, I also got really into growth algorithms, especially making them run in realtime. 
It seems like a perfect intersection of design and art with computer science and math.

Here are various realtime versions of some interesting growth algorithms I have seen over the years.
 - Mesh based
 - Mesh Splitting / Spring and attractive forces
    - Diffusion-Limited Aggregation
 - Voxel based
  - Gray-Scott
  - Anisotropic Dendritic Solidification




<video width="250" controls autoplay loop>
<source src="/img/growth/split3.mp4" type="video/mp4" >
</video>

<video width="250"  controls autoplay loop>
<source src="/img/growth/dla.mp4" type="video/mp4" >
</video>

<video width="250" controls autoplay loop>
<source src="/img/growth/wrinkles2.mp4" type="video/mp4" >
</video>

# Mesh Based

These involve splitting a manifold (1d or 2d surface) and then moving the nodes around in a higher dimensional space to minimise overlap

The simplest version is a line, which can be split and curved to remove intersections:

 {{<image "/img/growth/inconvergent.jpg" image3 >}}

from [Anders Hoff (inconvergent)](https://inconvergent.net/generative/differential-line/)

You can also split a mesh, it is just more complicated:

 {{<image "/img/growth/split.jpg" image2 >}}
From [Growth Forms, George Hart 2009](https://www.georgehart.com/Growth/GrowthForms.pdf)

{{<image "/img/growth/thumb.jpg" image3 >}}
{{<image "/img/growth/shiny.jpg" image3 >}}
 
Mesh generated in unity, wireframe rendered in Blender



This was based on [mxsage cpp implementation](https://github.com/mxsage/growth/blob/master/src/simulation.cpp) of [Andy Lomas](http://www.andylomas.com/extra/andylomas_paper_cellular_forms_aisb50.pdf). 

I implemented it in a unity compute shader, but graph data structures are pretty tricky to implement on GPU. My version could only get about this big before something started bugging out and I never fixed it. oh well, this isn't really the most elegant method anyways.

# Diffusion Limited Aggregation

DLA is a way to generate branching structures. It simulates particles moving around and then depositing themselves on a surface, which grows. 



<video class="image3" controls autoplay loop>
<source src="/img/growth/dla2.mp4" type="video/mp4" >
</video>

There was no advection here, just random particle movement. 
This uses unity sopheres and colliders, which got quite slow as unity only supoorts around 10,000 colliders maximum. 

{{<image "/img/growth/grow4.png" image3 >}}
{{<image "/img/growth/grow5.png" image3 >}}

These particles were advected using divergence-free curl noise

<video width="500" height="350" controls autoplay loop>
<source src="/img/growth/dla.mp4" type="video/mp4" >
</video>
<video width="250"  controls autoplay loop>
<source src="/img/growth/dla3.mp4" type="video/mp4" >
</video>

This is DLA running in a voxel grid in realtime in Unity, making it a hybrid of the next approach.

There are particles moving through a volume and depositing when they hit a cell with a threshold. 
The volume is being diffused a bit over time, so it looks like it's melting and smoothing a bit.
An isosurface is rendered with marching cubes and colored based on the laplacian (curvature) of the scalar field. 


# Voxel Based

I like thhis a lot more because the equations are very simple and GPUs are fast at doing 3D texture updates with compute shaders.

This technique computes scalar fields and updates them with some differential equations. 
the most well known is probably turing patterns, using [gray scott ](https://mrob.com/pub/comp/xmorphia/) equations. These generalize to 3D 


<video width="250"  controls autoplay loop>
<source src="/img/growth/gray.mp4" type="video/mp4" >
</video>
 {{<image "/img/growth/gray scott.jpg">}}

[live demo](https://nshelton.github.io/webgl-shader-demos/rd-fluid-vort.html)

Dendritic solidification, Laplacian growth

I was intrigued by [Nervous System](https://n-e-r-v-o-u-s.com/projects/albums/laplacian-growth/) and wondered how to implement this in real time using compute shaders.

 {{<image "/img/growth/formula1.jpg" image3 >}}


They just showed these equations briefly at the beginning of a video once

 {{<image "/img/growth/formula2.jpg" image3 >}}
 
 
Eventually I found this paper  [Ryo Kobayashi 1994](https://projecteuclid.org/download/pdf_1/euclid.em/1062621004) with a similar equation. notably the m is now dependeat on the temperateure and gradient of the phase field, creating anisotropic growth. 

The simulation works by storing the temperature and phase of each cell of the grid.
The temperature spreads out (dT), according to the phase change of neighboring cells. Heat is absorbed at the solid/liquid boundary to 
The phase changes (dp) similar to a traveling wave along the interface
In this case liquid would be phase=0, solid phase=1


<video width="500" height="350" controls autoplay loop>
<source src="/img/growth/cube.mp4" type="video/mp4" >
</video>

<video width="500" height="350" controls autoplay loop>
<source src="/img/growth/mushroom.mp4" type="video/mp4" >
</video>


These look like classic dendritic solidificaiton (above)

 {{<image "/img/growth/copper.jpg" image3 >}}

Pure copper crystal [wikipedia](https://en.wikipedia.org/wiki/Dendrite_(metal)#/media/File:Copper,_dendritic_crystal.tif)




<video width="500" height="350" controls autoplay loop>
<source src="/img/growth/wrinkles.mp4" type="video/mp4" >
</video>
<video width="500" height="350" controls autoplay loop>
<source src="/img/growth/wrinkles2.mp4" type="video/mp4" >
</video>


Lowering the anisotropy makes it looks more bulbous and organic like a fungus or something


<video width="500" height="350" controls autoplay loop>
<source src="/img/growth/thin.mp4" type="video/mp4" >
</video>


<video width="500" height="350" controls autoplay loop>
<source src="/img/growth/thin2.mp4" type="video/mp4" >
</video>

A pretty large variety of structures can be made with this system.

I will probably add more to this in the future as I mess with new algorithms.

# Inspiration, Links

more tbd

[inconvergent](https://inconvergent.net/generative/)

[deskriptiv](https://deskriptiv.com/)

[Nervous System](https://n-e-r-v-o-u-s.com/)