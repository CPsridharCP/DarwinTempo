#!/usr/bin/env python
import rospy
from darwin_gazebo.darwin import Darwin

def frange(start, stop, step, sign):
    ''' "range()" like function which accept float type''' 
    i = start
    if sign==1:
    	while i < stop:
        	yield i
        	i += step
    elif sign==0:
    	while i > stop:
    		yield i
    		i += step


def path(home,end,interval):

	diff = end-home
	delta = diff/interval
	if diff>0:
		direction = 1
	elif diff<0:
		direction = 0

	ans = [x for x in frange(home,end+delta,delta,direction)]
	#print ans
	#print (len(ans))
	# found few mismatch with an extra element contribiting to error in some test cases
	# clearing them off
	final_ans = [ans[x] for x in range(0,int(interval)+1)]
	#print final_ans
	#print (len(final_ans))
	return final_ans

if __name__=="__main__":
    rospy.init_node("walker_demo")
    rospy.loginfo("Instantiating Darwin Client")
    darwin=Darwin()
    rospy.sleep(1)

    darwin.set_angles({"j_pan": 1})
    
    steps = 5.0

    j_high_arm_r = 1.343676989
    j_high_arm_l = 1.378893255

    j_shoulder_r = 0.831647219
    j_shoulder_l = 0.711766896
    
    j_low_arm_r = 1.499488737
    j_low_arm_l = -1.508986304

    
    j_high_arm_r_path = path(0.0,j_high_arm_r,steps)
    j_high_arm_l_path = path(0.0,j_high_arm_l,steps)
    j_shoulder_r_path = path(0.0,j_shoulder_r,steps)
    j_shoulder_l_path = path(0.0,j_shoulder_l,steps)
    j_low_arm_r_path  = path(0.0,j_low_arm_r,steps)
    j_low_arm_l_path  = path(0.0,j_low_arm_l,steps)

    for i in range(0,int(steps)+1):
    	darwin.set_angles({"j_high_arm_r": j_high_arm_r_path[i]})
    	darwin.set_angles({"j_high_arm_l": j_high_arm_l_path[i]})
    	darwin.set_angles({"j_shoulder_r": j_shoulder_r_path[i]})
    	darwin.set_angles({"j_shoulder_l": j_shoulder_l_path[i]})
    	darwin.set_angles({"j_low_arm_r": j_low_arm_r_path[i]})
    	darwin.set_angles({"j_low_arm_l": j_low_arm_l_path[i]})
    	rospy.sleep(1)





