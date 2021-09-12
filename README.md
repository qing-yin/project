Project description：
This project is the final project of a Master's degree student, entitled Human-Robot collaboration. The goal is to use Kinect to collect information about the human skeleton, and after a series of coordinate conversions and angle calculations, use python code to map the corresponding arm joint angles to Baxter in CoppeliaSim, so that Baxter can replicate the human movement and implement the stacking task. Before implementing the stacking task, first check that all the code is written and the scene is set up correctly, and run the code to check that Baxter's movements are consistent with human movements before adding the suction cups, table and small blocks.

Description of the individual files：
The .ttt file in the coppeliaSim folder is the coppeliaSim scenario, the main_1.py file in the python folder is the python main function where the communication is established and the data is transferred. process_data_1.py is a wrapped file where all the coordinate conversions and The baxter_move_position.txt file is the human skeletal position data collected using Kinect. The remaining three files are auxiliary packages that can be imported at runtime.

For more information on how to run this project:
First download the .ttt file, import it into coppeliaSim and click on Run. The baxter will not make any movements at this point as it is controlled by python. Afterwards, download all the files from the python folder to a directory of the same level and run main__1.py with vs code to drive the baxter in coppeliaSim.

For human action information you need to click on the link to download the video.
The code testing vedio:(without suction cup)
https://user-images.githubusercontent.com/80648551/133003935-24c03b4a-d763-4350-bcc6-675e671690cc.mov

https://user-images.githubusercontent.com/80648551/133004480-8214c863-8c32-4cfe-ba8d-d9646f780cec.mov

The stacking task:
As this part of the video file is too large, they have been split into two parts and only the key parts have been cut.
https://user-images.githubusercontent.com/80648551/133004097-a74a5776-0047-420b-904d-5b5491251cc9.mov


https://user-images.githubusercontent.com/80648551/133004108-ca702382-c4ec-48b9-8f05-173b30b0a583.mov


https://user-images.githubusercontent.com/80648551/133004116-1888574d-6ecb-47ff-bfe6-3b017b567192.mov
