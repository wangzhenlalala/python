## yield 和 return 的作用的异同

def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                ##这里的语句会被执行吗
                print('element',element)
                yield element
    except TypeError:
        print('nested', nested)
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
# error()

lies = [1,2,[3,4]]
gen = flatten(lies)
for i in gen:
    print('print', i)