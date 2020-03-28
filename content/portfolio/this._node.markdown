---
layout: post
title:  "this._node"
date:   2015-11-20 20:32:03 -0800
categories: 
 - installation
 - facebook
 - dataviz
image: /img/thisnode/thumbnail.jpg
---

Interactive Facebook Graph Visualization  
<!--more-->

<iframe src="https://player.vimeo.com/video/150832778" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
<p><a href="https://vimeo.com/150832778">this._node at EAST</a> from <a href="https://vimeo.com/bymeredith">ByMeredith</a> on <a  href="https://vimeo.com">Vimeo</a>.</p>




A collaboration with [Tom Bandage](http://www.tombandage.com/).

Users log in on the website, and their connections are displayed in the space. I implemented a custom THREE.js 3D graph renderer, using a force-directed layout [[source]](https://github.com/nshelton/3d-graph-vis). Every line represents a single like, comment or photo tag shared between the two users. The 3D Structure spins slowly and responds to new users being added.

Featured at [East Austin Studio Tour](http://east.bigmedium.org/)

[DUE EAST](http://east.bigmedium.org/due_east.html) & [Chicon Collective](http://chicon.co/).

<div class="gallery">
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
