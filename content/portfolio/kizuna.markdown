---
layout: post
title:  "The Light - Kizuna AI / W&W"
date:   2019-03-10 00:13:37 -0666
categories: 
 - unity
 - fractals

image: img/kizuna/kizuna_Unity.PNG

---


At the Wave VR we made a Music video for [Internationally renown producers DJs W&W](https://www.wandwmusic.com/) for their musical collaboration with japanese [vtuber](https://en.wikipedia.org/wiki/Virtual_YouTuber) [Kizuna Ai](https://www.youtube.com/channel/UC4YaOt1yT-ZeyB0OmxHgolA/videos). 


{{<youtube YtU_sb4jYE8 >}}

We had to make this in like a week or two, so we 
Here's some Unity Workflow Documentation:



# Art Team
Aaron Lemke, Dare Matheson and [Daniel Sierra](http://optical-rhythm.com/) built this out of mostly kitbash assets and copious Unity postprocessing 
[Kitbash Neo Tokyo](https://kitbash3d.com/products/tokyo) 
{{<image "/img/kizuna/kitbash.jpg" image3>}}
{{<image "/img/kizuna/city.jpg" image3>}}


# Animation Data

The Kizuna mesh and mesh came straight from [Activ8](https://activ8.co.jp/) in [MikuMikuDance](https://en.wikipedia.org/wiki/MikuMikuDance) format

{{<image "/img/kizuna/mmd.png" image3>}}
{{<image "/img/kizuna/markers.png" image3>}}
{{<image "/img/kizuna/kizuna_Unity.PNG" image3>}}

MD skeleton vs Mocap Data skeleton, and cute little colliders on the hair to prevent self intersection when doing physics sim

{{<webm "/img/kizuna/danceTest.webm">}}


{{<image "/img/kizuna/c4d.jpg" image2>}}{{<image "/img/kizuna/unity.png" image2 >}}

Artists at Strangeloop Studios created the energy ball effect in Cinema4D. But the mograph animation didnt come through the fbx so I just hand animations and used some displacement shaders.

# Rendering workflow
We rendered spereate G-Buffer channels [Emission, Albedo, depth, etc] out of Unity into EXR sequences 


{{<image "/img/kizuna/channels.png"  >}}

Strangeloop Studios did the sick edit and comp in Premiere

{{<image "/img/kizuna/kizuna.png" "image2">}}{{<image "/img/kizuna/3.jpg" "image2">}}{{<image "/img/kizuna/4.jpg" "image2">}}



# Slush Tokyo
The video was debut at Slush tokyo with a sick laser sequence live to the video??? because why not?
We also got to set up our virtual raves at the Avex Future of Music Booth.

We also projection mapped three walls of a private club in Tokyo with a realtime 270 degree, 3 camera view

{{<image "/img/kizuna/club.jpg" image2>}}{{<image "/img/kizuna/slush.jpg" image2>}}
{{<image "/img/kizuna/fom.jpg" image2>}}{{<image "/img/kizuna/squad.jpg" image2>}}
