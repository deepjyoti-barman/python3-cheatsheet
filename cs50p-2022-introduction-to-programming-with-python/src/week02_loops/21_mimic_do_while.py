# A do-while loop runs at least once, then checks the condition
# We can mimic a do-while loop in Python using a while True loop with a break condition
count = 1

while True:
    print(count)
    count += 1

    if count > 5:
        break
