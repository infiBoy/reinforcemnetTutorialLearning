import  gym
from time import sleep
from IPython.display import clear_output

env = gym.make("Taxi-v3").env


env.s = 1

epochs = 0
penalties, reward = 0,0

frames = []

done =False

while not done:
    action = env.action_space.sample()
    state, reward, done,info = env.step(action)

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