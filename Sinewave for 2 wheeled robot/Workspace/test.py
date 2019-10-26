import vrep
import time
import math

def pid_yaw(base_speed,yaw_angle):
    kp = 0.5
    prop = kp*yaw_angle
    motor_control(base_speed-prop,base_speed+prop)

def motor_control(left_speed,right_speed):
    returnCode=vrep.simxSetJointTargetVelocity(clientID,leftmotor,left_speed,vrep.simx_opmode_streaming)
    returnCode=vrep.simxSetJointTargetVelocity(clientID,rightmotor,right_speed,vrep.simx_opmode_streaming)

def yaw_angle():
    orientation_val = vrep.simxGetObjectOrientation(clientID,leftmotor,floor,vrep.simx_opmode_continuous)
    return orientation_val[1][1]*180/math.pi

prev_sec = time.time()
vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP
if clientID!=-1:
    print ('Connected to remote API server')
else:
    print('Failed connecting to remote API server')

returnCode = vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot)

returnCode,leftmotor = vrep.simxGetObjectHandle(clientID,'DynamicLeftJoint',vrep.simx_opmode_blocking)
returnCode,rightmotor = vrep.simxGetObjectHandle(clientID,'DynamicRightJoint',vrep.simx_opmode_blocking)
returnCode,robot_handle = vrep.simxGetObjectHandle(clientID,'LineTracer',vrep.simx_opmode_blocking)
returnCode,leftsensor = vrep.simxGetObjectHandle(clientID,'LeftSensor',vrep.simx_opmode_blocking)
returnCode,midsensor = vrep.simxGetObjectHandle(clientID,'MiddleSensor',vrep.simx_opmode_blocking)
returnCode,rightsensor = vrep.simxGetObjectHandle(clientID,'RightSensor',vrep.simx_opmode_blocking)
returnCode,floor = vrep.simxGetObjectHandle(clientID,'DefaultFloor',vrep.simx_opmode_blocking) 

left_sensor1 = 0
mid_sensor1 = 0
right_sensor1 = 0
left_sensor1 = vrep.simxReadVisionSensor(clientID, leftsensor, vrep.simx_opmode_streaming)
mid_sensor1 = vrep.simxReadVisionSensor(clientID, midsensor, vrep.simx_opmode_streaming)
right_sensor1 = vrep.simxReadVisionSensor(clientID, rightsensor, vrep.simx_opmode_streaming)
time.sleep(5)
odometer_val = vrep.simxGetObjectPosition(clientID,leftmotor,floor,vrep.simx_opmode_continuous)
    

returnCode=vrep.simxSetJointTargetVelocity(clientID,leftmotor,31.416/4,vrep.simx_opmode_streaming)
returnCode=vrep.simxSetJointTargetVelocity(clientID,rightmotor,31.416/4,vrep.simx_opmode_streaming)

odometer_val = vrep.simxGetObjectPosition(clientID,leftmotor,floor,vrep.simx_opmode_continuous)
count=0
prev_sec = time.time()
prev_yaw = yaw_angle()
def sin_wave():
    target_yaw1 = 0
    global prev_sec
    odometer_val = vrep.simxGetObjectPosition(clientID,leftmotor,floor,vrep.simx_opmode_continuous)
    curr_sec = time.time()
    y = 0.5*math.sin(12.566*odometer_val[1][0] - (curr_sec-prev_sec)*math.pi*0.001*2)
    # print(y)
    if y == 0:
        y = y+0.001
    tan_angle = ((math.pi/2)*y/0.5)
    main_angle = math.cos(tan_angle)
    if(main_angle <= 1 and main_angle >= 0):
        targ = math.atan(main_angle)*180/math.pi
        targ = targ
        if(count%1000 == 0):
            print(targ)
        # print(odometer_val[1][0])
        # targ = map_yaw()
        
            # print(target_yaw)
        # prev_sec = curr_sec
        curr_yaw = yaw_angle()
        error = curr_yaw-targ
        pid_yaw(10,error)

# def map_yaw():
#     curr = yaw_angle()
#     curr = curr - 90
#     if(curr>=-90 and curr<=0):
#         target_yaw = (curr+90)/2
#     if(curr>0 and curr<=90):
#         target_yaw = (90-curr)/2
#     return target_yaw

count = 0
for i in range(50):
    odometer_val = vrep.simxGetObjectPosition(clientID,leftmotor,floor,vrep.simx_opmode_continuous)

while True:
    count += 1
    # motor_control(10,10)
    # curr_yaw = yaw_angle()
    # error = curr_yaw-88.17
    # # pid_yaw(10,error)
    sin_wave()
    if count>1000000:
        break

# target_yaw = 45
count = 0
# while True:
#     count += 1
#     motor_control(10,10)
#     curr_yaw = yaw_angle()
#     error = curr_yaw-target_yaw
#     pid_yaw(10,error)
#     if count>1000000:
#         break

# for i in range(20):
#     odometer_val = vrep.simxGetObjectPosition(clientID,leftmotor,floor,vrep.simx_opmode_continuous)
#     orientation_val = vrep.simxGetObjectOrientation(clientID,leftmotor,floor,vrep.simx_opmode_continuous)
#     disp_val = math.sqrt(odometer_val[1][0]*odometer_val[1][0] + odometer_val[1][1]*odometer_val[1][1])
#     print("displacement")
#     print(disp_val)
#     print("orientation")
#     print(orientation_val[1][1]*180/math.pi)
#     time.sleep(0.5)

# while count<50:
#     time.sleep(0.1)
#     left_sensor1 = vrep.simxReadVisionSensor(clientID, leftsensor, vrep.simx_opmode_streaming)
#     mid_sensor1 = vrep.simxReadVisionSensor(clientID, midsensor, vrep.simx_opmode_streaming)
#     right_sensor1 = vrep.simxReadVisionSensor(clientID, rightsensor, vrep.simx_opmode_streaming)
#     print(left_sensor1[1])
#     print(mid_sensor1[1])
#     print(right_sensor1[1])
#     count = count + 1
# #returnCode,position=vrep.simxGetObjectPosition(clientID,robot_handle,-1,vrep.simx_opmode_buffer)

odometer_val = vrep.simxGetObjectPosition(clientID,leftmotor,floor,vrep.simx_opmode_continuous)
    
returnCode=vrep.simxSetJointTargetVelocity(clientID,leftmotor,31.416/40,vrep.simx_opmode_streaming)
returnCode=vrep.simxSetJointTargetVelocity(clientID,rightmotor,-31.416/40,vrep.simx_opmode_streaming)
# for i in range(40):
#     odometer_val = vrep.simxGetObjectPosition(clientID,leftmotor,floor,vrep.simx_opmode_continuous)
#     orientation_val = vrep.simxGetObjectOrientation(clientID,leftmotor,floor,vrep.simx_opmode_continuous)
#     disp_val = math.sqrt(odometer_val[1][0]*odometer_val[1][0] + odometer_val[1][1]*odometer_val[1][1])
#     print("displacement")
#     print(disp_val)
#     print("orientation")
#     print(orientation_val[1][1]*180/math.pi)
#     time.sleep(0.5)
returnCode = vrep.simxStopSimulation(clientID,vrep.simx_opmode_oneshot)

time.sleep(0.1)
