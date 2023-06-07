def validate_input(text):  # '1,2,3'
    try:
        s = []
        command = text.split(',')
        for i in command:
            s.append(int(i))
        return s
    except (ValueError, TypeError):
        return False


if validate_input('h,a,d') == False and \
        validate_input('1,2,3') == [1, 2, 3] and \
        validate_input('2,gf') == False and \
        validate_input('2') == [2] and \
        validate_input('g') == False:
    print('ok')
