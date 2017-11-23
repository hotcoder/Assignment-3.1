'''
Created on Nov 21, 2017

@author: z002krv
'''
'''
Custom Filter and Reduce function implementations
'''

def myfilter(functionToApply , sourceList):
    resultList =  []
    try:
        itr = iter(sourceList)
    except TypeError:
        print("Please provide sourceList of type iterable only")
        
    for element in sourceList:
        if(functionToApply(element)):
            resultList.append(element)
    return resultList
            
print(myfilter(lambda x: x%2==0 , [1,2,3,4,5,6]))

###########################################################
print("#"*20)

def myreduce(functionToApply,sourceList,init=0):
    result = init
    for s in sourceList:
        result = functionToApply(result,s);
    return result
        
print(myreduce(lambda x,y:x+y,[10,2,3,4,5,6]))

def findMax(x,y):
    if(x>y):
        return x
    else:
        return y


print(myreduce(findMax,[10,2,3,4,5,6]))

###########################################################
print("#"*20)



        