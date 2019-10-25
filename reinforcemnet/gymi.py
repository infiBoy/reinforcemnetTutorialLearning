import gym
enviroment = gym.make("Taxi-v3").env

enviroment.render()

#env.reset()
#obs, reward, done, info = env.step()

state = enviroment.encode(0, 0, 0, 1) # (taxi row, taxi column, passenger index, destination index)
print("State:", state)
enviroment.s = state
enviroment.render()

#print("Action Space {}".format(enviroment.action_space))
#print("State Space {}".format(enviroment.observation_space))
print(enviroment.P[328])

#Learning from:
#States --> Actionts.



#P matrix goes as follow:
#{action: [(probability, nextstate, reward, done)]}