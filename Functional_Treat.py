print("""Welcome to the Data Analyzer and Transformer Program.
Main Menu:
1. Input Data
2. Display Data Summary
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold(Lambda Function)
5. Sort Data
6. Display Dataset Statistics(Return Multiple Values)
7. Exit Program""")
while True:
    choice=int(input("Please enter your choice: "))
    match choice:
        case 1:
            def built_in(arr):
                print("Length:", len(arr))
                print("Sum:", sum(arr))
                print("Minimum", min(arr))
                print("Maximum", max(arr))
            data=[10, 20, 30, 40, 50]
            built_in(data)
        
        case 2:
                
            def average(arr):
                avg=sum(arr)/len(arr)
                return avg
                
            def duplicates(arr):
                dup=[]
                for i in arr:
                    if arr.count(i)>1:
                        if i not in dup:
                            dup.append(i)
                return dup
                
            def value(arr):
                unique=[]
                for i in arr:
                    if i not in unique:
                        unique.append(i)
                return unique
            data=[10,30,50,50,70,50,30,20,40,25]
            print("Average:", average(data))
            print("Duplicates:", duplicates(data))
            print("Values:", value(data))
        
        case 3:
            def factorial(n):
                if n==1:
                    return 1
                return n*factorial(n-1)
            num=int(input("Enter a number to calculate its factorial: "))
            result=factorial(num)
            print("Factorial of", num, "is:", result)
        case 4:
            data=[20,35,50,56,78,90]
            print("Enter a threshold value to filter out data above this value:")
            limit=int(input())
            result=list(filter(lambda x: x>limit,data))
            
            print("\nFiltered Data (values >= ", limit, "):")
            print(*result, sep=", ")
            
            mapped=list(map(lambda x: x*2, data))
            print("\nData after applying map(each value*2):")
            print(*mapped, sep=", ")
            
        case 5:
            data = [56, 21, 78, 12, 90, 34, 43]
            print("Choose sorting option:")
            print("1. Ascending")
            print("2. Descending")
            
            choice=int(input("Enter your choice: "))
            
            if choice==1:
                data.sort()
                print("Sorted in Ascending Order:", data)
            elif choice==2:
                data.sort(reverse=True)
                print("Sorted in Descending Order:", data)
            else:
                print("Invalid Choice")
            
        case 6:
            def built_in(arr):
                avg=sum(arr)/len(arr)
                print("Minimum", min(arr))
                print("Maximum", max(arr))
                print("Sum:", sum(arr))
                print("Average:", avg)
            data=[10, 20, 30, 40, 50]
            built_in(data)
            
        case 7:
            print("Thank You! for using the Data Analyzer and Transformer Program. Goodbye!")
            
            break