# hare krishna

def find_lcm(numbers):
    h = max(numbers)

    lcm = h

    def check(l, numbers):
        remainders = [ l%n==0 for n in numbers]
        return all(remainders)

    while (check(lcm, numbers) == False):
        lcm = lcm + h
    
    return lcm
