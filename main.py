
  #Describe the solution in your own words
    # 1. loop trough the list of nums
    # 2. check if with the position of the number is less then its predeccessor
    # 3. if so then this is the answer
    # 4. else we will just increment the position.
def count_rotations_linear(nums):
    position = 0                 # What is the intial value of position?
    
    while position<len(nums):                     # When should the loop be terminated?
        
        # Success criteria: check whether the number at the current position is smaller than the one before it
        if position > 0 and nums[position]<nums[position-1]:   # How to perform the check?
            return position
        
        # Move to the next position
        position += 1
    
    return 0   
print(count_rotations_linear([15, 18, 2, 3, 6, 12]))  # Expected: 2
print(count_rotations_linear([7, 9, 11, 12, 5]))      # Expected: 4
print(count_rotations_linear([1, 2, 3, 4, 5]))        # Expected: 0 (not rotated)
               # Expected: 0 
