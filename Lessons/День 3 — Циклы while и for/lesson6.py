for i in range(5):
    print(i)

# range(5)      # 0, 1, 2, 3, 4
# range(1, 6)   # 1, 2, 3, 4, 5
# range(0, 10, 2) # 0, 2, 4, 6, 8 — каждый второй

for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} - чётное")
    else:
        print(f"{i} - нечётное")