import sys

def main(a, b):
    print(f"Sum: {a + b}")
    print(f"Multiply: {a * b}")
    print(f"Subtract: {a - b}")
    print(f"Divide: {a / b}")
    print(f"Remainder: {a % b}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please provide two numbers.")
    else:
        main(float(sys.argv[1]), float(sys.argv[2]))
1 21
