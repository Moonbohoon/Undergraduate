# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:37:44 2022

@author: KADA_AIWORKSTATION
"""

import gym
import gym_examples
from stable_baselines3 import DQN
from stable_baselines3.common.env_checker import check_env

env = gym.make("gym_examples/GridWorld-v0")
# check_env(env)
model = DQN("MultiInputPolicy", env, verbose=1)
model.learn(total_timesteps=10000, log_interval=4)
model.save("dqn_GridWorld")

del model # remove to demonstrate saving and loading

model = DQN.load("dqn_GridWorld")

obs = env.reset()
env.reset()

# print(env.observation_space.shape)
# for key, subspace in env.observation_space.spaces.items():
#     print(env.observation_space.spaces.items())
#     print(subspace.shape)

while True:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
      obs = env.reset()
      