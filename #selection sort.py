#selection sort 
# create a function 
def selectingS(lyst):
    index = 0                               # the iteration will search on all the list
    while index < len(lyst)-1:              # we assume that the last number is the maximum value left 
        minI = index                        #to keep the original item amd save its value
        j = index +1                        # comparing iteration 
        while j < len(lyst):
           if lyst[j] < lyst[index]:        #if the item in j is less than the index then it is the minimum and recompar it to the other 

            minI = j
        j+=1
        if minI != index :                  # if the item is with the minimum  index does not equal the the current index the we swap 
            lyst[minI],lyst[index] =  lyst[index], lyst[minI]
    return lyst

def bubble (lyst):
   #index = 0
   sorte = False                         #a way to exit the loop when the sorting is done


   while not sorte:                     #while true we will go tthoght all the items of the list 
       sorte = True
       for i in range(0,len(lyst)-1):   # do the comparesm on all the idex of the lyst
         
        if lyst[i]> lyst[i+1]:       
           sorte = False                #to stop the repeating the comparing
           lyst[i],lyst[i+1] = lyst[i+1],lyst[i]    #swap the items
   return lyst                                       #get the loop 


def insrtion (lyst):
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = itemToInsert
        i += 1
    return lyst
# the quick sort depends in chosing pivot poin then devid the list into two sublist greater and lower then redo it again until the sequence become less thar one 

def quick (lyst):
   lenght = len(lyst)
   
   if lenght <= 1:
      return lyst
   else:
      pivot = lyst.pop()        # delet and return the last value 

      Lgeater = []
      Llower =[]

      for i in lyst:
         if i > pivot:
            Lgeater.append(i)
         else:
            Llower.append(i)

   return quick(Llower)+ [pivot] + quick(Lgeater)   

def quick_insertion(lyst):
   if len(lyst)<50:
      insrtion(lyst)
   else:
      quick(lyst)
   return lyst



import time
import random
sizes = [50, 500, 5000]
results = {}
for size in sizes:
 arr = [random.randint(0, 10000) for _ in range(size)]
 start_time = time.time()
 quick(arr.copy())
 end_time = time.time()
 quicksort_time = end_time - start_time
 start_time = time.time()
 quick_insertion(arr.copy())
 end_time = time.time()
 hybrid_quicksort_time = end_time - start_time

 results[size] = {'quicksort_time': quicksort_time, 'hybrid_quicksort_time': hybrid_quicksort_time}
print(results)


# a = [6,3,1,9,10,7]
# print(insrtion(a))