---
layout: post
title:  "Paintings"
date:   2017-01-01 00:13:37 -0666
categories: 
 - analog
 - small 
imageDir: /assets/img/art/scans
thumbnail: "dp.jpg"
---

Some paintings I did in high school & college

<script type="text/javascript">
  window.onload = function() {
    // var container = document.getElementsByClassName('post-list');
    var container = document.getElementById('grid');
    var wall = new Masonry( container, {
      columnWidth: 400
    });
  };
  </script>

<div id="grid">
{% assign myArray = "" | split:"|"  %}

{% for image in site.static_files %}
  {% if image.path contains page.imageDir %}
  {% if myArray contains image.path %}
  {% else %}
<a href="{{image.path}}"> <img src="{{image.path}}" width="400"/> </a>
  {% assign myArray = myArray | push: image.path %}
  {% endif %}
  {% endif %}
{% endfor %}
</div>
