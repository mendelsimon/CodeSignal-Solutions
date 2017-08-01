def avoidObstacles(inputArray):
    for length in range(2, max(inputArray) + 2):
        done = True
        jump = length
        while jump < (max(inputArray) + length):
            if jump in inputArray:
                done = False
                break
            jump += length
        if done:
            return length
