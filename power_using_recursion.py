#Implementing power(base, power) function using recursion

##def power(n,p):
##    if p == 0:
##        return 1
##    elif p == 1:
##        return n
##    else:
##        return n*power(n,p-1)

def power(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2) # rely on truncated division
        result = partial * partial
        if n % 2 == 1:
            # if n odd, include extra factor of x
            result *= x
        return result


print(power(2,100000))

#num = 83711609936427134449095706957812641450109750914494813081542999091433675869135634569781123344976238916218333821683839595717745725444712034656129512302332615655738810740814304573602145352049774545921517048070675585809233916151552871555980812078727054020087472481926110684847108059786128022165669281792000000000000
#print(num)

