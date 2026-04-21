---
layout: post
title:  "Disney Imagineering R&D"
date:   2024-06-01 00:00:00 -0600
categories: 
 - cv
 - ml
 - reconstruction
 - installation
image: img/disney/thumbnail.jpg
---
Projection mapping, computer vision, 3D reconstruction, and real-time tracking for Walt Disney Imagineering R&D.
<!--more-->

## Overview

From 2023 to 2024 I worked as a contractor at *Walt Disney Imagineering's R&D group in Glendale* on computer vision, 3D reconstruction, and real-time tracking systems. 

Most of this is under NDA and i really don't want Disney to sue me so I'll just post obviously public information and photos. Some of the work I did was related to these projects, or maybe the code found its way in there. The R&D group is very serparated from what actually happens at the park and spends most of their time making prototypes.

I basically spent a lot of time combining really nice industrial vision *cameras* and *projectors* with really expensive *GPU clusters* to make *magic*.

{{<image "/img/disney/droids.jpg">}}

from [disneytouristblog](https://www.disneytouristblog.com/inside-imagineering/)

Probably the most visible project to come out of R&D was these walking droid trained with simulated reinforcement learning. These guys were super cool. *I did not have anything to do with this* but they were sometimes walking around my desk area. 


{{<image "/img/disney/holotile.jpg">}}

from [disneytouristblog](https://www.disneytouristblog.com/inside-imagineering/)

Obligitory photo of lanny and the holotile floor. I was tangentially involved in this one. I worked on a couple of projects with Lanny, what a legend.

## Moana: Journey of Water

{{<image "/img/disney/moana.jpg">}}

One of the more public displays of the tracking tech we built was in  [Moana: Journey of Water](https://disneyworld.disney.go.com/attractions/epcot/journey-of-water/) at EPCOT. This attraction uses real-time sensing for the park guests to control the water!


## Patents

Disney loves to patent things... I pretty quickly got involved in a patent for tracking laser beams. You can probably google the rides at disneyland that invole laser beams...

{{<image "/img/disney/patent.png">}}

**U.S. Patent Application No. 18/389,346** — *High Frame Rate Light Beam Collision Detection* (2025). [View on Google Patents](https://patents.google.com/patent/US20250153050A1)

A second patent application for *Interactive Sensing Techniques* is also in progress. I am pretty excited about this one!

## Tools

Python, C++, OpenCV, PyTorch, ONNX, OpenVINO, COLMAP, Nerfstudio, ROS, Docker, Linux, DINO-ViT 
