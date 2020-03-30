---
layout: post
title:  "LEVELS"
date:   2016-10-30 
categories: 
 - fractals
 - webgl
image: img/levels/0.jpg
---
webgl audio-reactive iterative function system
<!--more-->

![header](/img/levels/l1.jpg)

![header](/img/levels/l2.jpg)

![header](/img/levels/l3.jpg)
 

[Live Demo here](http://nshelton.github.io/r/levels) play it some music with a beat and it should start dancing [ broken ]

while being a TA at [Gray Area](http://grayarea.org/) I worked on a fractal installation that I wanted to be educational.


## Background

----

I had been working with Raymarched Distance Fields for about a year and found a few cool techniques I was happy with: 

  * raymarching at half-res for performance

  * doing filtering at full res

  * adding noise

  * simulating wide-angle lens distortion

  * shading based only on iteration count indxing into colormaps

So I had sort of found a style. I wanted to learn other types of 3D fractals, and start developing my own. 

Greetz 2:

 - [Shadertoy : KIFS Flythrough - Shane](https://www.shadertoy.com/view/XsKXzc)

 - [Shadertoy: Menger Journey - Syntopia](https://www.shadertoy.com/view/Mdf3z7)

 - [Fractal Forums: Kaleidoscopic (escape time) IFS - Knighty](http://www.fractalforums.com/ifs-iterated-function-systems/kaleidoscopic-(escape-time-ifs))


## Goals

----

![header](/img/levels/example.jpg)

I think that most fractal artists don't attempt to explain anything about how the fractal is constructed, which is a shame!

To me, the coolest part about fractals is how crazy simple they are - how chaos can grow from simple rules. I believe this says something profound about our universe and how things don't need to be "designed" to be super complex! 

So I created a custom KIFS shader and exposed the parameters of translation and rotation to an iPad's gyroscope, as well as the number of levels and number of mirrors. 

My favorite KIFS I found is making the primitives long skinnies, and then adding a scale factor in between each iteration. Most others I had seen either didn't scale, or scaled down. I like scaling up because it gives you these huge environments that seem to go out forever, instead of giving infinite tiny detail.

#### scaling down
![header](/img/levels/smaller.jpg)

#### scaling up
![header](/img/levels/bigger.jpg)

In the interactive version, you can still try out both kinds of scales.

The whole thing can be simplified in terms of the math / programming by just creating a 4x4 matrix transform which represents the iteration transform. This contains scale, and 3 dimensional rotation and translation. The scale could also be 3 dimentional, but haven't tried that yet. I use homogenous coordinates here to make the scaling and translation and rotation into a 4D matrix multiplication. This can be computed on CPU side so the shader doesn't have to do a ton of redundant sin and cos

~~~ glsl

uniform mat4 iterationTranform
...

float DE(vec3 p)
{
  vec4 p_homo = vec3(p, 1.0);
  float distance = 0.0;

  for ( int i = 0; i < iterationCount; i ++)
  {

    p_homo = iterationTransform * p_homo;
    
    p_homo = mirrorFunction(p_homo);

    distance = min(primitive(p_homo.xyz), distance);

  }
  
  return distance;

}
~~~

## Audio Reactivity & Interactivity
----
Again, using the fantastic [ThreeAudio.js](https://github.com/unconed/ThreeAudio.js/) from [Acko](http://acko.net/). Doesn't seem to be under development anymore, but I find the beat detection and FFT analysis much better than the stock WebAudio FFT.

![header](/img/levels/touchosc.jpg)

For an interactive installtion, I wanted to focus on 3D controls, since this is a 3D system. 
I wanted to communicate the idea that the iteration transform is composed of a translation, rotation and mirrors.

So, the Gyro of the iOS device controls rotation, if ROTATION is selected. And the same with TRANSLATION, which is a bit weird because people aren't used to orientation corresponding to a translation. Maybe a better way would be to integrate the accelorometer to get the movement, but this could be very noisy. Sill needs some development.

Also wanted to get a way to change the iteration count to show the levels of complexity. So I made this quick UI in TouchOSC. It communicates with a node server serving the page, and Websockets the data into the page in realtime. It's really super fast, I had doubts, but it looks like OSC + node + websockets could actually be a legit way to do low-latency audiovisuals. Will definitely work on this some more.

 
## Exhibitions

I showed this at the Gray Area Creative Coding Immersive Showcase for ffall 2016, where I was a TA
 
 {{<gallery levels>}}