Project description：
This project is the final project of a Master's degree student, entitled Human-Robot collaboration. The goal is to use Kinect to collect information about the human skeleton, and after a series of coordinate conversions and angle calculations, use python code to map the corresponding arm joint angles to Baxter in CoppeliaSim, so that Baxter can replicate the human movement and implement the stacking task. Before implementing the stacking task, first check that all the code is written and the scene is set up correctly, and run the code to check that Baxter's movements are consistent with human movements before adding the suction cups, table and small blocks.

Description of the individual files：
The .ttt file in the coppeliaSim folder is the coppeliaSim scenario, the main_1.py file in the python folder is the python main function where the communication is established and the data is transferred. process_data_1.py is a wrapped file where all the coordinate conversions and The baxter_move_position.txt file is the human skeletal position data collected using Kinect. The remaining three files are auxiliary packages that can be imported at runtime.

For more information on how to run this project:
First download the .ttt file, import it into coppeliaSim and click on Run. The baxter will not make any movements at this point as it is controlled by python. Afterwards, download all the files from the python folder to a directory of the same level and run main__1.py with vs code to drive the baxter in coppeliaSim.

For human action information you need to click on the link to download the video.
The code testing vedio:(without suction cup)
https://user-images.githubusercontent.com/80648551/133005218-03cc5b2e-1167-4f4d-908b-8fd9e29a3164.mp4


https://user-images.githubusercontent.com/80648551/133005226-fc66d601-a8e6-4798-aec9-fc8f71fa210b.mp4

The stacking task:
As this part of the video file is too large, they have been split into two parts and only the key parts have been cut.
https://user-images.githubusercontent.com/80648551/133004536-ae641c4e-5bdc-4cbf-9bf5-02c9b1877167.mov


https://user-images.githubusercontent.com/80648551/133004542-e98a0e00-c838-4b91-8eee-75067b555836.mov


https://user-images.githubusercontent.com/80648551/133004550-836c561b-ba70-40aa-868f-27e809b90398.mov
