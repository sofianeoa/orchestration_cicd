from calcules import Calculator

def main():
    a, b = 10, 5
    print(f"Addition: {Calculator.addition(a, b)}")
    print(f"Multiplication: {Calculator.multiplication(a, b)}")
    print(f"Division: {Calculator.division(a, b)}")
    print(f"Subtraction: {Calculator.subtraction(a, b)}")

if __name__ == "__main__":
    main()
