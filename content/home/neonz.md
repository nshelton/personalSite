---
layout: post
title:  "Neonz AR"
date:   2022-02-20 00:13:37 -0666
categories: 
 - unity
 - generative
 - art
 - ar
image: img/neonz/thumb.jpg
---
# AR NFT Viewer



In 2021, Sutu launched one of the first generative NFT series on the tezos blockshain, a 10,000 profile pic series called [Neonz](https://www.neonz.xyz/). This was deveoped by the folks at [Eyejack](https://www.eyejack.io/), I got on board to help them with some cool AR rendering effects.

I worked on a couple of components of the SUTUVERSE

 - Face filter - https://www.neonz.xyz/neonz-facez

 - NFT ART Viewer - https://www.neonz.xyz/neonz-signz

{{<image "/img/neonz/sutu.jpg" image3>}}
{{<image "/img/neonz/Sutuverse.png" image3>}}

# AR Lighting

The new ARKit stuff has some awesome new features for spatial perception - you can use either a realtime 3D scanned mesh to composite new types of lighting into a scene. On Android, you can get an estimated depth map, and compute lighting that way as well:





## Color and Depth
{{<image "/img/neonz/color.png" image3>}}
{{<image "/img/neonz/depth.png" image3>}}


The depth is not great quality, I think because it does it at a very low res, and then just interpolates. It somehow is both too smooth and too blocky at the same time, which is impressive. I think this was set to the "Fastest" quality so I'm not expecting anything great. (The Android results are even worse)


## Normals

{{<image "/img/neonz/normals.png" image3>}}
{{<image "/img/neonz/smoothNormals.png" image3>}}

Using the depth image, you can estimate normals. There's a lot of blocky artifacts because of the way the depth image is computed, so I do some smoothing.


## Basic Lights

{{<image "/img/neonz/lighting.png" image3>}}
{{<image "/img/neonz/lighting2.png" image3>}}


Directional Light, Point Light 

You can then do most kind of lighting calculations you would do with any real time rendering, using the estimated surface normal and the world position.


## Analytic lights
{{<image "/img/neonz/tubeLighting.png" image3>}}
{{<image "/img/neonz/composite.png" image3>}}

Then you can compute any type of light and just add it on to the scene.


I have based this example on some unity rendering command buffer samples such as:

https://docs.unity3d.com/2018.3/Documentation/Manual/GraphicsCommandBuffers.html

{{<image "/img/neonz/RenderingCommandBufferCustomLights.jpg" image3>}}


## iOS compatibility
I ran into a very strange issue where I could not get the buffer uploaded to the 

## Environment effects

I also created some fun effects for the experience which will add MORE NEON into the world - 


And wouldn't you know these are also released as some 


# AR Face Filter





https://ted.sutuverse.com/

# FaceTracking

