def goodVsEvil(good, evil):
    good = sum(map(int, good.split()))
    evil = sum(map(int, evil.split()))

    if good > evil:
        return "Battle Result: Good triumphs over Evil"
    elif evil > good:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"
