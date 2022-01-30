#new code from HWH server

import array

arr = array.array('i',[1, 2, 4, 3, 1, 7, 2, 2, 1, 1]) # Array for testing

def remove_duplicate(user_array): # function to remove duplicate in an array
  
  import array

  new_array = array.array('i',[]) # create a new empty array

  for k in user_array: # for each item in the array
    
    if k not in new_array: # if this item is not in the new array
    
      new_array.append(k) # add it in the new array

    
    print(new_array,'test array, when the for loop is running') #this is to show how the for loop works

  
  print (new_array,"filtered final array") # display the filtered array


remove_duplicate(arr)