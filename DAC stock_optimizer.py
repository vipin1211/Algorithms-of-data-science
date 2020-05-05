
# Author : Vipin Amar Vivekanandan

import pandas as pd

#function that finds the best stock on the crossing subarray
def MSS_cross(a, low, mid, high):
    maxLeft2Center = -100000000
    left2Center = 0
    #iterating through the left half of the crossing subarray
    for i in range(mid, low-1, -1):
        left2Center += a[i]
        # Keeping track of the best sum so far and its index
        if left2Center > maxLeft2Center:
            maxLeft2Center = left2Center
            max_left = i
    maxRight2Center = -100000000
    right2Center = 0
    #iterating through the right half of the crossing subarray
    for j in range(mid+1, high+1):
        right2Center += a[j]
        # Keeping track of the best sum so far and its index
        if right2Center > maxRight2Center:
            maxRight2Center = right2Center
            max_right = j
    return (max_left, max_right, maxLeft2Center+maxRight2Center)

#function that finds the best stock on the left and right subarray
def MSSDAC(a,low=0,high=None):                                  
    if high==None:
        high=len(a)-1
    # base case
    if low == high:  
        return (low, high, a[low])
    else:
        #Divide
        mid = (low+high)//2
        #Conquer- Finds the starting and ending index of the left right and the crossing subarray along with their best profits
        left_start, left_end, left_sum = MSSDAC(a, low, mid)
        right_start, right_end, right_sum = MSSDAC(a, mid+1, high)
        cross_start, cross_end, cross_sum = MSS_cross(a, low, mid, high)
        #Combine -Checks which subarray has the best profit and returns that along with its starting and ending index
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_start, left_end, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_start, right_end, right_sum)
        else:
            return (cross_start, cross_end, cross_sum)
        
#Function that finds the best date to buy and sell stocks of various companies for optimal profits 
def stock_optimizer(stocks,security):
    df1 = pd.read_csv(f"{stocks}")
    df2 = pd.read_csv(f"{security}")
    for i in df1["symbol"].unique():
        #finding out the closing dates of stocks for a particular ticker symbol
        arr=df1.loc[df1["symbol"] == i,['close','date']]
        #finding out the respective company name
        company=df2.iloc[df2.loc[df2["Ticker symbol"] == i].index[0]]['Security']
        changes=[]
        #Calculating the change in stock prices at the closing dates for every company and calculating max profit 
        for j in range(len(arr)-1):
            diff=arr.iloc[j+1][0]-arr.iloc[j][0]
            changes.append(diff)
        m = MSSDAC(changes)
        print(f'Best stock to buy:"{company}" on {arr.iloc[m[0]][1]} and sell on {arr.iloc[m[1]+1][1]} with profit of {m[2]}')

#Test Code        
stock_optimizer("prices-split-adjusted.csv","securities.csv")