import numpy as np

def input_matrix():
    rows=int(input("enter the no of rows"))
    cols=int(input("enter the no of col"))

    matrix=[]

    for i in range(rows):
        row=list(map(int,input(f"enter row {i+1}:").split()))
        matrix.append(row)

    return np.array(matrix)


while True:
    print("\n=== Matrix Operations Tool ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")

    choice = int(input("Enter your choice: "))



    if choice == 1:
        print("Enter Matrix A:")
        A = input_matrix()

        print("Enter Matrix B:")
        B = input_matrix()

        result = np.add(A, B)
        print("Result:\n", result)

    elif choice == 2:
        print("Enter Matrix A:")
        A = input_matrix()

        print("Enter Matrix B:")
        B = input_matrix()

        result = np.subtract(A, B)
        print("Result:\n", result)

    elif choice == 3:
        print("Enter Matrix A:")
        A = input_matrix()

        print("Enter Matrix B:")
        B = input_matrix()

        result = np.dot(A,B)
        print("Result:\n", result)
    elif choice == 4:
        print("enter the matrix")
        A = input_matrix()

        result=np.transpose(A)
        print("Result:\n", result)
        
    elif choice == 5:
        print("Enter Matrix:")
        A = input_matrix()

        if A.shape[0] != A.shape[1]:
            print("❌ Determinant only for square matrix")
        else:
            result = np.linalg.det(A)
            print("Determinant:", result)
        
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("❌ Invalid choice")

