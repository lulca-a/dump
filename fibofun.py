def fibolist(length:int):
    stopper = 0
    a,b = 0,1
    fibo_list = [a]
    while stopper <length-1:#already has the first position
        a,b = b,b+a
        #print(a)
        fibo_list.append(a)
        stopper += 1
    return fibo_list

def fibopos(length:int):
    stopper = 0
    a,b = 0,1
    fibo_list = [a]
    
    while stopper <length-1:
        a,b = b,b+a
        fibo_list.append(a)
        stopper += 1
    
    return list(enumerate(fibo_list,start=1))

def fibomax(length:int): #return the specific number according to the lenght 
    stopper = 0
    a,b = 0,1
    fibo_list = [a]
    while stopper <length-1:
        a,b = b,b+a
        fibo_list.append(a)
        stopper += 1
    return fibo_list[-1]

