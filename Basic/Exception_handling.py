def m1():

    print('Inside M1 Method..')
    try:
        print('inside try block..')
        print('A'+'p')
        print('try block completed')
        print('inside else block')

        return 10


    except ZeroDivisionError as V:
        print('inside zerodivision error',V)

    except TypeError as T:
        print('inside type error',T)

    # else:
    #     print('inside else block')

    finally:
        print('inside finally')
        return 45
m1()
