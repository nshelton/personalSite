---
layout: post
title:  "Ready Player One"
date:   2018-03-09 00:13:37 -0666
categories: 
 - vr
 - wave
image: img/rpo/arcades.png
---

Making of TheWaveVR's Distracted Globe
<!--more-->

<iframe src="https://player.vimeo.com/video/262891110" width="800" height="450" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

<iframe src="https://player.vimeo.com/video/259063906" width="800" height="450" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

For SXSW 2018 we tried our most ambitous project yet - recreating the *Distracted Globe* venue from the Ernest Cline's *Ready Player One* as a Venue in *TheWaveVR*.

Working with *Warner Brothers* and *ILM*, we got Maya/straight from the film. The goal was to somehow jam these into a VR Scene in Unity, complete with interactive visuals, dancing robots, and retro 80's themed arcade cabinets... We even met Stephen Spielberg in VR to get the green light. This was a super fun project, and while I was mainly working on some initial R&D for our Imogen Heap project, I was still able to work closely with the team to add some sweet effects.

## THE TEAM

Working out of [Strangloop Studios](https://www.strangeloop-studios.com/) in Culver City, we assembled an international team of weirdos to crank out this project in a mere *3 weeks* leading up to *SXSW 2018*.

[Taylor Shechet](https://twitter.com/_tlr_) Asset conversion // art pipeline 

[Dawn Rivers](https://twitter.com/DawnRivers) Unity lighting R&D

[Stuart Campbell aka Sutu Eats Flies](http://www.sutueatsflies.com/) Tilt Brush art  

[Aaron Lemke](https://twitter.com/aaronlemke) Putting it all together

[Sheltron](https://nshelton.github.io) Shaders // VFX


## SOME OF STU'S SICK TILT BRUSH DRAWINGS ##

<a href="/img/RPO/sutu0.jpg"> <img src="/img/RPO/sutu0.jpg" width="300"> </a>
<a href="/img/RPO/sutu1.jpg"> <img src="/img/RPO/sutu1.jpg" width="300"> </a>
<a href="/img/RPO/sutu2.jpg"> <img src="/img/RPO/sutu2.jpg" width="300"> </a>
<a href="/img/RPO/sutu3.jpg"> <img src="/img/RPO/sutu3.jpg" width="300"> </a>
<a href="/img/RPO/sutu4.jpg"> <img src="/img/RPO/sutu4.jpg" width="300"> </a>
<a href="/img/RPO/sutu5.jpg"> <img src="/img/RPO/sutu5.jpg" width="300"> </a>
<a href="/img/RPO/sutu6.jpg"> <img src="/img/RPO/sutu6.jpg" width="300"> </a>
<a href="/img/RPO/sutu7.jpg"> <img src="/img/RPO/sutu7.jpg" width="300"> </a>


## VISUAL EFFECTS

# LASER TEK

![IronGiant](/img/RPO/ironGiant.png)

<blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/p/BeoHwB_FCBk/?utm_source=ig_embed" data-instgrm-version="9" style=" background:#000; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:8px;"> <div style=" background:#F8F8F8; line-height:0; margin-top:40px; padding:50.0% 0; text-align:center; width:100%;"> <div style=" background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAsCAMAAAApWqozAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAMUExURczMzPf399fX1+bm5mzY9AMAAADiSURBVDjLvZXbEsMgCES5/P8/t9FuRVCRmU73JWlzosgSIIZURCjo/ad+EQJJB4Hv8BFt+IDpQoCx1wjOSBFhh2XssxEIYn3ulI/6MNReE07UIWJEv8UEOWDS88LY97kqyTliJKKtuYBbruAyVh5wOHiXmpi5we58Ek028czwyuQdLKPG1Bkb4NnM+VeAnfHqn1k4+GPT6uGQcvu2h2OVuIf/gWUFyy8OWEpdyZSa3aVCqpVoVvzZZ2VTnn2wU8qzVjDDetO90GSy9mVLqtgYSy231MxrY6I2gGqjrTY0L8fxCxfCBbhWrsYYAAAAAElFTkSuQmCC); display:block; height:44px; margin:0 auto -44px; position:relative; top:-22px; width:44px;"></div></div><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/p/BeoHwB_FCBk/?utm_source=ig_embed" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">A post shared by Nick Shelton (@nshelton)</a> on <time style=" font-family:Arial,sans-serif; font-size:14px; line-height:17px;" datetime="2018-01-31T20:21:16+00:00">Jan 31, 2018 at 12:21pm PST</time></p></div></blockquote> <script async defer src="//www.instagram.com/embed.js"></script>

Procedural laser sweeping through smoke effect based on [Domain Warping](http://www.iquilezles.org/www/articles/warp/warp.htm), simulation of camera exposure on laser sweeping side to side.
Originally used fully procedural 3D noise field but was too expensive for pixel shader. Ended up blending two 2D noise textures to make a beliveable 3D field.


# RUBIKS CUBE

<blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/p/Be9yUwXFnlw/?utm_source=ig_embed" data-instgrm-version="9" style=" background:#000; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:8px;"> <div style=" background:#F8F8F8; line-height:0; margin-top:40px; padding:50.0% 0; text-align:center; width:100%;"> <div style=" background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAsCAMAAAApWqozAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAMUExURczMzPf399fX1+bm5mzY9AMAAADiSURBVDjLvZXbEsMgCES5/P8/t9FuRVCRmU73JWlzosgSIIZURCjo/ad+EQJJB4Hv8BFt+IDpQoCx1wjOSBFhh2XssxEIYn3ulI/6MNReE07UIWJEv8UEOWDS88LY97kqyTliJKKtuYBbruAyVh5wOHiXmpi5we58Ek028czwyuQdLKPG1Bkb4NnM+VeAnfHqn1k4+GPT6uGQcvu2h2OVuIf/gWUFyy8OWEpdyZSa3aVCqpVoVvzZZ2VTnn2wU8qzVjDDetO90GSy9mVLqtgYSy231MxrY6I2gGqjrTY0L8fxCxfCBbhWrsYYAAAAAElFTkSuQmCC); display:block; height:44px; margin:0 auto -44px; position:relative; top:-22px; width:44px;"></div></div><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/p/Be9yUwXFnlw/?utm_source=ig_embed" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">A post shared by Nick Shelton (@nshelton)</a> on <time style=" font-family:Arial,sans-serif; font-size:14px; line-height:17px;" datetime="2018-02-09T06:19:20+00:00">Feb 8, 2018 at 10:19pm PST</time></p></div></blockquote> <script async defer src="//www.instagram.com/embed.js"></script>


Randomly does rubiks cube turns on the beat ! Will it eventually solve itself ?

# JETPACKS


![flying](/img/RPO/flying.jpg)
Wouldn't it be cool if you could fly around the venue like in the movie?! The grip buttons will shoot out little jet streams that you can aim, and move your roomscale. We were hesitant to do this at first, but actually everyone thought it was awesome and nobody threw up. 

# DISCO FLOOR

<video width="640" height="480" autoplay   preload="auto" loop controls>
    <source src="{{ site.baseurl }}/img/RPO/disco.webm"  type="video/webm"  />
Video not supported</video>

We made a new item. Users can spawn in cool animated disco-style floors like we saw in the scene, also hoping it would decreasee vertigo effects from flying (people like floors in VR...)

Animation by Strang   preload="auto" loop controls in C4D, custom audioreactive shader scrolling a noise texture on bass accumulator.

# KVANT SWARM

<video width="600" height="300" autoplay   preload="auto" loop controls>
    <source src="{{ site.baseurl }}/img/RPO/swarm.webm"  type="video/webm"  />
Video not supported</video>

Fun interactive streamer thing. Grab the attractor for the system and fly around! Audioreactive emission on this custom shader, [original effect](https://github.com/keijiro/KvantSwarm) created by [Keijiro Takahashi](https://github.com/keijiro).

Unfortunately some assholes would try to grief the DJ by flying around the DJ booth with the streamer so they couldn't see the deck. Should have seen that one coming. Also perf could get pretty rough if this shader is filling your entire screen.

# KVANT STREAK

![flying](/img/RPO/streak.png)
[anamorphic lens flare post effect](https://github.com/keijiro/KvantSwarm) created by [Keijiro Takahashi](https://github.com/keijiro). To get that 80's look? 


## THE EVENT

![Djing in VR ](https://www.austin360.com/rf/image_lowres/Pub/p9/Austin360/2018/03/09/Images/sxsw%20ready%20player%20one%2014.JPG)
Photo from [https://www.austin360.com](https://www.austin360.com)


Tye Sheridan from the movie for Djing the first show from Brazos hall during SXSW 2018.


[More Awesome photos of the event from superKaiju](https://www.superkaiju.com/sxsw-2018-ready-player-one-activation/)

Excellent production by [Giant Spoon](http://www.giantspoon.com/) and [Double A Events](https://www.doublea.com/)

Shoutout to the whole WaveVR team for making the event go smoothly.



## PRESS

[Forbes](https://www.forbes.com/sites/charliefink/2018/03/10/ready-player-one-vr-unveiled-at-sxsw/#2bafc7791de1) //
*"It was one of the most compelling VR experiences I've ever had"*

[VRScout](https://vrscout.com/news/inside-ready-player-one-oasis-sxsw/) // 
*"The Wave VR allows people to be immersed into the club scene right out of the film."*

[Venture Beat](https://venturebeat.com/2018/03/08/thewavevr-launches-ready-player-one-music-vr-experience-at-sxsw/)

[Fast Company](https://www.fastcompany.com/40542459/in-vr-steven-spielberg-is-a-cat-and-he-flies) // *"In VR, Steven Spielberg is a cat, and he flies"*

[TechCrunch](https://techcrunch.com/2018/04/19/thewavevr-wraps-a-6-million-series-a-to-fuel-its-immersive-social-vr-music-app/) // 
*"an experience that feels distinctly futuristic while drenching users in souped-up visuals that intertwine the emotion and connectedness of social VR with music that’s actively being created within the app."*

[Wired](https://www.wired.com/story/ready-player-one-vr/) //
*"an all-too-rare distillation of VR's greatest promise: Sharing something beautiful, and otherwise unattainable, with another person."*


## FAN VIDEOS

<iframe width="600" height="400" src="https://www.youtube.com/embed/inOiYI-EAWA" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

<iframe width="600" height="400" src="https://www.youtube.com/embed/OfAJI23nY90" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>