def lineUp(commands):
    count = 0
    smart_student = 0
    dumb_student = 0
    for command in commands:
        if command == 'L':
            smart_student = (smart_student - 1) % 4
            dumb_student = (dumb_student + 1) % 4
        elif command == 'R':
            smart_student = (smart_student + 1) % 4
            dumb_student = (dumb_student - 1) % 4
        elif command == 'A':
            smart_student = (smart_student + 2) % 4
            dumb_student = (dumb_student + 2) % 4

        if smart_student == dumb_student:
            count += 1
    return count
