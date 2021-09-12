import numpy as np
import os
import math



def load_data(path='./position_7.txt'):
    lines = []
    l_s = []
    l_e = []
    l_h = []

    r_s = []
    r_e = []
    r_h = []
    with open(path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip().rsplit(',', 1)[0].strip().replace(' ', '').split(',')[1:]  # split the data
        if line[1].lstrip('-').isdigit():
            line = [float(n)/1000.0 for n in line]  # divide each data by 1000, the calculation angle will not be affected
            temp = np.array(line)< -2147483640  # removal of redundant data
            temp = temp.sum()  # calculate the number of true, that is, the number with infinity
            if temp > 0:
                continue
            l_h.append(line[0:3])  # extraction of data
            l_e.append(line[3:6])
            l_s.append(line[6:9])
            r_h.append(line[9: 12])
            r_e.append(line[12:15])
            r_s.append(line[15:18])  
        else:
            pass  

    return np.array(l_s), np.array(l_e), np.array(l_h), np.array(r_s), np.array(r_e), np.array(r_h)


def cal_theta(v1, v2):
    eps = 1e-9
    dis_es = np.sqrt((v1*v1).sum(1))  # request for mould length
    dis_eh = np.sqrt((v2*v2).sum(1))
    theta = (v1*v2).sum(1) / ((dis_es*dis_eh)+eps)
    return theta  # sin theta


def get_theta(s, e, h): 
    T1 = np.array([[0,0,-1],
                   [0,1,0],
                   [1,0,0]])
    T2 = np.array([[1,0,0],
                   [0,0,1],
                   [0,-1,0]])     
    s = np.dot(T1, s.T)
    s = np.dot(T2, s).T
    e = np.dot(T1, e.T)
    e = np.dot(T2, e).T
    h = np.dot(T1, h.T)  
    h = np.dot(T2, h).T        
    eps = 1e-9
    l_es = s - e
    l_eh = h - e

    n = np.array([[1, 0, 0]])
    n = np.repeat(n, l_es.shape[0], axis=0)  # s vector
    theta1 = cal_theta(n, l_es)  # sin(x)
    theta1 = np.arcsin(theta1)*180/math.pi

    n = np.array([[0, 0, 1]])
    n = np.repeat(n, l_es.shape[0], axis=0)  # s vector
    theta2 = cal_theta(n, l_es)  # sin(x)    
    theta2 = np.arcsin(theta2)*180/math.pi

    n = np.ones([l_es.shape[0],3])
    n[:,1] *= -((e[:,0]-s[:,0])/(eps+e[:,1]-s[:,1]))
    n[:,-1] *= 0
    theta3 = cal_theta(l_eh, n)  # sin(x)
    theta3 = np.arcsin(theta3)*180/math.pi


    theta4 = cal_theta(l_es, l_eh)  # cos(x)
    theta4 = np.arccos(theta4)*180/math.pi

    return theta1, theta2, theta3, theta4

if __name__ == '__main__':
    l_s, l_e, l_h, r_s, r_e, r_h = load_data()
    l_t1, l_t2, l_t3, l_t4 = get_theta(l_s, l_e, l_h)
    r_t1, r_t2, r_t3, r_t4 = get_theta(r_s, r_e, r_h)
