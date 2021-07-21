LEFT_POWER = {
    'w': 4,
    'p': 3,
    'b': 2,
    's': 1,
    't': 0,
}

RIGHT_POWER = {
    'm': 4,
    'q': 3,
    'd': 2,
    'z': 1,
    'j': 0,
}

LEFT_TO_RIGHT = dict(zip(LEFT_POWER.keys(), RIGHT_POWER.keys()))
RIGHT_TO_LEFT = dict(zip(RIGHT_POWER.keys(), LEFT_POWER.keys()))


def alphabet_war(fight):
    fight = list('aa' + fight + 'aa')
    for i in range(2, len(fight)-2):
        if fight[i] == 't':
            if 'j' not in fight[i+1:i+3] and fight[i+1] in RIGHT_POWER:
                fight[i+1] = RIGHT_TO_LEFT[fight[i+1]]

            if 'j' not in fight[i-2:i] and fight[i-1] in RIGHT_POWER:
                fight[i-1] = RIGHT_TO_LEFT[fight[i-1]]

        elif fight[i] == 'j':
            if 't' not in fight[i+1:i+3] and fight[i+1] in LEFT_POWER:
                fight[i+1] = LEFT_TO_RIGHT[fight[i+1]]

            if 't' not in fight[i-2:i] and fight[i-1] in LEFT_POWER:
                fight[i-1] = LEFT_TO_RIGHT[fight[i-1]]

    left_power_counter = 0
    right_power_counter = 0

    for letter in fight:
        if letter in LEFT_POWER:
            left_power_counter += LEFT_POWER[letter]
        elif letter in RIGHT_POWER:
            right_power_counter += RIGHT_POWER[letter]

    if left_power_counter == right_power_counter:
        return "Let's fight again!"

    return ["Left side wins!", "Right side wins!"][right_power_counter > left_power_counter]
