---
layout: post
title:  "Illuminant Surgical"
date:   2024-06-01
categories: 
 - cv
 - medical
 - reconstruction
image: img/illuminant/thumbnail.jpg
---
Real-time surgical projection mapping and 3D fiducial tracking for image-guided surgery.
<!--more-->

## Overview

From 2024 to 2026 I was Senior Software Engineer at Illuminant Surgical, building real-time projection mapping systems for surgical navigation. Key personnel on NSF and NIH SBIR grants.

<!-- TODO: add hero image of projection mapping system -->
{{<image "/img/illuminant/placeholder.jpg">}}

## SIGGRAPH 2025

Our work was presented at SIGGRAPH 2025:

**Poster** — *Skylight: Real-Time Projection Mapping for Surgical Navigation Leveraging Skin-Adhered Fiducials*. [ACM Digital Library](https://dl.acm.org/doi/10.1145/3721250.3743042)

**Workshop** — *XR in Medicine*. [ACM Digital Library](https://dl.acm.org/doi/10.1145/3736539.3737499)

<!-- TODO: add photo from SIGGRAPH poster session -->

## Fiducial Localization

Achieved 100x speedup and 10x accuracy improvement on DICOM fiducial localization by implementing a custom HLSL DirectX Compute shader pipeline. This replaced a CPU-bound algorithm with a massively parallel GPU implementation.

<!-- TODO: add before/after performance comparison diagram -->

## Camera-Projector Calibration

Designed and operated a precision calibration darkroom for camera-projector-tracker alignment using custom Python convex nonlinear optimization scripts. This enabled sub-millimeter accuracy for surgical projection mapping.

<!-- TODO: add photo of calibration setup or diagram -->

## Provisional Patent

*System and Method for Real-Time Projection of 3D Medical Image Information onto a Patient's Body via Tracking of Skin Fiducials* (2025).

## Tools

Unity, C#, HLSL DirectX Compute, Python, OpenCV, SciPy, DICOM
