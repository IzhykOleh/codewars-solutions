class State:
    def __init__(self, initial_state):
        self.state = initial_state
    def __call__(self, new_state):
        self.state = new_state
    @property
    def get_state(self):
        return self.state

class Automaton(object):

    def __init__(self):
        self.states = []

    def read_commands(self, commands):
        # Return True if we end in our accept state, False otherwise
        state = State('q1')
        for com in commands:
            current_state = state.get_state
            if com == '1':                
                if current_state == 'q1':
                    state('q2')
                elif current_state == 'q2':
                    pass
                elif current_state == 'q3':
                    state('q2')
            elif com == '0':
                if current_state == 'q1':
                    pass
                elif current_state == 'q2':
                    state('q3')
                elif current_state == 'q3':
                    state('q2')
        return True if state.get_state == 'q2' else False
    
my_automaton = Automaton()
