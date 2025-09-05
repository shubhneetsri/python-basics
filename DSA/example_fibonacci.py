previous_val = 0
next_val = 1
for i in range(0,1000):
    print(previous_val)
    current_val = previous_val + next_val
    previous_val = next_val
    next_val = current_val