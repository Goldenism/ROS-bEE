#!/usr/bin/env python3
import rospy
from bee_foraging.srv import BeeForaging, BeeForagingResponse
from bee_foraging_env import BeeForagingEnv

def handle_bee_foraging(req):
    global env
    state, reward, done, info = env.step(req.action)
    response = BeeForagingResponse()
    response.state = state
    response.reward = reward
    response.done = done
    response.info = str(info)
    return response

def bee_foraging_service():
    rospy.init_node('bee_foraging_service')
    env = BeeForagingEnv()
    service = rospy.Service('bee_foraging', BeeForaging, handle_bee_foraging)
    rospy.spin()

if __name__ == "__main__":
    bee_foraging_service()



