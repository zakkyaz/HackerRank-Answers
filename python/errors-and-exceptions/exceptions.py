import sys

lines = [line.strip() for line in sys.stdin]
    
for i in range(1, len(lines)):
    try:
        num1, num2 = map(int, lines[i].split())
        print(num1 // num2)
    except ZeroDivisionError as zde:
        print(f"Error Code: {zde.args[0]}")
    except ValueError as ve:
        print(f"Error Code: {ve.args[0]}")
