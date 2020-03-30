---
layout: post
title:  "Lynx Laboratories"
date:   2014-02-01 20:32:03 -0800
categories: 
 - ml
 - 3DScanning
image: /img/lynx/thumbnail.jpg"

---

First realtime mobile 3D scanner

<iframe width="560" height="315" src="https://www.youtube.com/embed/RjE68w3nBHw" frameborder="0" allowfullscreen></iframe>

This product was a fully mobile device (box) that could do real-time 3D scanning totally on the device. No cloud or offline processing.

Back at UT I joined a research group called the UT Perception lab. There we worked on realtime 3D reconstruction techniques using GPU processing. I helped implement Kinect Fusion in CUDA, a CUDA raytracer for scanning volume visualizaiton and other 3D reconstruction techniques using heightmaps on manifolds. 

I also designed all the hardware and handled sourcing motherboards, screens, controls, and manufacturing the case. 

Our team won international awards and presented our work at industry conferences:

 - Nvidia GTC
 - General Motors Innovation Day
 - SBIR Innovation Summit
 - Idea To Product Austin Winners

<iframe width="560" height="315" src="https://www.youtube.com/embed/Da2KGKTynOo" frameborder="0" allowfullscreen></iframe>

We went on to get additional [NSF SBIR phase II funding](https://www.sbir.gov/sbirsearch/detail/704651) to continue 3D scanning research.

I worked on some cool projects during this time including:

## HD Texture mapping on 3D scans


To improve visual quality of 3D scans, textures are just as important as the geometry (if not more). The VGA camera built in the Microsoft Kinect is not suitable for texture mapping, so we connected a HD webcam to the sensor. I created and implemented a novel image alignment technique and used state-of-the-art texture blending techniques.

With standard per-vertex color:
<div class="sketchfab-embed-wrapper"><iframe width="640" height="480" src="https://sketchfab.com/models/k8oqeZwGFAP6rL5rihIPaquVHeu/embed" frameborder="0" allowvr allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" onmousewheel=""></iframe>

<p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;">
    <a href="https://sketchfab.com/models/k8oqeZwGFAP6rL5rihIPaquVHeu?utm_medium=embed&utm_source=website&utm_campain=share-popup" target="_blank" style="font-weight: bold; color: #1CAAD9;">head2.ply</a>
    by <a href="https://sketchfab.com/lynxlabs?utm_medium=embed&utm_source=website&utm_campain=share-popup" target="_blank" style="font-weight: bold; color: #1CAAD9;">lynxlabs</a>
    on <a href="https://sketchfab.com?utm_medium=embed&utm_source=website&utm_campain=share-popup" target="_blank" style="font-weight: bold; color: #1CAAD9;">Sketchfab</a>
</p>
</div>

With HD texturing:

<div class="sketchfab-embed-wrapper"><iframe width="640" height="480" src="https://sketchfab.com/models/1a085558fbab46cab06801779d5a1426/embed" frameborder="0" allowvr allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" onmousewheel=""></iframe>

<p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;">
    <a href="https://sketchfab.com/models/1a085558fbab46cab06801779d5a1426?utm_medium=embed&utm_source=website&utm_campain=share-popup" target="_blank" style="font-weight: bold; color: #1CAAD9;">Elise </a>
    by <a href="https://sketchfab.com/lynxlabs?utm_medium=embed&utm_source=website&utm_campain=share-popup" target="_blank" style="font-weight: bold; color: #1CAAD9;">lynxlabs</a>
    on <a href="https://sketchfab.com?utm_medium=embed&utm_source=website&utm_campain=share-popup" target="_blank" style="font-weight: bold; color: #1CAAD9;">Sketchfab</a>
</p>
</div>



## 3D Sensor (Structured Light) Calibration

Accuracy of our 3D scans was was Lynx Labs primary competitive advantage, after the speed and simple interface. To get globally consistent room-scale models we improved upon the standard calibration of the Structure Sensor and implemented a custom stereo vision pipeline. 

Reconstruction using factory calibration :
![uncalibrated](/assets/img/lynx/uncalibrated.jpg)
Reconstruction using custom calibration and stereo vision pipeline :
![calibrated](/assets/img/lynx/calibrated.jpg)



