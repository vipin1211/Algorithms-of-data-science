
# Author : Vipin Amar Vivekanandan

'''
Here I will be using Dynamic Programming to to determine which metro areas to purchase house in assume we can only buy a single house in each city. 
We are given 1 million dollars to spend. Our DP algorithm should tell us how much estimated profit we will make, along with
a list of the city names of our purchases.

Since 1 million dollars will create a table with one huge dimension and houses usually aren’t bought
down to the dollar, we will add a variable to our function that tell the smallest increment the dollar amount can have.
'''

def optimizeInvestments(names,weight,value,avail_weight,step):
    # create a matrix of length equal to step size keeping in account the total
    #weight available to store the optimal profit 
    profit=[[0 for i in range(((avail_weight)//step)+1) ] for j in range(len(value)+1)] 
    # create a matrix of length equal to step size keeping in account the 
    #total weight available to store keep track of the optimal choices
    traceback=[['NOT IN' for i in range(((avail_weight)//step)+1) ] for j in range(len(value)+1)]
    for i in range(1,len(value)+1):
        l=0
        # for every unit weight 
        for j in range(((avail_weight)//step)+1):
            # if the weight of the commodity is less than the total weight record that
            if weight[i-1]>l:
                profit[i][j]=profit[i-1][j]
            # else the profit would be the max of the best profit for the available weight
            # or the sum of the value of the current commodity and the best profit for the 
            # available weight without the current commodity. 
            else:
                profit[i][j]=max(profit[i-1][j],value[i-1]+profit[i-1][j-(weight[i-1]//step)])
                # keep track of which commodity returned the best profit at that time
                if profit[i][j]==value[i-1]+profit[i-1][j-(weight[i-1]//step)]:
                    traceback[i][j]='IN'
            l+=step            
    #tracking back the commodity chosen an every stage.        
    items=[]
    j=avail_weight//step
    for i in range(len(value),0,-1):
        if traceback[i][j]=='IN':
            items.append(names[i-1])
            j-=weight[i-1]//step
    print(f"The best places to buy : {items} The max profit to be made : ${profit[len(value)][avail_weight//step]}")
    
import pandas as pd
df = pd.read_csv("Metro.csv")

value=df['2020-01'].sub(df['2019-01'], axis = 0).tolist()
weight=df['2020-01'].tolist()
names=df['RegionName'].tolist()

#Test Code :
optimizeInvestments(names,weight,value,1000000,1000)