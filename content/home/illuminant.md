---
layout: post
title:  "Illuminant Surgical"
date:   2025-06-01
categories: 
 - cv
 - medical
 - reconstruction
image: img/illuminant/thumbnail.jpg
recent: true
---
Real-time surgical projection mapping and 3D fiducial tracking for image-guided surgery.
<!--more-->

{{<image "/img/illuminant/projection.png">}}

## Overview

From 2024 to 2026 I was *Senior Software Engineer* at Illuminant Surgical, building real-time projection mapping systems for surgical navigation. Key personnel on NSF and NIH SBIR grants. I worked on the instrument calibration, fiducial registration, system architecture and visualization. 

[[illuminant.ai]](https://www.illuminant.ai/)


{{<image "/img/illuminant/spine.png">}}



## SIGGRAPH 2025

Our work was presented at SIGGRAPH 2025:

{{<image "/img/illuminant/poster.png">}}

**Poster** — *Skylight: Real-Time Projection Mapping for Surgical Navigation Leveraging Skin-Adhered Fiducials*. [ACM Digital Library](https://dl.acm.org/doi/10.1145/3721250.3743042)

**Workshop** — *XR in Medicine*. [ACM Digital Library](https://dl.acm.org/doi/10.1145/3736539.3737499)

<!-- TODO: add photo from SIGGRAPH poster session -->

## Details

I learned a lot about spinal fusion procedures, and implemented a novel fiducial localization algorithm to find the skindots inside of CT scans. 

Also implemented a end-to-end calibration pipeline to jointly register the camera, depth image, infrared stereo 3D tracker and projector. The alignment was sub-mm for the 3D tracker and on the order of a few mm for the projections. 


## Grants Awarded

I got to be involved in writing some of these grants, providing updates and data analysis.

 - [SBIR Phase II: Novel Camera-Projector Device Leveraging Non-invasive Registration and Projected Augmented Reality for Navigation in Minimally Invasive Spine Procedures](https://www.sbir.gov/awards/215088)

 - [Software Development and Cadaveric Testing of Deformable Registration Pipeline in Novel Camera-Projector Surgical Navigation Device](https://www.sbir.gov/awards/213264)

 - [SBIR Phase I: Novel Camera-Projector Device Leveraging Markerless Skin Registration and Projected Augmented Reality Software to Enable Navigation for Minimally Invasive Procedures](https://www.sbir.gov/awards/208141)

 - [Scanner Agnostic Image-Guided Biopsy Platform Employing Advanced Computer Vision and Computer Graphics to Enable Non-Invasive Registration and Dynamic Projection Mapping](https://www.sbir.gov/awards/219862)

 
## Provisional Patent

*System and Method for Real-Time Projection of 3D Medical Image Information onto a Patient's Body via Tracking of Skin Fiducials* (2025).

## Tools

Unity, C#, HLSL DirectX Compute, Python, OpenCV, SciPy, DICOM
