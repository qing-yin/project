import sim
import time
import math
from process_data__1 import load_data, get_theta
import keyboard as kb

def load_data1(txt):
    r, l = [], []
    with open(txt, 'r') as f:
        lines = f.readlines()
        lines = lines[1:]
        for i, line in enumerate(lines):
            line = line.strip().split('\t')
            r.append(180-float(line[-1]))
            l.append(180-float(line[-2]))
    return r, l


data_path = './baxter_move_position.txt'


print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim

assert clientID != -1
print ('Connected to remote API server')

# Now try to retrieve data in a blocking fashion (i.e. a service call):
res,objs=sim.simxGetObjects(clientID,sim.sim_handle_all,sim.simx_opmode_blocking)
if res==sim.simx_return_ok:
    print ('Number of objects in the scene: ',len(objs))
else:
    print ('Remote API function call returned with error code: ',res)


l_joints = []
r_joints = []
for i in range(1, 5):
    ret, handle1 = sim.simxGetObjectHandle(clientID, 'Baxter_leftArm_joint%s'%(str(i)),sim.simx_opmode_blocking)
    assert ret!=-1
    l_joints.append(handle1)    
    ret, handle2 = sim.simxGetObjectHandle(clientID, 'Baxter_rightArm_joint%s'%(str(i)),sim.simx_opmode_blocking)
    assert ret!=-1    
    r_joints.append(handle2)

l_s, l_e, l_h, r_s, r_e, r_h = load_data(path=data_path)
l_t1, l_t2, l_t3, l_t4 = get_theta(r_s, r_e, r_h)
r_t1, r_t2, r_t3, r_t4 = get_theta(l_s, l_e, l_h)

sim.simxSetJointTargetPosition(clientID, l_joints[0], 1*math.pi/180., sim.simx_opmode_oneshot)
sim.simxSetJointTargetPosition(clientID, l_joints[1], 1*math.pi/180., sim.simx_opmode_oneshot)
sim.simxSetJointTargetPosition(clientID, l_joints[2], 180*math.pi/180., sim.simx_opmode_oneshot)
sim.simxSetJointTargetPosition(clientID, l_joints[3], 1*math.pi/180., sim.simx_opmode_oneshot)
sim.simxSetJointTargetPosition(clientID, r_joints[0], 1*math.pi/180., sim.simx_opmode_oneshot)
sim.simxSetJointTargetPosition(clientID, r_joints[1], 1*math.pi/180., sim.simx_opmode_oneshot)
sim.simxSetJointTargetPosition(clientID, r_joints[2], 180*math.pi/180., sim.simx_opmode_oneshot)
sim.simxSetJointTargetPosition(clientID, r_joints[3], 1*math.pi/180., sim.simx_opmode_blocking)
time.sleep(3)

for i in range(2):

    for l_tt1, l_tt2, l_tt3, l_tt4, r_tt1, r_tt2, r_tt3,r_tt4 in zip(l_t1, l_t2, l_t3, l_t4, r_t1, r_t2, r_t3, r_t4):
        sim.simxPauseCommunication(clientID, True)
        sim.simxSetJointTargetPosition(clientID, l_joints[0], (l_tt1+2)*math.pi/180., sim.simx_opmode_oneshot)
        sim.simxSetJointTargetPosition(clientID, l_joints[1], (l_tt2)*math.pi/180., sim.simx_opmode_oneshot)
        sim.simxSetJointTargetPosition(clientID, l_joints[2], (l_tt3+175)*math.pi/180., sim.simx_opmode_oneshot)
        sim.simxSetJointTargetPosition(clientID, l_joints[3], min(150,180-l_tt4)*math.pi/180., sim.simx_opmode_oneshot)
        sim.simxSetJointTargetPosition(clientID, r_joints[0], (-(r_tt1+2))*math.pi/180., sim.simx_opmode_oneshot)
        sim.simxSetJointTargetPosition(clientID, r_joints[1], (r_tt2)*math.pi/180., sim.simx_opmode_oneshot)
        sim.simxSetJointTargetPosition(clientID, r_joints[2], (-r_tt3+175)*math.pi/180., sim.simx_opmode_oneshot)
        sim.simxSetJointTargetPosition(clientID, r_joints[3], (175-r_tt4)*math.pi/180., sim.simx_opmode_oneshot)
        sim.simxPauseCommunication(clientID, False)
        time.sleep(0.02)

    sim.simxSetJointTargetPosition(clientID, l_joints[0], 1*math.pi/180., sim.simx_opmode_oneshot)
    sim.simxSetJointTargetPosition(clientID, l_joints[1], 1*math.pi/180., sim.simx_opmode_oneshot)
    sim.simxSetJointTargetPosition(clientID, l_joints[2], 1*math.pi/180., sim.simx_opmode_oneshot)
    sim.simxSetJointTargetPosition(clientID, l_joints[3], 1*math.pi/180., sim.simx_opmode_oneshot)
    sim.simxSetJointTargetPosition(clientID, r_joints[0], 1*math.pi/180., sim.simx_opmode_oneshot)
    sim.simxSetJointTargetPosition(clientID, r_joints[1], 1*math.pi/180., sim.simx_opmode_oneshot)
    sim.simxSetJointTargetPosition(clientID, r_joints[2], 1*math.pi/180., sim.simx_opmode_oneshot)
    sim.simxSetJointTargetPosition(clientID, r_joints[3], 1*math.pi/180., sim.simx_opmode_blocking)
    time.sleep(2)

#============================================================================

