---
layout: post
title:  "Imogen Heap"
date:   2018-08-23 00:13:37 -0666
categories: 
 - vr
 - wave
image: /img/imogenheap/title.jpg
---

VR Volumetric Music Video Experience for Imogen Heap

<!--more-->


<iframe width="800" height="415" src="https://www.youtube.com/embed/HoDqeunBH10" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/1oTDIkbK1vw" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

[Oculus Blog](https://www.oculus.com/blog/a-new-sensation-the-glitch-mob-brings-see-without-eyes-to-thewavevr-on-rift/)


## *Volumetric Capture*

In December 2015 we went to Imogen Heap's house outside London for her 40th birthday celebration, and recorded her performance with a kinect using DepthKit Software

<video width="800" height="400" playsinline autoplay muted preload="auto" loop >
    <source src="{{ site.baseurl }}/assets/img/imogenheap/tree.webm"  type="video/webm"  />
</video>

<div id="grid">
{% assign myArray = "" | split:"|"  %}

{% for image in site.static_files %}
  {% if image.path contains page.imageDir %}
  {% if myArray contains image.path %}
  {% else %}
<a href="{{image.path}}"> <img src="{{image.path}}"/> </a>
  {% assign myArray = myArray | push: image.path %}
  {% endif %}
  {% endif %}
{% endfor %}
</div>






