def sortColors(nums):
    z,o,t=0,0,0
    for i in nums:
        if i==0:
            z+=1
        elif i==1:
            o+=1
        elif i==2:
            t+=1
    for i in range(len(nums)):
        if i<z:
            nums[i]=0
        elif i<z+o:
            nums[i]=1
        elif i<z+o+t:
            nums[i]=2
##lst=[2,0,2,1,1,0]
##sortColors(lst)
##print(lst)
def flip(A):
    B=[]
    for i in range(len(A)):
        B.append(A[len(A)-1-i])
    return B
def pancakeSort(A):
    lst=[]
    i=len(A)-1
    while(i>0):
        j=i-1
        if(A[i]<A[j] and i==len(A)-1):
            if(A[i]<A[0]):
                A=flip(A)
                print(A)
                lst.append(i+1)
            else:
                flipped=flip(A[:i])
                A=flipped+A[i:]
                print(A)
                lst.append(i)
        elif(A[i]<A[j]):
            if(i==1):
                k=len(A)-1
                while(A[j]<A[k]):
                    k-=1
                flipped=flip(A[:k+1])
                A=flipped+A[k+1:]
                print(A)
                lst.append(k+1)
                i=k    
            elif(A[i]<A[0]):
                k=i+1
                flipped=flip(A[:k])
                A=flipped+A[k:]
                print(A)
                lst.append(k)
            else:
                flipped=flip(A[:i])
                A=flipped+A[i:]
                print(A)
                lst.append(i)
        else:
            i-=1
        print(A[i],A[j])
    return lst

print(pancakeSort([1,2,4,3]))









