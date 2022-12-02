input_txt = open('./input/2.txt')
lines = input_txt.readlines()


"""

A/X - Rock
B/Y - Paper
C/Z - Scissors

A Beats Z
B Beats X
C Beats Y

X Beats C
Y Beats A
Z Beats B
"""

strategy_guide = {
    'A': 'Y',
    'B': 'X',
    'C': 'Z',
}
shape_points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
wins = [
    ('B', 'Z'),
    ('A', 'Y'),
    ('C', 'X')
]

ties = [
    ('A', 'X'),
    ('B', 'Y'),
    ('C', 'Z')
]

actions = {
    'lose': {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    },
    'win': {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    },
    'draw': {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }
}

total_points = 0

for round in lines:
    rsplit = round.replace('\n', '').split(' ')
    total_points += shape_points[rsplit[1]]
    if tuple(rsplit) in wins:
        total_points += 6
    if tuple(rsplit) in ties:
        total_points += 3

print(total_points)

# Second Half

total_points = 0

for round in lines:
    rsplit = round.replace('\n', '').split(' ')
    if rsplit[1] == 'X':
        total_points += shape_points[actions['lose'][rsplit[0]]]
    if rsplit[1] == 'Y':
        total_points += shape_points[actions['draw'][rsplit[0]]] + 3
    if rsplit[1] == 'Z':
        total_points += shape_points[actions['win'][rsplit[0]]] + 6

print(total_points)