#Project No. 20
import random 
import numpy as np
N = int(input("Enter Size of matrix : "))

if N == 3:
    x = 5     # ------------------------------------------ fix value
    a,b = random.choice([(3,1),(3,-1),(-3,-1),(-3,1),(-1,3),(-1,-3),(1,-3),(1,3)])
    ans =np.array([[x+a,x-a-b,x+b],[x-a+b,x,x+a-b],[x-b,x+a+b,x-a]])
    print(ans)
else:
    print("Invalid")