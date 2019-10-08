def enough(cap, on, wait):
    # Your code here
    if cap < (on + wait):
        return ((on + wait) - cap)
    else:
        return 0