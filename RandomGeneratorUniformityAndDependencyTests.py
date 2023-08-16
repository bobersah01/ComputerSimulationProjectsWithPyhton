#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

#We are using this function for generating random numbers based on determined parameters that are taken from user.
def generator(N, x0, a, c, m):
    randomNumbersList = list()  #We are cretaing a list.
    storedNum = x0

    for i in range(N):
        storedNum = (a* storedNum + c) % m  # Applying the formula.
        randomNumbersList.append(storedNum / m)  # Append created numbers to the list.

    return randomNumbersList  # Return the list.

def mid_square_method(x, N):
    arr = []  # Create a list to store the generated numbers.
    
    for i in range(N):
        xn = x * x  # Apply the formula.
        str_xn = str(xn)
        
        while len(str_xn) < 8:
            str_xn = "0" + str_xn
        
        str2 = str_xn[2:7]
        
        x = int(str2)
        
        arr.append(x / 10000.0)  # Append created numbers to the list.
    
    return arr  # Return the list.

def additive_congruential_method(N, x1, x2, x3, x4, x5, m):
    arr = []  # Create a list to store the generated numbers.
    
    numbers = [x1, x2, x3, x4, x5]
    
    for i in range(N):
        a = (numbers[i] + numbers[-1]) % m
        numbers.append(a)
        arr.append(a)
    
    return arr  # Return the list.

#For testing, first we are applying Kolmogorov-Smirnov test. 
def testFunction(randomNumbersList):
    
    randomNumbersList.sort()
    criticalValue = 0.136 #number for D alpha value for 0.05; 1,36/(10) 
    sizeOfList = len(randomNumbersList)
    
    emptyList = list()

    for i in range(sizeOfList):
        
        positiveD = (i + 1) / sizeOfList - randomNumbersList[i] #PosD 
        negativeD = randomNumbersList[i] - i / sizeOfList  #NegD
        
        #We are adding the D plus and D minus values for taking maximum of their numbers.
        emptyList.append(positiveD)
        emptyList.append(negativeD)
        
    maximumEmptyList = max(emptyList)
    #evaluatedCritical = criticalValue / math.sqrt(sizeOfList)
    print("Maximum of the empty list - D value: {}".format('%6.3f' % maximumEmptyList)) #Printing out the D alpha value.
        
    #When the first condition is executed, it means that generated random numbers are not uniform.
    #Otherwise, it means that generated random numbers are uniform.
        
    if maximumEmptyList > criticalValue:
        print("Kolmogorov-Smirnov Test: Not Uniform")
    else:
        print("Kolmogorov-Smirnov Test: Uniform")
        

def chi_square_test_uniform(arr, interval, critical):
    arr.sort()
    n = len(arr)
    
    Ei = n // interval
    
    total_sum = 0
    count = 0
    product = 1
    
    for i in range(n):
        if arr[i] < product * (1 / interval):
            count += 1
        else:
            total_sum += ((count - Ei) ** 2) / Ei
            product += 1
            count = 1
    
    if n < 51:
        print("N must be bigger or equal to 50")
    else:
        if total_sum < critical:
            print("Chi-Square Test: Uniform")
        else:
            print("Chi-Square Test: Not Uniform")


def runs_up_down_test(arr, critical):
    check = True
    count = 0
    
    n = len(arr)
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            if not check or i == 0:
                count += 1
            check = True
        elif arr[i] < arr[i + 1]:
            if check:
                count += 1
            check = False
    
    z = (count - ((2 * n - 1) / 3)) / math.sqrt((16 * n - 29) / 90)
    
    if z > critical or z < -1 * critical:
        print("Runs Up and Runs Down Test: Not Independent")
    else:
        print("Runs Up and Runs Down Test: Independent")
        

def above_below_test(arr, critical):
    n = len(arr)

    v1 = []
    v2 = []
    
    total_sum = 0.0
    
    for i in range(n):
        total_sum += arr[i]
    
    mean = total_sum / n
    
    for i in range(n):
        if arr[i] >= mean:
            v1.append(arr[i])
        else:
            v2.append(arr[i])
    
    v1_size = len(v1)
    v2_size = len(v2)
    
    check = True
    count = 0
    
    for i in range(n - 1):
        if arr[i] >= mean:
            if not check or i == 0:
                count += 1
            check = True
        elif arr[i] < mean:
            if check:
                count += 1
            check = False
    
    z_val = (count - (2 * v1_size * v2_size) / n - 0.5) / math.sqrt((2 * v1_size * v2_size * (2 * v1_size * v2_size - n)) / (n * n * (n - 1)))
    
    if z_val > critical or z_val < -1 * critical:
        print("Runs Above and Below the Mean Test: Not Independent")
    else:
        print("Runs Above and Below the Mean Test: Independent")


def autocorrelation_test(arr, i, m, critical):
    N = len(arr)
    M = 0
    
    while i + (M + 1) * m <= N:
        M += 1
    
    total_sum = 0
    
    for j in range(M):
        total_sum += arr[i + m * j] * arr[i + m * (j + 1)]
    
    total_sum = (total_sum * (1 / (M + 1))) - 0.25
    
    alpha = math.sqrt(13 * M + 7) / (12 * (M + 1))
    
    z_score = total_sum / alpha
    
    if z_score > critical or z_score < -1 * critical:
        print("Autocorrelation Test: Not Independent")
    else:
        print("Autocorrelation Test: Independent")

def poker_test(arr, critical):
    n = len(arr)
    
    total_sum = 0.0
    
    threedif = 0
    onediff = 0
    same = 0
    
    for i in range(n):
        num_str = str(arr[i])
        
        if num_str[3] != num_str[2] and num_str[2] != num_str[4] and num_str[3] != num_str[4]:
            threedif += 1
        elif num_str[3] == num_str[2] and num_str[2] == num_str[4] and num_str[3] == num_str[4]:
            same += 1
        else:
            onediff += 1
    
    total_sum += pow(2, (threedif - 720)) / 720
    total_sum += pow(2, (onediff - 270)) / 270
    total_sum += pow(2, (same - 10)) / 10
    
    if total_sum > critical:
        print("Poker Test: Not Independent")
    else:
        print("Poker Test: Independent")


def main():
    
    #We are executing generator and test function in the maimn function.
    #constant number called N and other numbers that have to be taken from the user as input.
    
    N = 100 #determined in the question. Total number generated.
    x0 = int(input("Enter x0 (initial value): "))
    a = int(input("Enter a: "))
    c = int(input("Enter c: "))
    m = int(input("Enter m: "))
    
    #Critical Values For Runs up Down and chi square tests.
    #criticalValueForRunDown = 1.96
    #criticalValueForChiSquare = 1.96
    
    #interval for chi square test
    #interval = 10
    
    #Randomgenerator 
    randomNumbers = generator(N, x0, a, c, m)
    #randomNumbers = mid_square_method(x, N)
    
    for index, num in enumerate(randomNumbers, start=1):
        print(f'{index}: {num:6.3f}')
    
    #for num in randomNumbers:
    #   print(f"{num:.3f}", end=" ")
    #print("----------------------------------------------------------")
    

    testFunction(randomNumbers)
    #chi_square_test_uniform(randomNumbers, interval, criticalCS)
    #runs_up_down_test(randomNumbers, criticalValueForRunDown)
    #above_below_test(randomNumbers, criticalRD)
    #autocorrelation_test(randomNumbers, 3, 5, criticalRD)
    #poker_test(randomNumbers, criticalRD)
    
main()

