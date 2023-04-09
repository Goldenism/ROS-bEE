# bee_foraging_env.py
import gym
import numpy as np
from gym import spaces
from gym.utils import seeding
from bee_foraging.srv import BeeForaging, BeeForagingResponse


class BeeForagingEnv(gym.Env):
    def __init__(self, training_phase=1):
        super(BeeForagingEnv, self).__init__()

        self.action_space = spaces.Discrete(12)
        self.observation_space = spaces.Box(low=0, high=1, shape=(12, 4), dtype=np.float32)

        self.seed()
        self.training_phase = training_phase
        self.reset()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        reward = 0
        done = False
        info = {}

        selected_flower = action
        flower_reward = self.state[selected_flower, 2]  # Use the reward column in the state
        reward += flower_reward

        self.state[selected_flower, 0] = 1  # Mark the selected flower as visited

        max_flowers_to_visit = 12
        if np.sum(self.state[:, 0]) >= max_flowers_to_visit:
            done = True
            info['score'] = reward

        return self.state.flatten().tolist(), reward, done, info

    def reset(self):
        self.state = np.zeros((12, 4))
        self._initialize_flowers()
        return self.state.flatten().tolist()

    def render(self, mode='human'):
        pass

    def _initialize_flowers(self):
        if self.training_phase == 1:
            flowers_properties = [
                (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
                (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
                (1, 0, 30), (1, 0, 30), (0, 1, 0), (0, 1, 0)
            ]
        elif self.training_phase == 2:
            flowers_properties = [
                (0, 0, 30), (0, 0, 30), (0, 0, 0), (0, 0, 0),
                (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
                (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)
            ]
        else:  # Test phase
            flowers_properties = [
                (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
                (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
                (1, 0, 0), (1, 0, 0), (0, 1, 0), (0, 1, 0)
            ]

        np.random.shuffle(flowers_properties)
        self.state[:, 1:] = flowers_properties


