'''
 From the GYM repo itself:
 The main API methods that users of this class need to know are:
        step
        reset
        render
        close
        seed
    When implementing an environment, override the following methods
    in your subclass:
        _step
        _reset
        _render
        _close
        _seed
    And set the following attributes:
        action_space: The Space object corresponding to valid actions
        observation_space: The Space object corresponding to valid observations
        reward_range: A tuple corresponding to the min and max possible rewards
    The methods are accessed publicly as "step", "reset", etc.. The
    non-underscored versions are wrapper methods to which we may add
    functionality to over time.

'''
import gym
from gym import spaces
from utils import *
import numpy as np

class MySpace(gym.Space):
    '''
    To be written for creation of a new space.
    '''
    def __init(self):
        self.counter = 0  # just playing

    def contains(self, x):
        """
        Return boolean specifying if x is a valid
        member of this space
        """
        return not True  # TODO

'''
Want to try and keep this example as minimal as possible so that we can see what gym HAS and REQUIRES in creating
new environments.
'''

class DummyEnv(gym.Env):
    # Set this in SOME subclasses
    metadata = {'render.modes': ['human']}

    def __init__(self):
        '''
        gym.Env uses __new__ - so we dont need to call super's __init__ method
        '''
        self.action_space = spaces.Discrete(2)
        self.observation_space = MySpace()
        self.reward_range = (-np.inf,np.inf)

    def _reset(self):
        self.state = MySpace()

    def _step(self, action):
        '''
        note about info -
        (dict): diagnostic information useful for debugging.
        It can sometimes be useful for learning (for example, it might contain the raw probabilities
        behind the environment's last state change). However,
        official evaluations of your agent are not allowed to use this for learning.

        :param action:
        :return: State(object),reward(float),done(boolean),info(dict)
        '''
        somestate = MySpace()
        reward = -1
        assert(action in [0,1])
        if action == 0:
            done = np.random.uniform() > 0.75
        elif action == 1:
            done = np.random.uniform() > 0.25       # meh - just playing    - note no notion of altering state currently
        info = {}
        return somestate, reward, done, info

    def _render(self, mode='human', close=False):
        '''
        core.py (of gym) checks this environments metadata -- which lists (as a dict value) the supported modes of rendering
        :param mode:
        :param close:
        :return:
        '''
        if close:
            return
        if mode == 'human':
            print self.state

    def _seed(self, seed=None):
        return []

    def _close(self):
        pass

if __name__=='__main__':
    # env = gym.make() ?  or MyEnv() ?  gym.make() once env has been placed within gym (somehow). ie official. (i think).
    env = DummyEnv()
    agent = RandomAgent(env.action_space)

    do_rollout(agent, env, num_steps=10, render=True)

'''
THOUGHTS ON WHAT IS REQUIRED TO CREATE A DIALOGUE ENVIRONMENT + WHAT THE BENEFITS WOULD BE:
- would basically be a simulated user
- need to define:
    STATE SPACE:

    ACTION SPACE:

    ENVIRONMENT:

'''