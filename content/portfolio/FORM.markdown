---
layout: post
title:  "FORM 0.0 beta"
date:   2017-06-11 00:13:37 -0666
categories: 
 - vr
 - fractals
image: /img/form/thumbnail.png
---

Free VR Fractal Visualizer & Manipulation Software for Vive
<!--more-->

<iframe src="https://player.vimeo.com/video/224276393" width="800" height="450" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

Have you ever wanted to fly around in fractals in 3D in VR??? NOW YOU CAN 

FORM is a VR Fractal Visualizer, controller, and 3D manipulation

[Download Binary (15MB)](https://drive.google.com/file/d/0B5G6DAhx0gwlQVdvZFRGWG1TZTg/view?usp=sharing)

I haven't had time ot do all the features I wanted, so I decided to release it in its half baked state. 
"this is beta software"

i'd love for anyone who has any feedback to email me: nshelton at gmail dot com

# *Requirements*

 - VR compatible graphics card
 - HTC Vive
 - SteamVR



# *Running*

 - [Download Here](https://drive.google.com/file/d/0B5G6DAhx0gwlQVdvZFRGWG1TZTg/view?usp=sharing)
 - Unzip
 - run FORM.exe



# *Controls*
![Controls](/assets/img/form/controller.png)



# *Public Demo Tips:*

 - Click “disable sliders” on the onscreen GUI
 - Encourage clicking the thumb pad (next preset)




# *Flying*

 - Right Trigger = forward ; left trigger = backwards
 - Controller orientation controls flying direction.
 - The distance from the controller to head is the speed

 


# *Trackball Manipulation*

This is a common form of 3D manipulation on 2D screens. In VR it is slightly different, and will take some getting used to but it’s probably worth it because it’s awesome.
 
  
- hold the grip buttons on both hands simultaneously.
- The midpoint between the hands is the center of the trackball.
 
While gripping with both hands:

 - To *Translate*: Move both hands in the same direction
 - To *Scale*: Increase or decrease the distance between hands
 - To *Rotate*: Grip Points rotate around the trackball center
 


# *Advanced Controls*

Onscreen GUI toggles two types of controls I'm working on:

*Sliders* - using [NewtonVR](https://github.com/TomorrowTodayLabs/NewtonVR) for interactions, there are some sliders to manipulate fractal parameters. These can accidentally be clicked while using the trackball, and are very sensitive.

*3D Boxes* - The position and rotation of the gray and white box controls some parameters of the fractal. This is under development. Having these visible will override the preset when it is loaded, so it’s better to keep this hidden with the onscreen button.

For beginners or in a public scenario, the advanced controls should probably be disabled.



# *Common Pitfalls*

*Zooming in too far* : Zooming is awesome, but must be done carefully. You can zoom into the wrong spot, and totally change the scale of the world and then you won’t be able to go anywhere. There is LOD in the renderer that will make things further away less detailed. If you zoom in too far, everything will disappear. 



# *Known Issues*

Working on these

 - Squashed Worlds: Some presets are corrupted (because quaternions). So if there is a world that looks very distorted and flattened, just skip to the next one. Or check it out if you want. 
 
 - Inconsistent Scales: polygon geometry (controllers, sliders, ui) is rendered at a different scale than the fractal, so they don’t composite correctly. 

---

## *About the Fractals*



# *Mandelbox (_FractalType = 0.0)*


<iframe width="560" height="315" src="https://www.youtube.com/embed/bO9ugnn8DbE" frameborder="0" allowfullscreen></iframe>
[Krzysztof Marczak](https://www.youtube.com/channel/UC9wtVVoVJvJQ1t_eV3-86KQ) // YouTube

<img src="https://upload.wikimedia.org/wikipedia/en/8/8f/Mandelboxpwr2.png" alt="Mandelbox" style="width: 560px;"/>

[Wikipedia - Mandelbox](https://en.wikipedia.org/wiki/Mandelbox)

[Tom Lowe's site on the Mandelbox](https://sites.google.com/site/mandelbox/negative-mandelbox)
 
![syntopia mandelbox](http://blog.hvidtfeldts.net/media/mbx1.png)

[Syntopia](http://blog.hvidtfeldts.net/index.php/2011/11/distance-estimated-3d-fractals-vi-the-mandelbox/)

![mandelbox](/assets/img/form/mandelbox.png)

Screenshot from FORM



# *Hartverdrahtet Demo(_FractalType = 0.5)*

<iframe width="560" height="315" src="https://www.youtube.com/embed/0w_xEUoK79o" frameborder="0" allowfullscreen></iframe>

Straight out of this sick demo… Found this code which I still don’t understand but produces many interesting variants that are not seen in the original demo like:
 
![Hartverdrahtet](/assets/img/form/hart2.jpg)
![Hartverdrahtet](/assets/img/form/form1.png)
![Hartverdrahtet](/assets/img/form/form2.png)

Screenshots from FORM



# *Kaleidoscopic IFS(_FractalType = 1.0)*
 
I like using long skinnies for primitives instead spheres:
 
 ![ifs](https://nshelton.github.io/assets/img/levels/example.jpg)

Sphere based:

![knighty](/assets/img/form/knighty.png)

Knighty // Fractal Forums 	

<iframe width="560" height="315" src="https://www.youtube.com/embed/x0mRp05qabA" frameborder="0" allowfullscreen></iframe>

iq // Shadertoy	

![form](/assets/img/artandvr/vive2PNG.PNG)

long skinnies from form



# *Rendering*
 
Coloring - The renderer colors based on iteration count only, indexing into a color map. Some of my favorites (with more info) can be found here: [https://bids.github.io/colormap/](https://bids.github.io/colormap/)
 
![colormaps](/assets/img/form/colormaps.png)

For rendering efficiency - there is no lighting, normals calculation, fog, etc. I want to add some of this in the future.

The image is rendered at 60% resolution to keep the frame rate high. 

![colormaps](/assets/img/form/steamvr.png)

If you have a crappy card and are seeing frame rate issues, go to SteamVR Developer settings, and lower the resolution even further. I add some FXAA to try to cut down on aliasing. 

I have many ways to improve the visual detail, probably want to add lighting and fog and everything, using a progressive renderer like I have [experimented with on iOS](https://nshelton.github.io/fractals/ios/raymarcher/2016/08/10/iOS_mandelbox.html) . Also interested in the 3D UI which is pretty rough now but shows some promise. Stay tuned! 
