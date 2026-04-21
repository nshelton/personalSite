---
layout: post
title:  "Life After BOB"
date:   2021-08-16 00:13:37 -0600
categories: 
 - unity

image: img/labob/9.jpg
recent: true
---

## Real Time Unity short Film

What if an AI could do the job of living your life better than you?

Neural engineer Dr. Wong has installed an experimental AI named BOB (“Bag of Beliefs”) into the nervous system of his 10-year-old daughter Chalice. Designed to guide Chalice through the challenges of growing up in a volatile world, BOB confronts more and more of the conflicts in Chalice’s life on her behalf, while Chalice grows increasingly irrelevant and escapist. As Dr. Wong begins to favor the BOB side of his daughter, and as BOB threatens to do the job of living Chalice’s life better than she can, Chalice jealously wonders: what is left for her classic human self to do?

read more at [https://lifeafterbob.io/](https://lifeafterbob.io/)


{{<youtube vCc2djR25hg>}}

# look development

My main role was working with Ian and the art team on different toon-style shaders in unity, but just adding so many controls and tools and *spicy* bits so that they could really control the lighting and look. The rendering style was partially inspired by the game [Inside](https://en.wikipedia.org/wiki/Inside_(video_game)) :
{{<image "/img/labob/inside.jpg">}}


I started making a basic toon shader that quantized the standard dot(normal, light), and then adding some texture in, messing with some custom shadow filters, and color overrides for pretty much every stage of the lighting pipeline.

{{<image "/img/labob/toon.jpg">}}

i like the kind of watercolor effect / artifact the shadows are doing here


## Concept art
{{<image "/img/labob/style_convo_02.jpg">}}
## Unity Mesh + Lightmap
{{<image "/img/labob/apartment.jpg" image2>}}
{{<image "/img/labob/lightmap.jpg" image2>}}
## Standard Shader
{{<image "/img/labob/interiorNormal.jpg">}}
## With Toon shader and post
{{<image "/img/labob/image.jpg">}}
{{<image "/img/labob/style.jpg">}}
{{<image "/img/labob/image2.jpg">}}

## Light Shafts Post Effect

I started making some raymarching for volumetric lighting effects. (You can see it a bit in the above shot) This was implemented as a *unity post effect* in the postprocessing stack. Essentially you do a raymatch through the gbuffer and lookup the shadow map at each step. This can be optimized (like in *inside*) with jittery subsampling and some temporal denoising, but I have a 2080 and didnt have to optimise anything lol.

{{<image "/img/labob/lightshaft0.jpg">}}
{{<image "/img/labob/lightshaft1.jpg">}}
{{<image "/img/labob/lightshaft3.jpg">}}

## holy order independent transparency batman

{{<image "/img/labob/distort0.jpg">}}
{{<image "/img/labob/distort1.jpg">}}
standard grabpass glass blur effect

## trippy look dev ?

we worked a lot on interesting looks for the "Wavyverse" - mostly using *vertex distortion* and *projection matrix tricks*
{{<image "/img/labob/wavyverse1.jpg">}}
{{<image "/img/labob/wavyverse2.jpg">}}
{{<image "/img/labob/wavyverse3.jpg">}}
just some simplex noise displacement, but with different planes! like a trippy depth of field...

# some cool shots
{{<image "/img/labob/0.jpg">}}
{{<image "/img/labob/1.jpg">}}
{{<image "/img/labob/2.jpg">}}
{{<image "/img/labob/3.jpg">}}
{{<image "/img/labob/4.jpg">}}
{{<image "/img/labob/5.jpg">}}
{{<image "/img/labob/6.jpg">}}
{{<image "/img/labob/7.jpg">}}
{{<image "/img/labob/8.jpg">}}
{{<image "/img/labob/10.jpg">}}
{{<image "/img/labob/11.jpg">}}
{{<image "/img/labob/12.jpg">}}

# exhibitions
[The Shed NYC](https://theshed.org/program/142-ian-cheng-life-after-bob) ~ Sept 10 - Dec 19 2021

[Luma Zurich](https://www.worldartfoundations.com/luma-westbau-ian-cheng-life-after-bob/?v=7516fd43adaa_) ~ Sept 17 - Oct 30 2021

*Luma Arles* ~ June 26 - Oct 30 2021

Coming to *Light Art Space Berlin* ~ Spring 2022




