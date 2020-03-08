# states x xt (probability)
#     1   2   3
#   _|_ _ _ _ _ _|_
# A  |x   x   x  |
# B  |x   x   x  |
# C  |x   x   x  |
#   _|_ _ _ _ _ _|_
#    |           |
symbol_probabilities = [
    [0.9, 0.1, 0.0],
    [0.1, 0.8, 0.1],
    [0.0, 0.1, 0.9]
]

T = 55

# input
input = [1, 1, 1, 1, 1, 1, 1, 2, 2, 3,
         2, 2, 2, 2, 2, 2, 3, 2, 3, 1,
         1, 1, 1, 1, 2, 3, 2, 2, 2, 3,
         1, 1, 1, 2, 2, 2, 2, 1, 2, 1,
         1, 1, 1, 1, 3, 1, 2, 2, 1, 2, 1, 1, 1, 1, 1]

# states x T (probability)
#     t1  t2  t3
#   _|_ _ _ _ _ _|_
# A  |x   x   x  |
# B  |x   x   x  |
# C  |x   x   x  |
#   _|_ _ _ _ _ _|_
#    |           |
max_probability = [
    [0.0] * T,
    [0.0] * T,
    [0.0] * T
]

# states x T (states)
#     t1  t2  t3
#   _|_ _ _ _ _ _|_
# A  |-1  A   B  |
# B  |-1  B   A  |
# C  |-1  C   C  |
#   _|_ _ _ _ _ _|_
#    |           |
max_probability_predecessor = [
    [-1] + [0] * (T - 1),
    [-1] + [0] * (T - 1),
    [-1] + [0] * (T - 1)
]

# starting probabilities by state
initial_probabilities = [1/3, 1/3, 1/3]

# transition probabilities to other states from A
A = [0.8, 0.1, 0.1]

# transition probabilities to other states from B
B = [0.1, 0.8, 0.1]

# transition probabilities to other states from C
C = [0.5, 0.5, 0.0]

# transition matrix for all states
# states x states (probability)
#     A   B   C
#   _|_ _ _ _ _|_
# A  |x   x   x|
# B  |x   x   x|
# C  |x   x   x|
#   _|_ _ _ _ _|_
#    |         |
transition_matrix = [
    A,
    B,
    C
]

# initialize transition path data
for state, probability in enumerate(initial_probabilities, start=0):
    max_probability[state][0] = symbol_probabilities[state][input[0] - 1] * probability

# create maximum path data
for i in range(1, T):
    for state, state_transitions in enumerate(transition_matrix, start=0):
        for post_state, post_transition in enumerate(state_transitions, start=0):
            if max_probability[post_state][i] < post_transition * max_probability[state][i - 1]:
                max_probability[post_state][i] = post_transition * max_probability[state][i - 1]
                max_probability_predecessor[post_state][i] = state
    # symbol transition probabilities need to be applied after determining the maximum value for a post state
    for post_state, post_state_transitions in enumerate(transition_matrix, start=0):
        max_probability[post_state][i] = max_probability[post_state][i] * symbol_probabilities[post_state][input[i] - 1]

# determine matrix entry state with highest probability after T steps
max_state = 0
for state, probabilities in enumerate(max_probability, start=0):
    if max_probability[max_state][T - 1] < probabilities[T - 1]:
        max_state = state

# final path of highest probability states
max_path = [0] * T

# determine and print max path

max_path[T - 1] = max_state
# determine values for remaining entries
for i in reversed(range(1, T)):
    max_state = max_probability_predecessor[max_state][i]
    max_path[i - 1] = max_state

print("Most probable path:[", end='')
for index, state in enumerate(max_path, start=0):
    if index > 0:
        print(", ", end='')
    if state == 0:
        print("A", end='')
    elif state == 1:
        print("B", end='')
    elif state == 2:
        print("C", end='')
print("]")
