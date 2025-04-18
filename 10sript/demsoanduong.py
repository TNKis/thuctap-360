lst = [-1, 0, 5, -3, 2]
pos = sum(1 for x in lst if x > 0)
neg = sum(1 for x in lst if x < 0)
zero = lst.count(0)
print(f"Số dương: {pos}, Số âm: {neg}, Số 0: {zero}")
