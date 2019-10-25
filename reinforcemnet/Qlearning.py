import  gym
from time import sleep
from IPython.display import clear_output
import  numpy as np

env = gym.make("Taxi-v3").env

#Hyper-params
alpha, gamma, epsilon = 0.9 , 0.9 , 0.1

#For plotting
all_epochs,all_pentalies = [],[]


q_table = np.zeroes([env.observation_space ,env.action_space])


for i in range(1,100000):

    state = env.reset()
    epochs, penalties, reward = 0,0, 0
    done = False

#frames = []

while not done:
    action = env.action_space.sample()
    state, reward, done,info = env.step(action)
    #Q = States*Action
    #enviroment[Q(state,action)] = (1-alpha)*state + alpha* (reward(state)+ gamma*(max(next_state))

    if (reward ==-10):
        penalties +=1

    frames.append({
        'frame':env.render(mode='ansi'),
        'state':state,
        'action': action,
        'reward': reward
    })

    epochs +=1

print( "Timesteps taken: {}".format(epochs))
print("penalties incurred: {}".format(penalties))




def print_frames(frames):
    for i,frame in enumerate(frames):
        clear_output(wait=True)
        print(frame['frame'])
        print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.1)



print("Ready to see the results?")
#sleep(5)

print_frames(frames)