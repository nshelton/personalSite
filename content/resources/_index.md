+++
date = 2016-11-06T07:30:25Z
title = "resources"

+++
I get many requests for resources about how I learned about raymarching fractals or general computer graphics stuff. So I started this page

Also I wish there was more active demoscene community in san francisco / austin / la / wherever so hopeflly somebody finds this helpful.

# Unity and Shaders

[Catlike Coding](https://catlikecoding.com/unity/tutorials/)

* [Rendering](https://catlikecoding.com/unity/tutorials/rendering/)
* [Scriptable Render Pipeline](https://catlikecoding.com/unity/tutorials/scriptable-render-pipeline/)

[Alan Zucconi](https://www.alanzucconi.com/ "View all posts by Alan Zucconi")

[Ronja's Shader Tutorials](https://www.ronja-tutorials.com/)

[Makin' Stuff Look Good In Unity](https://www.youtube.com/channel/UCEklP9iLcpExB8vp_fWQseg)

# Raymarching SDF & Fractals

## Mercury Demogroup

[Mercury.sexy](mercury.sexy) demogroup has created a [distance field library](http://mercury.sexy/hg_sdf/) with some cool stuff in there. Except they said that fractals are boring.

## Syntopia

Mikael Hvidtfeldt Christensen (creator of [Fragmentarium](http://syntopia.github.com/Fragmentarium/) and [Structure Synth](http://structuresynth.sourceforge.net/)) has an [excellent site](http://blog.hvidtfeldts.net/) with some great articles on distance field fractal rendering.

* [Mandelbox](http://blog.hvidtfeldts.net/index.php/2010/04/folding-space-the-mandelbox-fractal/)
* [Mandelbox II](http://blog.hvidtfeldts.net/index.php/2011/11/distance-estimated-3d-fractals-vi-the-mandelbox/)
* [Kaleidoscopic IFS](http://blog.hvidtfeldts.net/index.php/2010/06/folding-space-ii-kaleidoscopic-fractals/)

## Inigo Quilez

[http://www.iquilezles.org/](http://www.iquilezles.org/) this guy's home page is incredible I learned a ton of awesome stuff about graphics, shaders, and raymarching. Here are some articles I still refer to:

* [Path Tracing](http://www.iquilezles.org/www/articles/simplepathtracing/simplepathtracing.htm)
* [Distance Functions](http://iquilezles.org/www/articles/distfunctions/distfunctions.htm)
* [Distance Field Derivatives](http://www.iquilezles.org/www/articles/derivative/derivative.htm)
* [Nice Distance Field shadows](http://www.iquilezles.org/www/articles/rmshadows/rmshadows.htm)
* [Fog](http://www.iquilezles.org/www/articles/fog/fog.htm)

## General OpenGL / Math

[Song Ho Ahn](www.songho.ca) has some pages that I find myself coming back to when looking for matrix help:

* [Transforms](http://www.songho.ca/opengl/gl_transform.html)
* [Projection Matrix](http://www.songho.ca/opengl/gl_projectionmatrix.html)

Also [GPU Gems](https://developer.nvidia.com/gpugems/GPUGems3/gpugems3_pref01.html) is super legit and especially the chapter about fluid simulation. I've never taken college-level physics but was able to implement a GLSL navier-stokes pipline in a few days with it!

# GLSL Programming tools

## Interactive Shader Format

[https://www.interactiveshaderformat.com](https://www.interactiveshaderformat.com)
Mad by the good folks at VIDVOX (creators of [VDMX](http://vidvox.net/). The cool thing is that these can be saved as `.fs` files and dragged directly into VDMX. The parameters can be hooked up to audio analysis and LFO, OSC, MIDI, Wiimote, you name it!
I have a few [here](https://www.interactiveshaderformat.com/u/SHELTRON3030) that I have made, feel free to poke around.

## Shadertoy

another awesome resource and great community. Maybe I will add some of my favorite shaders in here eventually. You can find all kinds of stuff from basic tutorials to bind blowing fullly produced demo stuff.
[https://www.shadertoy.com](shadertoy)

# VJ Programs

## Programs Supporting Interactive Shader Format

These run custom shaders which can do audio analysis and parameter automation for your GLSL shaders with ISF
\* [VDMX](http://vidvox.net/) drag the `.fs` file into a Media Bin. These guys are awesome and will give you a discount if you write shaders on the interactive shader format website above.
\* [Magic Music Visuals](https://magicmusicvisuals.com/) you have to put the `.fs` files in a special folder somewhere and go to `Help > Additional Module Folders` to hook it up.

# Blogs

* [Fairlight](https://directtovideo.wordpress.com/)
* [Prideout](http://prideout.net/blog/)
* [Softology](https://softologyblog.wordpress.com/)
* [Tim Lottes](https://timothylottes.github.io/)

# Other Inspiration

* [SubBlue](http://sub.blue/)
* [Syntopia's Generative Art Links](http://blog.hvidtfeldts.net/index.php/generative-art-links/)
* [Evan Wallace's awesome WebGL stuff](http://madebyevan.com/)