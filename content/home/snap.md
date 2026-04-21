---
layout: post
title:  "Snap Inc / Spectacles"
date:   2026-03-01 00:00:00 -0600
categories: 
 - reconstruction
 - mobile
image: img/snap/thumbnail.jpg
recent: true
---
Gaussian Splatting rendering optimization for mobile AR hardware.
<!--more-->

## Overview

In 2026 i had a brief stint at Snap Inc in *Santa Monica* working on their graphics team. I was mostly working on the shader pipeline, and got familiar with the *Lens Studio* project, codebase and how they handle various graphics systems. I did not realize they they had essentially built their own game engine ! Each "lens" which most people would call "filters" (though they discourtage this word) is a self-contained scene with assets and javascript that gets evaluated and rendered on whatever device is running it.

Unfortunately about 6 weeks ater starting they did some company-wide restructuring and then let me go! 


## Lens Studio

{{<image "/img/snap/lensStudio.png">}}


[Lens Studio Download](https://ar.snap.com/lens-studio-dl)


## Gaussian Splatting on Mobile

{{<image "/img/snap/specs.png">}}


[these glasses have a GPU!](https://www.spectacles.com/)


Worked on optimizing 3D Gaussian Splatting renderers for the constrained GPU and thermal budgets of mobile AR hardware. This involved Vulkan and OpenGL shader compilation pipelines tuned for mobile architectures, like *Spectacles*.


## Tools

Vulkan, OpenGL, C++, Android, Gaussian Splatting
