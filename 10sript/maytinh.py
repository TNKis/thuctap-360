a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
op = input("Chọn phép toán (+ - * /): ")

if op == '+': print(a + b)
elif op == '-': print(a - b)
elif op == '*': print(a * b)
elif op == '/': print(a / b)
else: print("Phép toán không hợp lệ")
