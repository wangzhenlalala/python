## yield 和 return 的作用的异同

def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                ##这里的语句会被执行吗
                yield element
    except TypeError:
        yield nested

def error():
        time = 0
        while time < 10:
            try:
                if time % 2 == 0:
                    raise Exception
                else:
                    print(time)
            except:
                    print('no')
            time+=1
error()