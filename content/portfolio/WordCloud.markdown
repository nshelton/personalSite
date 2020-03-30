---
layout: post
title:  "Rap Word Cloud"
date:   2020-01-20 
categories: 
 - ml
 - unity
 - vr
image: /img/rrl/verbs.PNG
---

An Optimisaiton Journey. Client : [Rap Research Lab](https://rapresearchlab.com/)

<img src="https://lh4.googleusercontent.com/S6agD_LTrvX5_9dgCptzMPRUJDHWNSo1y9NAkvphhTDa8cWEdJvelwTFeYE7eFTD9yEyxMu-bmV3P7PUlTEECkZ4-b1uMmAyh0wvjRgjV-lu6bmaf4a5Stmi75YnDT3zlHiEOek" alt="">


<h3><a id="Rendering_5000_TextMeshPro_meshes_in_1ms_for_an_interactive_VR_word_cloud_7"></a>Rendering 5000 TextMeshPro meshes in 1ms for an interactive VR word cloud</h3>


I started with a naive 5000 TextMeshPro gameobjects, which could take 30ms CPU and GPU, and made a new system that took 1ms CPU and GPU and still looked dope.


<h1>Functionality</h1>


Interactive 3D visualization of words used in a corpus of rap lyrics (See Part 1)


<h3>Interface Features</h3>

- Left Thumb button transitions from Globe View to Word Cloud view
- Right hand controller has a “laser” which intersects with words to select them
- Clicking word with laser transports user to the word
- Words can also be selected with Right Hand controller Interaction point
- Selecting word with Right hand shows usage over time of the word and 10 similar words Timeline View
- Pressing both grips allows user to scale and rotate the word cloud.
- <strong>Runs in VR at 90fps on mid-tier hardware</strong>

<h3><a id="Visualization_Features_21"></a>Visualization Features</h3>
<ol>
- Words are color coded by part of speech
- Words are scaled by frequency of use
- Words are scaled by distance from user
- Words transition into points when they are far away
</ol>
<h1><a id="Implementation_27"></a>Implementation</h1>
<h2><a id="Initial_Approach_29"></a>Initial Approach</h2>


<img src="https://lh3.googleusercontent.com/c-wVAWx1NIr6hxbdiEc9fr6SgP8wbQ5Ri_P7L81B0wwmYBJKztACkQvUXSgv-T2el0l6GjwTX6N6KaBz3pWAvo1TwioROd1cwjC087M6Xm1AeC6Ars2EfZtbS4eDMYdJSVGqFwE" alt=""><br>
<em>builtin Unity TextMesh plus a backing quad</em><img src="https://lh6.googleusercontent.com/lmI1V-AYQXSFsvltFVbfl5-FxDamRU2RdAKNk1MUdgPp3GWTG3c1SBw9Sq8ti8kbWQvR9YNK-TZQfLxkcxxf84-GXyMz8AosfnrDhbNX_CC8QZteOMVWLCvTdBXsCA7xEMLd-kw" alt=""><br>
<em>5k TextMeshPro components in VR. Added some depth fog for depth perception purposes.</em>



{{<youtube d0p6xZ9SveE>}}


Since premature optimization is the root of all evil, I just did the simplest thing I could think of at first. Instantiate 5000 gameobjects with TextMeshPro on them and it actually worked at 60fps.  Add in my two-hand grip trackball I have used from my fractal visualizer to explore and zoom the cloud. The client complained of a “weird shimmery effect when moving” which usually means Oculus time warp. The rendering would hit 30 when looking at every element of the cloud at once which is rare. But, when I started making it interactive it was tough to:



- Manually get the text to face camera (GameObject.transform.LookAt(camera) 5k times)
- Rescale TMP transforms (TextMeshPro does some kind of recalculation on the rescale of a TMP component)
- Move Unity colliders (Causes Unity physics update)



Let’s check out the profiler…




Unity Profiler is tough to read sometimes, so I like to profile the scene with all my non-essential GameObjects disabled to see what we’re working with as a baseline.




<img src="https://lh6.googleusercontent.com/yiM2Xw0f40PLxetNofqUqfdKKM1LnILZMB0bzYO6kWeHUiMnJojsvYKJedx8zUSCOO70uIqZtNbcaXQnPmSTCIYaoRhlx4iuW5vg7q91Barh8107CX2JgPBnxYg_TUp5-vDYols" alt="">




Lot of vsync with the CPU, which is good (CPU and GPU taking &lt; 16ms which is my refresh rate) and then 10ms of <strong>Other</strong> on the GPU (damn!) which could be Unity Editor overhead, like rendering the profiler or something. Good to know.




Here’s a profile of the first initial version:<br>
<img src="https://lh4.googleusercontent.com/g_-u6GFJbWCFpSDmubg8USFcnjdc7EGNnQSfVeOPrt2Tt3rY9j-6q536QXBwKkNvSnRej9iSAlSzJsqT1WGeLpZuU6xVGQOSacQ_LCmn2lPl89IjxdKZNG8qETztW6juSoKReOs" alt="">



- 13ms for draw calls alone
- 3ms for the script update to make everything look at the camera
- 5ms for animation (not sure what that’s about)
- 9ms on GPU for rendering (not bad, but i have a 2080Ti)



Let’s see why rescaling is so slow:




<img src="https://lh3.googleusercontent.com/kE5GDxU-ghkmsyqvv8KoOVezfxiBdcawmxmj0Xg52QwxpwEGoEjxn3qIEjBblaOJ_s-93q-Efk1MLmVr1Wbe_yogeLn4lxivBsdnLeQZGi38ZpW_g6BmkSO1C5fwaZnRGg2WKDw" alt="">




Clear bump during frames where the Word Cloud is changing scale:



- Rendering / draw calls unchanged
- 17ms scripts (TextMeshPro)
- 7ms physics



Oh ya, by the way there are 10k batches and 100k triangles! That’s no good, looks like my TextMeshPros aren’t batching.


<h2><a id="First_Optimisation_71"></a>First Optimisation</h2>


At this point, I moved the project to “Single Pass” stereo for VR, since that should give me at least a 50% speedup, but the way it handles shaders had caused unexpected issues before. And there is still a bug in Unity’s postprocessing stack “Bloom” effect that doesn’t do a double wide buffer for the bloom downsample pass, which required me to just jump in and multiply the bloom buffer width by 2. I reported <a href="https://github.com/Unity-Technologies/PostProcessing/issues/497">this bug</a> about two years ago <code>¯\_(ツ)_/¯</code>




Next idea was to disable TextMeshPro renderers if they are beyond a certain distance from the camera. This will cut down on the rendering, and whatever scaling calculations that TextMeshPro is doing on scale change. Also manually disable TMP objects that are outside the camera frustrum. Definitely helps the GPU, but enabling/disabling gameobjects at runtime has a cost. I bet using ECS would have made this approach viable but I haven’t dug into that system quite yet and was on a deadline.




<img src="https://lh6.googleusercontent.com/MHNLhu5WoAl6wkq8KgACz3RuDRNxz6WjWOttwg9j0L6aZNK3qCjlfqEk_KT1mcmUxALUMD0-zfp2yF4KbXmiKShY66vqOiDnCvL_FZ-A1WBXHPRgEckAYAgeEb4julpzBDYCmAU" alt="">




Far away text is now rendered as a point (There’s a quad mesh on each point in addition to TMP). Every frame the distance to camera is calculated for every point, which controls if it is rendered (or disabled if out of view) Also here, you can see the words colored by part of speech.




<img src="https://lh6.googleusercontent.com/0yItKs-itN77WN06d1ld_5-iqNDgtP_9l9Xm8lV1sYBh7azzZ0U73Yccz90upYT6GD3l2cp7Gq7kJK5VAkLrPDDcO-ObuwuHEUYMrn4URJcdjld9iUhma7dBoXrnz_JmmSICjZY" alt="">




(SteamVR profile) Calculating all this stuff was really terrible for the CPU, even though the GPU was now happy (rendering less stuff, mostly points which batch!). I tried to batch Text Mesh Pro, but they explicitly disallow that in the shader <code>{DisableBatching = True }</code> and instance every material (not ideal). This also clogs up the CPU making 10k draw calls per frame.




So, we need to somehow:



- Not scale Text Mesh Pro (don’t want to change their source)
- Not move colliders
- Get the Text to batch, and use a single material
- Get the text to billboard in the shader

<h2><a id="Colliders_91"></a>Colliders</h2>


<img src="https://lh6.googleusercontent.com/iRStIxHN-WPqeklthLZ0tZ06zanvomLQYxN_gIv7TKktnhUPL9uCLLxmUA5dgiGzvrZ3Thpn1rX5Tq3dxogg4tw6Dd-jk2aT71MujMNRtd7B4UoPRC0tV8LGrFMNJGjjaEk-mEo" alt=""><br>
<em>Every word has a collider so that I can detect grab and laser-pointer select in VR.</em>




This one is pretty easy. Create the colliders, put them in another space and never move them! Then, manually raycast/spherecast every frame to calculate intersections. But, transform the controller position into the other space, and then do the raycast/spherecast in the other space. First off though, create a <code>Dictionary&lt;Collider, WordPoint&gt;</code> to map each of my proxy colliders to the words that they represent quickly.




More precisely, the hand (controller) is in the word cloud, compute its local position in the word cloud, and use that as the local position in the collider cloud.


<pre><code>var handInCloudSpace = WordCloudTransform.InverseTransformPoint(RightCursorTransform.position);
var handDirInCloudSpace = WordCloudTransform.InverseTransformDirection(RightCursorTransform.forward);
var handInColliderSpace = ColliderTransform.transform.TransformPoint(handInCloudSpace);
var handDirInColliderSpace = ColliderTransform.transform.TransformDirection(handDirInCloudSpace);
int numHits = Physics.RaycastNonAlloc(new Ray(handInColliderSpace, handDirInColliderSpace), raycastRightHand, 10f);
</code></pre>


Now I realize I need to bite the bullet and create a custom shader for the word cloud text if I wanted to get all my goals accomplished.


<h3><a id="Custom_Shaders_Rant_108"></a>Custom Shaders Rant</h3>


When I first started Unity dev, I wanted to make a custom shader for everything because it made me feel badass and I could do anything I wanted. But then I realized:



- custom shaders make it much harder for your coworkers to collaborate
- nothing batches if everything’s got a custom shader
- they are liable to break with updates to Unity or changes in your rendering pipeline



So now I usually think, if you can do it in Unity with the Standard shader, do that. But desperate times call for desperate measures…


<h2><a id="Custom_Shader_118"></a>Custom Shader</h2>


First thing was to just render a TextMeshPro mesh with my new shader and see what it looked like. But where do I get the mesh? TMP created the meshes and UVs them dynamically based on its texture atlas for the font you’ve selected, so there’s no actual mesh asset. No problem, I just rip the mesh out at runtime:


<pre><code>MyMeshfilter.mesh = SomeOtherTextMeshPro.meshFilter.mesh
</code></pre>


<img src="https://lh5.googleusercontent.com/bao79S1ab8nVg5aOiDh9kiKYSLlBVb_ymiqN2r5oVzT4HWozU4eC5RMq1sq_92LWrp08478uX_WQHCg30p6rLaDBreWaYDREE87t090ym-CJFqOx6mScJYanuBSU6IrsjH1GYYo" alt=""><br>
<em>TextMeshPro mesh rendered with a default custom unlit shader.</em>




So… why is it blocks? Our material doesn’t have a texture yet. Search “Atlas” in the project to find the same texture atlas the original mesh was using… and it kinda works.




<img src="https://lh6.googleusercontent.com/JFv65IoTAVemko1OyL-ZK3g5AiSBGQbVFZTXpG7tZuhB3lTa80MRIJlu_Ejxll5RsDi_KDJEr_GGFilhzJLMKtryjzdERrhMDRQoCec_abR93G1ddrxPN5ZPN6VxnCJymobdVhw" alt=""><br>
Why does it look like weird (it’s a distance field…)? Maybe I should have stuck with the text mesh pro shader after all? Yeah… let’s just copy paste <code>TextMeshPro/Mobile/Distance Field</code> into here… perfect. Now I can get into what I actually wanted to do, billboard the text. Some googling gives me this little gem: (shoutout to Github user Spongert) and <a href="https://en.wikibooks.org/wiki/Cg_Programming/Unity/Billboards">https://en.wikibooks.org/wiki/Cg_Programming/Unity/Billboards</a>


<pre><code>float4 vPosition = mul(UNITY_MATRIX_P, mul(UNITY_MATRIX_MV, float4(0.0, 0.0, 0.0, 1.0)) + float4(vert.x, vert.y, vert.z, vert.w));
</code></pre>


Which instead of transforming the vertex into clipspace, transforms the origin into viewspace. THEN it adds the vertex local position into that, and transforms into clipspace. This has the effect of keeping the mesh oriented to viewspace which is exactly what we want. The only problem is that if dynamic batching is enabled, you can’t assume that your vertices are <em>actually</em> in the local position of the object being rendered, because Unity will bake the gameobject transform into there. So we have to disable batching. Well damn, that’s not what I wanted.


<h2><a id="Batching_136"></a>Batching</h2>


If Unity’s not going to batch this and still keep the vertex in local space, then maybe it can be done manually. Take two text meshes at the origin and merge them. Then upload the position into the UV3 per-vertex data (TMP uses UV1 and UV2 for some reason). I also care about scale, so I’ll go ahead and pack that into the w component of UV3.




Then in the shader, the Model Matrix can be reconstructed per word, and the <code>input.vertex</code> vertices are still centered at the origin!


<pre><code>float3 uvPos = input.texcoord2.xyz;
float s = input.texcoord2.w
float4x4 Obj2World = float4x4(
    s, 0, 0, uvPos.x,
    0, s, 0, uvPos.y,
    0, 0, s, uvPos.z,
    0, 0, 0, 1);
</code></pre>


Rotation doesn’t matter because it is staying oriented toward view space (billboarding). So this is a simple affine transform with only scale and translation. The inverse has an easy closed-form solution.


<pre><code>float4x4 World2Obj = float4x4(
    1 / s, 0, 0, -uvPos.x / s,
    0, 1 / s, 0, -uvPos.y / s,
    0, 0, 1 / s, -uvPos.z / s,
    0, 0, 0, 1);
</code></pre>


So the vertex shader becomes (including the billboarding trick from above):


<pre><code>float4x4 custom_MV = mul(UNITY_MATRIX_V, Obj2World);
float4 vPosition = mul(UNITY_MATRIX_P, mul(custom_MV, float4(0, 0, 0, 1)) + vert * float4(scale, scale, 1, 1));
</code></pre>


What this does:


<ol>
- Create custom model matrix based on the UV data uploaded per vertex
- Transform 0,0,0 in the model space into view space
- Add the vertex position offset (times the scale)
- Project into clipspace
</ol>


The other thing I need to do is add color per word, so I just upload that to the pervertex color channel.




I do this for all 5000 words, and they merge into one mesh with 100,000 vertices. (Use integer index format to exceed the 64k vert limitation) so it’s one draw call now!




At this point, I am using no TextMeshPro scripts, not moving or scaling any colliders, and billboarding all the words in the shader. But I can’t move the word cloud, because we only have local position available. So, take the trackball transform and upload the <code>WorldToObject</code> and <code>ObjectToWorld</code> matrices as a uniform shader parameter <code>_WordCloudMatrix</code> and <code>_WordCloudMatrixInverse</code> to the material.




So the vertex shader is now:


<pre><code>float4x4 customObj2World = mul(_WordCloudMatrix, Obj2World);
float4x4 custom_MV = mul(UNITY_MATRIX_V, customObj2World);
float4 vPosition = mul(UNITY_MATRIX_P, mul(custom_MV, float4(0, 0, 0, 1)) + vert * float4(scale, scale, 1, 1));
</code></pre>
<h2><a id="Profile_183"></a>Profile</h2>


Now, I get exactly the same functionality with:



- One mesh
- One material
- One draw call
- One dynamic transform
- No dynamic colliders



Feeling good about this! Let’s check the profile.




<img src="https://lh5.googleusercontent.com/x4kItQP1jj__JZCd9Swzb5tJAI2HWAhg1wW9_QsaI5QShkbTIxxJBBKIEYznPX-QRg23aqN47Tq9Ptb4I3TDB51Aw2d0m7Wvzl3E3D0VKM7FfVmwtZqsP5kH0LGZkB7vbcGQdxM" alt="">




<em>Here’s my profiling test scene, using the new font from the client and the builtin postproc stack for the rest of their app. It’s got a good amount of text in view, and rendering pretty much the whole cloud.</em>




It doesn’t show up on the profile. I enable and disable the mesh, even rotate it and scale it around.




<img src="https://lh5.googleusercontent.com/sAEvDSpxg40cWeWTlLelQEV51GqWIsvfRwR45IZE9bwz4B0C2_cNpWk3qy9EGoRqbDg48rqmMkdHrU69En_qTFmWzL618jnXoodYq48ZCRNr_4JXO1E6pLQTPjmtRun4-SNCOuE" alt="">




Left side of profile is my “empty scene”, with the same random 10ms “other”. Then you can see the spike on rendering (bottom) when I enable the word cloud. No difference. Maybe I should Look at it in a build.




<img src="https://lh4.googleusercontent.com/TMBL2YWA4WLJZGKBH0tGvTmiLMW5wRRI0sIJ1YSJkexIshI4j6lS9K3Ay5hHGaxsVqgjvbXdKK5RKFQavb4Rmn7SvCPOf16tnVACRH-rbc6hhKdnwjCn1t5unZvW2prwfEsC-b0" alt="">




Ok so CPU is taking 1ms, that’s a good sign. But for some reason, i lost my GPU data in the build. Will have to look at why that happens later. Let’s check out the SteamVR profiler again.




<img src="https://lh5.googleusercontent.com/U3kvAIzofROOY-9GOeAN5kSQQArmDnUMHQxPwzIch_Ky36ogAc_fXHI_zEG1GawCkN7D-UNRAISJkOaVNU7XuTKNO4V5jLn6Tu8HUygi2Eq7a08HDwbWh4txPDvOrHK2syPh4E8" alt="">




Hot damn! I have my 5K text/points rendering, totally interactively at a constant 1ms cpu and GPU. (originally was 30ms CPU and 16-20ms GPU). Time for a beer.


<h3><a id="Point_Rendering_Transition_213"></a>Point Rendering Transition</h3>


I skipped the part where I render points when the word gets far enough away.




Basically there is a second mesh exactly like the first merged text mesh, except each word is a quad. Still upload the color and local position/scale into the pervertex data. The shader is really similar.




Then add some scaling logic in the shader… since we have the per-word scale and create the model matrix on the fly per word, this can be dynamic. So use the builtin Unity shader uniform <code>_WorldSpaceCameraPos</code> and then compute the word position in world space (that’s why I needed to compute the inverse matrix above)


<pre><code>float objSpaceDistance = length(mul(customWorld2Object, float4(_WorldSpaceCameraPos, 1)).xyz);
float scale = length(customObj2World._m00_m01_m02) * v.texcoord2.w;
scale = lerp(0, scale, smoothstep(_FadeOutNear, _FadeOutFar, objSpaceDistance));
</code></pre>


So there’s some more shader parameters, <code>_FadeOutNear</code> and <code>_FadeOutFar</code>, which control the fadeout-ness. Just invert the logic in the point shader vs the text mesh shader, so that the points fade in as the words fade out.




In theory, this could be all in the same original mesh with just a flag pervertex saying if it is part of the quad or the text. Or, make all the text character quads for each letter morph smoothly into a single point… but who has time for that.


<h3><a id="Selection_230"></a>Selection</h3>


Well, I still want to be able to select words, which is what I was doing earlier with the dumb version, but I was swapping materials to show if something was selected. That doesn’t work anymore because this is all one mesh. Luckily, I have a <strong>unique Identifier</strong> per word, which is its position in the cloud. So If I have detected a selection (using the collider setup and dictionary lookup above), then the position of the selected word is uploaded as another material property uniform.


<pre><code>bool selected = (length(_SelectedWordPos - uvPos.xyz) &lt; 0.01);
</code></pre>


Then something like:


<pre><code>scale *= lerp(1,2,selected);
color *= lerp(1,2,selected);
outlineWidth = lerp(0,1,selected);
</code></pre>


Or whatever else you feel like doing. And bam! Super interactive. No CPU logic!


<h2><a id="BONUS_SECTION_Timelines_249"></a>BONUS SECTION: Timelines</h2>


I also did some analysis of the word usage in the corpus over time.<br>
If you click a word, it will generate this view of the frequency of each word each year.




<img src="https://lh3.googleusercontent.com/i_Nrilpsf2GGK_2dlGYU9zXjJkNBWTHXzxhGX551wFB93YrQhN7tdp0tCAIr8KI9Vxldhi6HAm9AcxEuecBwz52Kf0I16yfCPBXz8px_jpFvnuFXQfgKirYd5bWG-g3znOkfsXU" alt=""><strong><img src="https://lh5.googleusercontent.com/hT6l81eO1rJ1KPJUUJ5FMHI6H68E27hWWfdFQ96cw5e284-_XpOiMhNgo-VO8vq5w_C0exNa-pDd-7W1Y-7latpefoNEAh_8_FktpA_NpljmEKG5U1VauBsKgpx_7CVkohpRbtU" alt=""></strong>


# interesting word cloud areas

{{<gallery rrl >}}
