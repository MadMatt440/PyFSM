#fsm

class State:
    def __init__(self, state_action):
        self.action = state_action

    def __repr__(self):
        return f"<State: {self.action}>"

class FSM:
    def __init__(self, start_state, transitions):
        if start_state not in transitions:
            raise ValueError("Start state must be in the transitions table")
        
        self.current_state = start_state
        self.transitions = transitions

    def transition(self, input_value) -> State:
        state_transitions = self.transitions[self.current_state]

        if input_value not in state_transitions:
            raise ValueError(f"invalid input {input_value} in state {self.current_state} ")
        
        self.current_state = state_transitions[input_value];

        return self.current_state

    def get_state(self) -> State:
        return self.current_state



fight  = State("Fight state")
run = State("Run state")
defend = State("Defend state")

InputA = 0
InputB = 1

current_state = fight

machine = {fight:{InputA:run, InputB:defend},
            run:{InputA:fight, InputB:defend},
              defend:{InputA:fight, InputB:run}}


fsm = FSM(fight, machine)

print("Finite State Machine")
print("Start:", fsm.get_state().action)

print("InputA ->", fsm.transition(InputA).action)
print("InputA again ->", fsm.transition(InputA).action)
print("InputB ->", fsm.transition(InputB).action)

print("sucessfully ran")


