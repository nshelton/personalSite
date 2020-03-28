---
layout: post
title:  "See Without Eyes"
date:   2018-06-21 00:13:37 -0666
categories: 
 - vr
 - wave
image: /img/SeeWithoutEyes/title.png
---

Interactive VR Music video Experience
<!--more-->


<iframe width="800" height="400" src="https://www.youtube.com/embed/70H3Sv6lxIY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## *THE FILM*

[Strangeloop Studios](https://www.strangeloop-studios.com/) created a 50 minute film to accompany the entire album. This gave us plenty of reference. We also shared assets and they actually rendered some sequences from the film in Unity, giving us a decent starting point. 

## *VR SCREENSHOTS*

We ended up getting several songs chopped into to shorter mixes, and created several scenes. Some were solitary experiences, and others were multiplayer. All scenes had some sort of interactivity. 

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

## *FAN VIDEOS* 


<iframe width="560" height="315" src="https://www.youtube.com/embed/1oTDIkbK1vw" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## *PRESS* 

[Oculus Blog](https://www.oculus.com/blog/a-new-sensation-the-glitch-mob-brings-see-without-eyes-to-thewavevr-on-rift/)



