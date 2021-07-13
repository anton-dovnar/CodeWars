def bouncing_ball(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and window < h:
        times = 1
        rate = h * bounce
        while rate > window:
            rate *= bounce
            times += 2
        return times
    return -1
