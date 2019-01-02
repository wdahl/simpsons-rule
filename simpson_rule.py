import math

def Simpson(a, b, n):
    if a > b:
        print ('Incorrect bounds')
        return None
    if n%2 != 0: # also an 'if' because both tests are NOT
        # mutually exclusive
        print ('Invalid choice of n')
        return None
    else:
    	h = (b - a)/float(n) # need to cast 'n' as float in order to avoid
        # integer division
    	sum1 = 0
    	for i in range(1, int(n/2) + 1):
        	sum1 += f(a + (2*i - 1)*h)
    	sum1 *= 4
    	sum2 = 0
    	for i in range(1, int(n/2)): # range must be ints: range() integer 
            #end argument expected, got float.
        	sum2 += f(a + 2*i*h)
    	sum2 *= 2
    	approx = (b - a)/(3.0*n)*(f(a) + f(b) + sum1 + sum2)
    	return approx

def f(x):
    return math.pow(x, 2.5)

print ("Simpson approximation:")
for n in 2,4,8,16,32,64,128,256:
    if n is not 2:
        prev_error = error
        error = 2/7 - Simpson(0, 1, n)
        print ('For n=%g:   approx=%.10f,   error~%E, ratio=%f' % \
        (n, Simpson(0, 1, n), error, abs((error-prev_error)/prev_error)))

    else:
        error = 2/7 - Simpson(0, 1, n)
        print ('For n=%g:   approx=%.10f,   error~%E' % \
        (n, Simpson(0, 1, n), error))