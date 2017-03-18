from pancackes import *

def readfrom(source, target):

    f = open(source)
    lines = f.readlines()
    f.close()

    T = int(lines[0])
    inputs = lines[1:]
    i = 1
    f = open(target, 'w')
    
    if T in range(1, 101):
        for stack in inputs:
            
            stack = stack.rstrip('\n')
            if len(stack) in range(1, 101):
                print "Case #"+str(i)+': '+str(head_waiter.run(stack))
                f.write("Case #"+str(i)+': '+str(head_waiter.run(stack))+'\n')
                i+=1
    f.close()


def console():

    cmd = raw_input("waiter> ")

    l = cmd.split(' ')
    src = l[0]
    dest = l[1]

    try:
        readfrom(src, dest)
    except:
        console()

    console()


console()
