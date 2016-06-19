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

class DialogEnvSpace(gym.Space):
    '''
    To be written for creation of a new space.
    -- for dialog - this would be the response action from a simulated user
    '''
    def __init(self):
        '''
        # Object creation:
        # a BELIEF TRACKER
        # -----------------
        # Then:
        0. belief state is reset
        :return:
        '''
        pass

    def contains(self, x):
        """
        Return boolean specifying if x is a valid
        member of this space
        """
        return not True  # TODO

    def restart(self):
        pass

'''
Want to try and keep this example as minimal as possible so that we can see what gym HAS and REQUIRES in creating
new environments.
'''

class DialogEnvInterface(gym.Env):
    # Set this in SOME subclasses
    metadata = {'render.modes': ['human']}      # TODO check modes -

    def __init__(self, configfile=None):
        '''
        gym.Env uses __new__ - so we dont need to call super's __init__ method
        # Object creation:
        # a SIMULATED USER
        # a DialogEnvSpace()  aka belief tracker
        '''
        self.construct(config=configfile)

    def construct(self, configfile):
        # TODO CONFIG base this so that we can plug in version0, version1 etc which will mean a certain combo of
        # user and belief state tracker and action space for agent.
        self.simulated_user = None  # TODO
        self.action_space = spaces.Discrete(2)  # TODO define agent summary action set
        self.observation_space = DialogEnvSpace()
        self.reward_range = (-np.inf,np.inf)

    def _reset(self):
        '''
            0. belief tracker reset.
            1. sim user will sample a goal and create an agenda from it
            2. first act on agenda fed through belief state tracker
            3. this belief state will be emitted.
        '''
        self.turn = 0
        self.belief_tracker.restart()
        self.user_act = self.simulated_user.restart()
        self.state = self.belief_tracker.track(user_act=self.user_act, agent_act=None)  # TODO sort out exact call for focus tracker
        return self.state  # also called observation  # TODO can also return info dict with sim user goal and agenda

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
        self.turn += 1
        self.agent_action = action
        self.user_act = self.simulated_user.respond(agent_act=action)
        self.done = False # if 'bye' then done = True else False or maxturns? TODO
        self.state = self.belief_tracker.track(user_act=self.user_act, agent_act=action)  # TODO for focus tracker
        # calculate reward
        self.reward = -1  # TODO
        # info ?
        self.info = {} # TODO
        return self.state, self.reward, self.done, self.info

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
            self.pretty_print_dialog_turn()

    def pretty_print_dialog_turn(self):
        print '-'*5
        print '{}\n: '.format(self.turn)
        print '[env/simuser]:{}\n[agent/policy]:{}'.format(self.user_act,self.agent_action)
        return


    def _seed(self, seed=None):
        return []

    def _close(self):
        pass

if __name__=='__main__':
    # env = gym.make() ?  or MyEnv() ?  gym.make() once env has been placed within gym (somehow). ie official. (i think).
    env = DialogEnvInterface()
    agent = RandomAgent(env.action_space)

    do_rollout(agent, env, num_steps=10, render=True)

'''
THOUGHTS ON WHAT IS REQUIRED TO CREATE A DIALOGUE ENVIRONMENT + WHAT THE BENEFITS WOULD BE:
- would basically be a simulated user
- need to define:
    STATE SPACE:  - some sort of belief state which agent would then act on

    ACTION SPACE: - some set of actions, likely summary

    ENVIRONMENT:  - along with state space, this would be completed by specifying a
                    reward function for state + action sequences.

'''