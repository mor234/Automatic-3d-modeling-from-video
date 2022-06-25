
# Usage of code

This is an example of usage of the code on high qulity simulation video taken from:
 https://www.youtube.com/watch?v=FfCfxlllwtU&ab_channel=Helderhugo. 
 The video was downloaded and cut to be 3 minutes that showes the tower.
 ![tower_from_video](https://github.com/mor234/Automatic-3d-modeling-from-video/blob/a011fb347f7069ee44750ce8538e7d3608d3a221/images/video_tower.png)
 It was named "video1" and place in the same directory as the python code.
## Changes inside the main in the code: 
 - **number_of_frames_per_second** was assigned 2.5  
 - **create_point_clouds** was called as followes:     create_point_clouds(photo_amount ,images_dir_path="data",photos_per_cloud=70,overlap=40)

```python
if __name__ == "__main__":

    # constants
    address = os.path.dirname(os.path.realpath(__file__)) +"\\video1.MP4"
    cam = cv2.VideoCapture(address)

    # calculations
    fps = cam.get(cv2.CAP_PROP_FPS)
    frame_count = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
    duration, number_of_frames_per_second = frame_count/fps, 2.5
    myframerate = duration / (duration * number_of_frames_per_second)

    photo_amount = produce_images_from_video( myframerate, 0, cam,"data")
    create_point_clouds(photo_amount ,images_dir_path="data",photos_per_cloud=70,overlap=40)
```
For more options to adjust the create point clouds: https://docs.opendronemap.org/sw/arguments/ 
## Run code
 - Compile cyhton code :python setup.py build_ext --inplace
 - Open docker, and run docker run -ti -p 3000:3000 --gpus all opendronemap/nodeodm:gpu on cmd
 - Run code

## Download subclouds results
Open http://localhost:3000/ on your broweser and download "all assets", for each sub cloud.
![localhost](https://github.com/mor234/Automatic-3d-modeling-from-video/blob/1ec771404b6617cf6a5abacb84825bb41fbc8ca5/images/loacl_host_view.png)

From each results directory, take the point cloud from the **odm_georeferencing** directory
You can see the reaulting sub clouds in the directory "sub clouds towers example" 
![subcloud](https://github.com/mor234/Automatic-3d-modeling-from-video/blob/286345a700e227e493235b2c285d8ce69acfbf05/images/sub_cloud_example.png)

## Merge points clouds
Open the points clouds on cloud compare and combine them.
One useful operation is multiply scale (so the points cloud you are combining will be in the same size):
![multiply scale](https://github.com/mor234/Automatic-3d-modeling-from-video/blob/a011fb347f7069ee44750ce8538e7d3608d3a221/images/multiply_scale.png)
For the rest, you can use the following tuturial: https://www.youtube.com/watch?v=8lxFsXgXdTY&t=204s
![combined cloud](https://github.com/mor234/Automatic-3d-modeling-from-video/blob/5a19465a0f2175c9b7b713d76a47043a756a55ce/images/combined_tower_point_cloud.png)
## Create 3d model for unity
Follow instructions from main readme: https://github.com/mor234/Automatic-3d-modeling-from-video/blob/main/README.md
