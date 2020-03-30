---
layout: post
title:  "OpenSWR"
date:   2014-02-01 20:32:03 -0800
categories: 
 - dataviz
image: img/openswr/intel-logo.jpg
---

Low-level OpenGL driver development


<iframe width="560" height="315" src="https://www.youtube.com/embed/c_td8epBihg" frameborder="0" allowfullscreen></iframe>

video: isosurface extraction and realtime rendering of a shit ton of triangles on a xeon phi cluster (no GPUs!)

In 2015 I contracted for Intel's visualization department on an OpenGL driver optimised for many-core intel supercomputer clusters. With that many CPUs, you can treat the network as a GPU, with each core doing some work in a Tile-Based Deferred Rendering (TBDR) pipeline. This was built on the Mesa3D graphics library and greatly improved frame rates on certain systems compared to the built in software renderer in Mesa3D (llvmpipe). It is now a part of the open source OpenMesa3D graphics library.

[http://openswr.org/](http://openswr.org/)


{{<gallery openswr>}}