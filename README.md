# Unity-point-cloud and photogrametry using ODM

#### project goals. 
this is our final project for Automumos-vihicels, the project is divided into two parts :
1. automation of photogrametry using ODM.
2. using cloud compare to analyze and export 3d MESH
3. importing said MESH into unity and playing the game.

#### instructions.
1. clone this repository.
2. put a video file, from your drone in the folder you have just created, name it vedio1.mp4.
3. donwload and install docker desktop (for ODM to analyze images)
4. donwload and install cloud-compare.
5. run the following command to run docker image in cmd - "docker run -ti -p 3000:3000 opendronemap/nodeodm" - this may take a while
6. run - extract_photos_from_video.py. -this should take a while.
  6.1. this code will run thorugh the video and:
        A. a folder named data will be created.
        B. each frame (as defulat there will be 25 frames per second), will be created as a new image in the data folder.
        C. ODM will work on the array of images.
          C.1. the defualt overlap of images is 30 , meaning first 0-50 images, then 30-80 and so forth.
7. once finished with all of the images,a .las file will be created in a folder name "results", take that and drag it into cloud compare.
<img src="https://github.com/mor234/Unity-point-cloud/blob/main/images/cc1.png"/>
8. click on the .las file similar to the above image. (notice the yellow border) 
9. now we need to normilize the points, go to Edit->Normals->compute - this sould take a while. (this will compute minimun spaning tree over the point cloud)
insert image 2
insert image 2-1
10. now go to Plugins->PossionRecon .
insert image 3
11. now the value of Octreedepht will determine how accurate the sofware will make the 3d mesh, 10- is viable, 14 is very sharp 3dmesh but will be heavy in performace. - this shold take a while!
insert image 3-1
12. now we can see in the heat map, that blue areas are places with few dots, and red are places with a lot of dots, you can slide  the bar to the irght same as in 
    the image below to use only places with big concetrations of dots. (see that the bar starts from the middle?)
insert image 4
13. now save the file as FBX BINARY and import in to unity!
