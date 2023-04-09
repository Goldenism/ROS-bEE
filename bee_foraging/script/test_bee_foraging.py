#!/usr/bin/env python3

import rospy
import numpy as np
import random
from bee_foraging.srv import BeeForaging

def test_environment():
    rospy.wait_for_service('bee_foraging')
    try:
        bee_foraging_service = rospy.ServiceProxy('bee_foraging', BeeForaging)
        initial_state = bee_foraging_service('reset')
        state = np.reshape(initial_state.state, (12, 4))

        # Loop until the episode is done
        done = False
        while not done:
            # Choose a random action
            agent = np.random.randint(12)
            print('Agent chose action:', agent)
            # Convert action to integer
            action = int(agent)
            # Send the action to the environment
            next_state = bee_foraging_service(action)
            state = np.reshape(next_state.state, (12, 4))
            done = next_state.done
            reward = next_state.reward
            print('Reward received:', reward)
            print('Next state:', state)
    except rospy.ServiceException as e:
        print('Service call failed:', e)

if __name__ == "__main__":
    rospy.init_node('test_bee_foraging')
    test_environment()



