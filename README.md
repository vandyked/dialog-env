# dialog-env
First look at creating open AI gym environments, specifically for dialog

# Notes on creating an environment for learning dialog policies:
Environment has and returns the following components:
    - action space A: defines a set of legal actions an agent can take
        for example a summary dialog policy actino space: defining all 
        actions available to a dialog policy
    - state space S:  defines the space from which a state is emitted at
        each step and that is then used by the policy to produce A. 
         
         
    So a dialog would occur as follows, btw [agent] and [env],
    remembering that [env] is exactly the conversational partner, aka
    simulated user:
    turn 0 (setup):
    -----------
    [env] - is reset --> (goal is generated and agenda formed --> u.sim
        act produced -> belief tracker consumes u.sim act) --> outputs
        a belief state S. 
        Other init:
            done == false
            reward == 0
            info == dict containing goal and agenda. not to be used by
            policy but helpfull for debugging. 
    turn 1:
    -----------
    [agent] consumes b,r,done (not sure why it consumes done - since
        it is only every going to be false since we break when true...?)
        --> outputs an element of A, action.
    [env]  consumes action - (responds with u.sim action --> updates 
        belief state with this and action from agent/policy) --> outputs
        S, along with reward and done. 
    turn 2:
    -----------
    etc ... process continues like this until sim user state is done.
