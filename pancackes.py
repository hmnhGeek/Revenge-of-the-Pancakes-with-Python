

class pancackes(object):
    
    def __init__(self):
        self.moves = 0
        
    def all_happy(self, stack):

        if '-' in stack:
            return 0
        else:
            return 1

    def flipWhole(self, stack):
        stack = [i for i in stack]
        
        for i in range(len(stack)):
            if stack[i] == '+':
                stack[i] = '-'
            else:
                stack[i] = '+'
        s = ''
        for i in stack:
            s+=i
        self.moves+=1
        return s
    
    def run(self, stack):
        
        while not self.all_happy(stack):
            
            if stack[-1] == '-':
                stack = self.flipWhole(stack)
                
            else:
                i = -1
                while(stack[i] <> '-'):
                    i -= 1
                
                stack = stack[i::-1]
                
                stack = stack[-1:-len(stack)-1:-1]
                return self.run(stack)
                
        moves = self.moves
        self.moves = 0
        return moves
    
head_waiter = pancackes()

