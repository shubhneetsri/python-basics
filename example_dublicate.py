def containsDuplicate(listitems):

    seen = {}
    dublicate = {}

    for val in listitems:
        if val in seen:
            dublicate[val] += 1
        else:
            dublicate[val] = False
            seen[val] = True 
    
    return dublicate

nums = [1, 2, 3, 1]
print(containsDuplicate(nums))  # Output: True

