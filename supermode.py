#Supermode Using Divide And Conquer
def supermodediv(arr):
    n=len(arr)
    
    if n==1:
        return arr[0]
    elif n==2:
            if arr[0]==arr[1]:
                return arr[0]
            else:
                return -1             
    
    supermode1 = supermodediv(arr[:n/2])
    supermode2 = supermodediv(arr[n/2:])
    
    if supermode2 == -1 and supermode1 >= 0:
        return supermode1
    
    elif supermode1 == -1 and supermode2 >= 0:
        return supermode2 
            
    elif supermode1 == supermode2:
        return supermode1
    
    else:                      
        return -1

arr=[4,4,5,6,7,4,4,4]
print (supermodediv(arr))    

#Supermode Using Decrease And Conquer
def supermodedec(array,Median):
    l=len(array)
    if(l>=Median):
        k=0
        count=1
        while(k<l and array[k]==array[k+1]):
            count=count+1
            k=k+1
            if(k==l-1):
                break
        if count >=Median:
            return(array[0])
        else:
            if(k<l-1):
                return supermodedec(array[k+1:],Median)
    else:
        return "No supermode"
            
arr=[4,4,5,6,7,4,4,4]
arr.sort()
print (supermodedec(arr,(len(arr)//2)+1)) 