'''
For Dummy Env
'''

class RandomAgent(object):
    '''Just to test environment API setup is correct
    '''
    def __init__(self, action_space):
        self.action_space = action_space
    def act(self, ob, reward, done):
        return self.action_space.sample()



def do_rollout(agent, env, num_steps, render=False):
    '''
     generic function (modified from gym examples) that will work for most agent:
    :param agent:
    :param env:
    :param num_steps:
    :param render:
    :return:
    '''
    total_rew = 0
    # Initial observations from environment
    ob = env.reset()
    reward = 0
    done = False

    for t in range(num_steps):
        a = agent.act(ob, reward, done)
        if render: env.render()     # here to capture env then agent utterances
        (ob, reward, done, _info) = env.step(a)
        total_rew += reward

        if done: break
    return total_rew, t+1
