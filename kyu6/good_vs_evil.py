def goodVsEvil(good, evil):
    good_score = {
        1: 1,
        2: 2,
        3: 3,
        4: 3,
        5: 4,
        6: 10
    }
    evil_score = {
        1: 1,
        2: 2,
        3: 2,
        4: 2,
        5: 3,
        6: 5,
        7: 10
    }
    good = sum([good_score[key] * times for key, times in enumerate(map(int, good.split()), 1)])
    evil = sum([evil_score[key] * times for key, times in enumerate(map(int, evil.split()), 1)])

    if good > evil:
        return "Battle Result: Good triumphs over Evil"
    elif evil > good:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"
