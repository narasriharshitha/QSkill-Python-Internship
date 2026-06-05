import numpy as np

def get_matrix(name):
    print(f"\nEnter matrix {name}:")
    rows = int(input("  Number of rows: "))
    cols = int(input("  Number of columns: "))
    print(f"  Enter values row by row (space between numbers):")
    data = []
    for i in range(rows):
        row = list(map(float, input(f"  Row {i+1}: ").split()))
        data.append(row)
    return np.array(data)

def print_matrix(label, matrix):
    print(f"\n{label}:")
    print("-" * 35)
    for row in matrix:
        print("  " + "  ".join(f"{v:8.2f}" for v in row))
    print("-" * 35)

def main():
    print("=" * 40)
    print("   MATRIX OPERATIONS TOOL")
    print("   QSkill Python Internship")
    print("   Built with Python + NumPy")
    print("=" * 40)

    while True:
        print("\n--- MENU ---")
        print("1. Addition       (A + B)")
        print("2. Subtraction    (A - B)")
        print("3. Multiplication (A x B)")
        print("4. Transpose      (flip A)")
        print("5. Determinant    (value of A)")
        print("6. Exit")
        choice = input("\nChoose an option (1-6): ").strip()

        if choice in ['1', '2', '3']:
            A = get_matrix('A')
            B = get_matrix('B')
            print_matrix("Matrix A", A)
            print_matrix("Matrix B", B)
            try:
                if choice == '1':
                    result = np.add(A, B)
                    print_matrix("Result (A + B)", result)
                elif choice == '2':
                    result = np.subtract(A, B)
                    print_matrix("Result (A - B)", result)
                elif choice == '3':
                    result = np.matmul(A, B)
                    print_matrix("Result (A x B)", result)
            except ValueError as e:
                print(f"\nError: Matrices are not compatible!")
                print("Tip: For add/subtract, both must be same size.")
                print("For multiply, columns of A must equal rows of B.")

        elif choice == '4':
            A = get_matrix('A')
            print_matrix("Original Matrix A", A)
            print_matrix("Transpose of A", A.T)

        elif choice == '5':
            A = get_matrix('A')
            print_matrix("Matrix A", A)
            if A.shape[0] != A.shape[1]:
                print("\nError: Determinant needs a square matrix (2x2, 3x3 etc.)")
            else:
                det = np.linalg.det(A)
                print(f"\nDeterminant of A = {det:.4f}")

        elif choice == '6':
            print("\nThank you for using Matrix Operations Tool!")
            print("QSkill Python Internship - Task 3 Complete!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()
