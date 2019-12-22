def fibo():
    x = int(input('jak dlugi ma byc ciag Fibonnaciego?'))
#    if x == 0 or x == 1:
#        y.append(1)
    y = [1, 1]
    for i in range(1, x):
            y.append(y[i] + y[i-1])
            y[1:x+1]
            return y    
print(fibo())
        


#wymaga przemyslenia i dopracowania 
        
