# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:50:28 2022

@author: KADA_AIWORKSTATION
"""

import gym
import pygame
import numpy as np
from gym import spaces

class CustomEnv(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {"render.modes": ["human"]}
    N_DISCRETE_ACTIONS = 4
    
    def __init__(self, render_mode=None, size=5):
        super(CustomEnv, self).__init__()
        self.size = size  # The size of the square grid
        self.window_size = 512  # The size of the PyGame window
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)     
        # Example for using image as input (channel-first; channel-last also works):
        self.observation_space = spaces.Box(0, size - 1, shape=(2,), dtype=int)
        

    def step(self, action):
        ...
        return observation, reward, done, info
    def reset(self):
        ...
        return observation  # reward, done, info can't be included
    def render(self, mode="human"):
        ...
    def close (self):
        ...