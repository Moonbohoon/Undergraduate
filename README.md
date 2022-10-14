# Undergraduate


## Stable Baseline3 
pip install git+https://github.com/carlosluis/stable-baselines3@fix_tests

## After install SB3, To work in my custion Env, have to revise SB3 modules like thoses:
### C:\Users\anaconda3\envs\YOUR_VIRTUAL_ENV_NAME\Lib\site-packages\stable_baselines3\common\utils.py
* in line 329, change like -> 
```
if observation[0][key].shape != subspace.shape:
```
### C:\Users\anaconda3\envs\YOUR_VIRTUAL_ENV_NAME\Lib\site-packages\stable_baselines3\common\policies.py
* in line 250,251 change like ->   
```
            for key, subspace in self.observation_space.spaces.items():
                observation = observation.reshape((-1, ) + subspace.shape)             
        observation_ = observation[0][0]
        observation = obs_as_tensor(observation_, self.device)
```

### now error is
![image](https://user-images.githubusercontent.com/88705679/195842161-342e4e5b-04f5-4cb1-97ab-f434ffab4783.png)
