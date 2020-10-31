#!/usr/bin/env python
# coding: utf-8

# In[12]:


from simpleai.search import SearchProblem, astar

GOAL = 'Artificial Intelligence n Deep Learning'


class HelloProblem(SearchProblem):
    def actions(self, state):
        if len(state) < len(GOAL):
            alphabets = 'abcdefghijklmnopqrstuvwxyz'
            return list(alphabets + ' ' + alphabets.upper())
        else:
            return []

    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        # how far are we from the goal?
        wrong = sum([1 if state[i] != GOAL[i] else 0
                    for i in range(len(state))])
        missing = len(GOAL) - len(state)
        return wrong + missing

problem = HelloProblem(initial_state='')
result = astar(problem)

print(result.state)
print(result.path())


# In[ ]:




