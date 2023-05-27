# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 20:59:06 2020

@author: Ashiqrahman
"""

import numpy as np
import matplotlib.pyplot as plt
import math

%matplotlib qt

const = math.pi/180

p = np.array([[0],
              [0],
              [500],
              [1]])

theta = 0 *const #angle wrt x
psi   = 0 *const  #angle wrt y
phi   = 0 *const  #angle wrt z 

a,b,s = [0,0,0],[0,0,0],[0,0,0]

np.set_printoptions(formatter={'float_kind':'{:f}'.format})


R = 100    #distance of vertex in base
r = 30     #distance of vertex in end effector

#elements of roational matrices
r11 = math.cos(phi)*math.cos(theta)
r12 = math.cos(phi)*math.sin(theta)*math.sin(psi)-math.sin(phi)*math.cos(psi)
r13 = math.cos(phi)*math.sin(theta)*math.cos(psi)+math.sin(phi)*math.sin(psi)

r21 = math.sin(phi)*math.cos(theta)
r22 = math.sin(phi)*math.sin(theta)*math.sin(psi)+math.cos(phi)*math.cos(psi)
r23 = math.sin(phi)*math.sin(theta)*math.cos(psi)-math.cos(phi)*math.sin(psi)

r31 = -math.sin(theta)
r32 = math.cos(theta)*math.sin(psi)
r33 = math.cos(theta)*math.cos(psi)

#The transformation matrix
T = np.array([[r11,r12,r13,p[0]],
              [r21,r22,r23,p[1]],
              [r31,r32,r33,p[2]],
              [0  ,0  ,0  ,1  ]])

a[0]= np.array([[R*math.cos(30*const)],
               [-R*math.sin(30*const)],
               [0],
               [1]])

a[1]= np.array([[-R*math.cos(30*const)],
               [-R*math.sin(30*const)],
               [0],
               [1]])

a[2]= np.array([[0],
               [R],
               [0],
               [1]])

b[0]= np.array([[r*math.cos(30*const)],
               [-r*math.sin(30*const)],
               [0],
               [1]])

b[1]= np.array([[-r*math.cos(30*const)],
               [-r*math.sin(30*const)],
               [0],
               [1]])

b[2]= np.array([[0],
               [r],
               [0],
               [1]])
Rt = 0
ans = []
s_ = [0,0,0]
r_ans = []

#inverse kinematics part
for i in range(3):
    s[i] = np.dot(T,b[i]) 
    s_[i] = s[i] - a[i]
    #ans.append(math.sqrt(np.square(s[i][0])+np.square(s[i][1])+np.square(s[i][2])))
    r_ans.append(math.sqrt(np.square(s_[i][0])+np.square(s_[i][1])+np.square(s_[i][2])))    
    # print(math.sqrt(np.square(b[i][0])+np.square(b[i][1])+np.square(b[i][2])))
    # print(np.dot(T,b[i]))
    # print(a[i])
activate = 0

#constraint for parallel manipulator
for i in range(3):
    if r_ans[i] > 650 or r_ans[i]<400: #length constraint
        print("configuration not possible please try again")
        activate = 0
        break
    else:
        activate = 1
        
#for plotting
if activate == 1:        
    fig = plt.figure(figsize = (9,9))
    axs = fig.add_subplot(111, projection='3d')
    
    #axs.plot([Rt[0][0],Rt[1][0],Rt[2][0]],[Rt[0][1],Rt[1][1],Rt[2][1]],[Rt[0][2],Rt[1][2],Rt[2][2]])
    
    axs.plot([0,a[0][0],a[1][0],s[1][0],s[2][0]],
             [0,a[0][1],a[1][1],s[1][1],s[2][1]],
             [0,a[0][2],a[1][2],s[1][2],s[2][2]],linewidth = 5)
    
    axs.plot([0,a[1][0],a[2][0],s[2][0],s[0][0]],
             [0,a[1][1],a[2][1],s[2][1],s[0][1]],
             [0,a[1][2],a[2][2],s[2][2],s[0][2]],linewidth = 5)
    
    axs.plot([0,a[2][0],a[0][0],s[0][0],s[1][0]],
             [0,a[2][1],a[0][1],s[0][1],s[1][1]],
             [0,a[2][2],a[0][2],s[0][2],s[1][2]],linewidth = 5)

    
    #axs.axes.set_xlim3d(left=-10, right=10) 
    #axs.axes.set_ylim3d(bottom=-10, top=10) 
    #axs.axes.set_zlim3d(bottom=0, top=0)     
    
    axs.set_xlabel('X axis')
    axs.set_ylabel('Y axis')
    axs.set_zlabel('Z axis')
    
    plt.show()
    plt.draw()

    #print("b",p+np.dot(Rt,b[0])-a[0])
    #print("s",s[0])
    #print("a",a[0])
    ##print(s[2])
#print(ans)    
#print(math.sqrt(np.square(a[0][0]-s[0][0])+np.square(a[0][1]-s[0][1])+np.square(a[0][2]-s[0][2])))
#print(math.sqrt(np.square(a[1][0]-s[1][0])+np.square(a[1][1]-s[1][1])+np.square(a[1][2]-s[1][2])))
#print(math.sqrt(np.square(a[2][0]-s[2][0])+np.square(a[2][1]-s[2][1])+np.square(a[2][2]-s[2][2])))
    print(r_ans)



