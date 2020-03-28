---
layout: post
title:  "Atlanta "
date:   2015-07-18 00:13:37 -0666
categories: 
 - dataviz
image: /img/atlanta/thumb.jpg
---

geospatial vertex shader
<!--more-->



## Gallery ##
 
<script type="text/javascript">
  window.onload = function() {
    // var container = document.getElementsByClassName('post-list');
    var container = document.getElementById('grid');
    var wall = new Masonry( container, {
      columnWidth: 200
    });
  };
  </script>

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
