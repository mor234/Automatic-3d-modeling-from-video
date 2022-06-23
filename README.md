![image](https://user-images.githubusercontent.com/74238558/175327504-c6d78025-fd1e-4e3c-9bb6-fe9a95724ef6.png)

# Automatic 3d modeling from video

#### project goals. 
this is our final project for Automumos-vihicels, the project is divided into several parts :
1. automation of photogrametry using ODM.<br/>
  1.1. in this phase we use pyodm (python library) and Cython (convert pyhton code to C code)
  1.2. IMPORTAT - go to the file extract_photos_from_video.py and use the commands in comment to run the code.<br/>
        run with: docker run -ti -p 3000:3000 opendronemap/nodeodm.<br/>
        python setup.py build_ext --inplace.<br/>
3. using cloud compare to analyze and export 3d MESH
4. importing said MESH into unity and playing the game.

#### instructions.
1. clone this repository.
2. put a video file, from your drone in the folder you have just created, name it vedio1.mp4.
3. donwload and install docker desktop (for ODM to analyze images)
4. donwload and install cloud-compare.
5. run the following command to run docker image in cmd - "docker run -ti -p 3000:3000 --gpus all opendronemap/nodeodm:gpu" - this may take a while
6. you can go to https://localhost:3000 to see the task.<br />><img src="https://github.com/mor234/Unity-point-cloud/blob/main/images/task.png"/><br />
7. run - extract_photos_from_video.py. -this should take a while.
  6.1. this code will run thorugh the video and:<br />
        A. a folder named data will be created.<br />
        B. each frame (as defulat there will be 25 frames per second), will be created as a new image in the data folder.<br />
        C. ODM will work on the array of images.<br />
          C.1. the defualt overlap of images is 20 , meaning first 0-50 images, then 30-80 and so forth.<br />
7. once finished with all of the images, open http://localhost:3000/ on your broweser. download all the assets created. a .laz file will be created for each sub point cloud. take that and drag it into cloud compare. align and combine the clouds.<br />
<img src="https://github.com/mor234/Unity-point-cloud/blob/main/images/cc1.png"/><br />
8. click on the .las file similar to the above image. (notice the yellow border) <br />
9. now we need to normilize the points, go to Edit->Normals->compute - this sould take a while. (this will compute minimun spaning tree over the point cloud)<br />
<img src="https://github.com/mor234/Unity-point-cloud/blob/main/images/cc2.png"/><br />
<img src="https://github.com/mor234/Unity-point-cloud/blob/main/images/cc2-1.png"/><br />
10. now go to Plugins->PossionRecon.<br />
<img src="https://github.com/mor234/Unity-point-cloud/blob/main/images/cc3.png"/><br />
11. now the value of Octreedepht will determine how accurate the sofware will make the 3d mesh, 10- is viable, 14 is very sharp 3dmesh but will be heavy in performace. - this shold take a while!<br />
<img src="https://github.com/mor234/Unity-point-cloud/blob/main/images/cc3-1.png"/><br />
12. now we can see in the heat map, that blue areas are places with few dots, and red are places with a lot of dots, you can slide  the bar to the irght same as in <br />
    the image below to use only places with big concetrations of dots. (see that the bar starts from the middle?)<br />
<img src="https://github.com/mor234/Unity-point-cloud/blob/main/images/cc4.png"/><br />
13. now save the file as FBX BINARY and import in to unity!

### For Future Work:
- Number of frame per second taken from video can be adjasted.
- Allow lens repair (for a Go-Pro video for example), to create better quality photogrammetry.




### Unity : 
In this video we want to show the  result that we got, the connection between the points cloud to the  Unity game.
We want to show that the unity game base on the points cloud.
Where was a tree in the points cloud we creates tree object just to make it look good and comfortable.

![](https://github.com/mor234/Automatic-3d-modeling-from-video/blob/main/Gifs/ezgif.com-gif-maker%20(1).gif)
