import cv2
from pyodm import Node, exceptions
import os
import sys
import extract_photos_Cython as cython

# read instructions.
# to run docker (with all gpus): docker run -ti -p 3000:3000 --gpus all opendronemap/nodeodm:gpu
# to run docker : docker run -ti -p 3000:3000 opendronemap/nodeodm
# to compile cyhton code :python setup.py build_ext --inplace
# pip install openCV-python 

sys.path.append('..')

def produce_images_from_video( frameRate:float, count:int, cam,image_dir_name:str="data"):
    """
        The function produces frame from video according to given parmeters. 
        :param frameRate: how many times between frames, in seconds 
        :param count: counting frames, which to start from.
        :param cam:  cv2 object of the video
        :param image_dir_name: name to call the directory of frame, default is "data"
        :return count: amount of frames created from video       
    """
    try:
        if not os.path.exists(image_dir_name):
            os.makedirs(image_dir_name)
    except OSError:
        print ('Error: Creating directory of '+image_dir_name)

    sec = 0
    success = cython.getFrame(sec, cam, count,image_dir_name) 
    while success: 
        count += 1
        sec = sec + frameRate 
        sec = round(sec, 2) 
        success = cython.getFrame(sec, cam, count,image_dir_name) 

    cam.release()
    cv2.destroyAllWindows()
    return count-1

def create_point_clouds(photo_amount,photos_per_cloud:int=50,overlap:int=20,images_dir_path:str="data",run_once=False):
    """
        The function generates small point clouds from all the photos. each point cloud is generated from photos_per_cloud images,
        keeping the overlap images to be used when genrating the next point cloud
        :param frameRate: how many times between frames, in seconds 
        :param count: counting frames, which to start from.
        :param cam:  cv2 object of the video
        :param image_dir_name: name to call the directory of frame, default is "data"
        :return count: amount of frames created from video       
    """
    ### type check
    photos_per_cloud=int(photos_per_cloud)
    overlap=int(overlap)
    if (photos_per_cloud<=0) :
        raise "numbers of photos must be positive"
    if (overlap>=photos_per_cloud):
        raise "number of overlap photos must be smaller than numbers of photos per cloud"
    if(photo_amount<photos_per_cloud):
        photos_per_cloud=photo_amount
        overlap=0

    counter=0
    list_img = []
    img_to_jump=photos_per_cloud-overlap
    # # create client for odm api
    node = Node("localhost", 3000)
    #initial assignment off first  photos_per_cloud images
    for index in range(counter, photos_per_cloud):#create first_list
            list_img.append(str(images_dir_path)+"/frame"+str(index)+".jpg")


    last_round=False
    loop_index=0 #keep the number of the sub cloud
    while (True):
        create_point_cloud_from_range_odm(list_img,node)
        if(last_round): #end loop
            break
        index_to_remove_from=0
        # update frames for next cloud, witn overlap
        for i,path in enumerate(list_img):
            split_path=path.split("/")
            frame_number=int(split_path[-1].replace("frame","").replace(".jpg",""))
            split_path[-1]="frame"+str(frame_number+img_to_jump)+".jpg"
            list_img[i]='/'.join(split_path)
            if((frame_number+img_to_jump)==photo_amount):#no more photos
                last_round=True
                index_to_remove_from = i
                break
        #in last round remove extra frames.
        if (last_round):
            for _ in range(0,photos_per_cloud-index_to_remove_from):
                list_img.pop(index_to_remove_from)
        loop_index+=1




      
def create_point_cloud_from_range_odm(list_img,node):
    """
        The function create point cloud from given images. 
        :param list_img: list of images paths, relative to current directory
        :param node: a client to interact with NodeODM API.
         
    """
    try:
        # Start a task
        print("Uploading images...")
        # if use higher quality images: 
        #task = node.create_task(list_img,  {'feature-quality':'low','mesh-octree-depth':8,'pc-las':True,'pc-quality':'low','end-with':'mvs_texturing' })
        task = node.create_task(list_img,  {'mesh-octree-depth':8,'end-with':'mvs_texturing' })
        print(task.info())
        try:
            # This will block until the task is finished
            # or will raise an exception
            task.wait_for_completion()
            print("Task completed, download results from http://localhost:3000/")
            
        except exceptions.TaskFailedError as e:
            print("\n".join(task.output()))
    except exceptions.NodeConnectionError as e:
        print("Cannot connect: %s" % e)
    except exceptions.NodeResponseError as e:
        print("Error: %s" % e)

if __name__ == "__main__":

    # constants
    address = os.path.dirname(os.path.realpath(__file__)) +"\\video1.MP4"
    cam = cv2.VideoCapture(address)

    # calculations
    fps = cam.get(cv2.CAP_PROP_FPS)
    frame_count = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
    duration, number_of_frames_per_second = frame_count/fps, 25
    myframerate = duration / (duration * number_of_frames_per_second)

    photo_amount = produce_images_from_video( myframerate, 0, cam,"data")
    create_point_clouds(photo_amount ,images_dir_path="data")
