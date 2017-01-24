#Signs of Life

##Abstract
We want to learn applied reinforcement learning. The first step in doing so is a very practical one. Build a robot that can move freely without frying it's motors. This will serve as an introduction for anyone looking to do get a simple robot up and running so they can begin running algorithms.


##Building the physical robot
blah blah

##Empowering the robot
The basic reinforcement learning framework is simple. The agent (your algorithm) determines what state it's in based off of some sensation, determines what action to take (based on what it's learned), and performs this action within the environment. The environment responds with a reward and state update. In the bandit example, there is only one state, so the agent, based on experience decides which arm to pull. Once pulled, the environment responds with a reward (the amount recieved from pulling the slot machine). If the reward was largely positive, the agent would be wise to favor this action in the future. Conversly, if the reward was negative, the agent would be wise to avoid this. This of course is over simplifying. Life, and the bandit example, is stochastic. You may pull an arm of the bandit and recieve a negative reward, but there may be a massive jackpot waiting 2 pulls away. Therein lies the balance between exploration and exploitation. A successful player at the casino would balance pulling the most optimal arm of the bandit with the reality that they may not know the most optimal, and require exploration. Nevertheless, the basic Reinforcement Loop is simple. The agent senses it's state, determines it's "best action", takes that action, and is given a reward. Given that reward, it learns what it may do in the future to perform even better.

![alt text](Reference/RLLoop.png "RLLoop")

More stuff here.

##Initialize the robot
You need to initialize. That can be done like the following

```python
#From TestHarness.py
#ask algorithm for the arm it should pull
arm = algorithm.policy()
#pull the arm and collect the reward
reward = bandit.pull(arm)
#allow the algorithm to learn based on result of the arm
algorithm.learn(reward, arm)

```
##Control the robot
There are several important files main files:

1. [RobotController.py](Code/RobotController.py)
  * This contains several functions making it easy to test various different algorithms.
2. [lib_robotis_hack.py](Code/lib_robotis_hack.py)
  * Represents one arm within a bandit. 
  * Each arm has a mean and variance from which rewards are stochastically returned

To do stuff
```python
from TestHarness import *
```

Here is a video of the robot performing random actions while the data is being visualized.

[![Alt text](https://img.youtube.com/vi/N1N4K3NNvtw/0.jpg)](https://www.youtube.com/watch?v=N1N4K3NNvtw)


##Visualizing the data
As the robot interacts with the world, it is important to be able to visualize the actions, and causal effect. Both in real time and after the fact.

To do so in real time: blah blah blah

To do so after the fact. Blah blah blah

