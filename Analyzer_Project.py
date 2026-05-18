import numpy as np

class DataAnalytics:

    def __init__(self):
        self.array = None

    def check_array(self):

        if self.array is None:
            print("\nPlease create an array first")
            return False

        return True

    def create_array(self):

        try:

            print("\nArray Creation:")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")

            choice = int(input("Enter your choice: "))

            if choice == 1:

                elements = input("\nEnter elements separated by space: ")
                self.array = np.array(elements.split(), dtype=int)

            elif choice == 2:

                rows = int(input("\nEnter number of rows: "))
                cols = int(input("Enter number of columns: "))
                total = rows * cols

                elements = input(f"Enter {total} elements separated by space: ")

                self.array = np.array(elements.split(), dtype=int).reshape(rows, cols)

            elif choice == 3:

                x = int(input("\nEnter number of blocks: "))
                y = int(input("Enter number of rows: "))
                z = int(input("Enter number of columns: "))

                total = x * y * z

                elements = input(f"Enter {total} elements separated by space: ")

                self.array = np.array(elements.split(), dtype=int).reshape(x, y, z)

            else:
                print("\nInvalid Choice")
                return

            print("\nArray Created Successfully:")
            print(self.array)

        except:
            print("\nInvalid Input")

    def indexing(self):

        try:

            if not self.check_array():
                return

            index = int(input("\nEnter index number: "))

            print("\nElement is:")
            print(self.array[index])

        except:
            print("\nInvalid Input")

    def slicing(self):

        try:

            if not self.check_array():
                return

            if self.array.ndim != 2:
                print("\nSlicing works for 2D arrays only")
                return

            row_range = input("\nEnter row range (start:end): ")
            col_range = input("Enter column range (start:end): ")

            row_start, row_end = map(int, row_range.split(":"))
            col_start, col_end = map(int, col_range.split(":"))

            sliced_array = self.array[row_start:row_end, col_start:col_end]

            print("\nSliced Array:")
            print(sliced_array)

        except:
            print("\nInvalid Input")

    def addition(self):

        try:

            if not self.check_array():
                return

            elements = input("\nEnter second array elements: ")

            second_array = np.array(elements.split(), dtype=int)

            second_array = second_array.reshape(self.array.shape)

            result = self.array + second_array

            print("\nAddition Result:")
            print(result)

        except:
            print("\nArray size must match")

    def subtraction(self):

        try:

            if not self.check_array():
                return

            elements = input("\nEnter second array elements: ")

            second_array = np.array(elements.split(), dtype=int)

            second_array = second_array.reshape(self.array.shape)

            result = self.array - second_array

            print("\nSubtraction Result:")
            print(result)

        except:
            print("\nArray size must match")

    def multiplication(self):

        try:

            if not self.check_array():
                return

            elements = input("\nEnter second array elements: ")

            second_array = np.array(elements.split(), dtype=int)

            second_array = second_array.reshape(self.array.shape)

            result = self.array * second_array

            print("\nMultiplication Result:")
            print(result)

        except:
            print("\nArray size must match")

    def division(self):

        try:

            if not self.check_array():
                return

            elements = input("\nEnter second array elements: ")

            second_array = np.array(elements.split(), dtype=int)

            second_array = second_array.reshape(self.array.shape)

            result = self.array / second_array

            print("\nDivision Result:")
            print(result)

        except:
            print("\nArray size must match")

    def combine_arrays(self):

        try:

            if not self.check_array():
                return

            elements = input("\nEnter another array elements: ")

            second_array = np.array(elements.split(), dtype=int)

            if self.array.ndim == 1:

                combined = np.concatenate((self.array, second_array))

            else:

                second_array = second_array.reshape(self.array.shape)

                combined = np.concatenate((self.array, second_array))

            print("\nCombined Array:")
            print(combined)

        except:
            print("\nArray size must match")

    def split_array(self):

        try:

            if not self.check_array():
                return

            sections = int(input("\nEnter number of parts: "))

            split_arrays = np.array_split(self.array, sections)

            print("\nSplit Arrays:")

            for i in split_arrays:
                print(i)

        except:
            print("\nInvalid Input")

    def search_value(self):

        try:

            if not self.check_array():
                return

            value = int(input("\nEnter value to search: "))

            if value in self.array:
                print("\nValue Found")

            else:
                print("\nValue Not Found")

        except:
            print("\nInvalid Input")

    def sort_array(self):

        try:

            if not self.check_array():
                return

            sorted_array = np.sort(self.array)

            print("\nSorted Array:")
            print(sorted_array)

        except:
            print("\nInvalid Input")

    def filter_array(self):

        try:

            if not self.check_array():
                return

            value = int(input("\nShow values greater than: "))

            filtered = self.array[self.array > value]

            print("\nFiltered Array:")
            print(filtered)

        except:
            print("\nInvalid Input")

    def array_sum(self):

        if not self.check_array():
            return

        print("\nSum:")
        print(np.sum(self.array))

    def array_mean(self):

        if not self.check_array():
            return

        print("\nMean:")
        print(np.mean(self.array))

    def array_median(self):

        if not self.check_array():
            return

        print("\nMedian:")
        print(np.median(self.array))

    def array_std(self):

        if not self.check_array():
            return

        print("\nStandard Deviation:")
        print(np.std(self.array))

    def array_variance(self):

        if not self.check_array():
            return

        print("\nVariance:")
        print(np.var(self.array))

obj = DataAnalytics()

while True:

    print("\n===== NUMPY ANALYZER =====")
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")

    try:
        main_choice = int(input("Enter your choice: "))

    except:
        print("\nPlease enter numbers only")
        continue

    if main_choice == 1:

        while True:

            print("\n--- ARRAY MANAGEMENT ---")
            print("1. Create Array")
            print("2. Indexing")
            print("3. Slicing")
            print("4. Go Back")

            try:
                choice = int(input("Enter your choice: "))

            except:
                print("\nPlease enter numbers only")
                continue

            if choice == 1:
                obj.create_array()

            elif choice == 2:
                obj.indexing()

            elif choice == 3:
                obj.slicing()

            elif choice == 4:
                break

            else:
                print("\nInvalid Choice")

    elif main_choice == 2:

        while True:

            print("\n--- MATHEMATICAL OPERATIONS ---")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Go Back")

            try:
                math_choice = int(input("Enter your choice: "))

            except:
                print("\nPlease enter numbers only")
                continue

            if math_choice == 1:
                obj.addition()

            elif math_choice == 2:
                obj.subtraction()

            elif math_choice == 3:
                obj.multiplication()

            elif math_choice == 4:
                obj.division()

            elif math_choice == 5:
                break

            else:
                print("\nInvalid Choice")

    elif main_choice == 3:

        while True:

            print("\n--- COMBINE OR SPLIT ARRAYS ---")
            print("1. Combine Arrays")
            print("2. Split Array")
            print("3. Go Back")

            try:
                combine_choice = int(input("Enter your choice: "))

            except:
                print("\nPlease enter numbers only")
                continue

            if combine_choice == 1:
                obj.combine_arrays()

            elif combine_choice == 2:
                obj.split_array()

            elif combine_choice == 3:
                break

            else:
                print("\nInvalid Choice")

    elif main_choice == 4:

        while True:

            print("\n--- SEARCH, SORT, FILTER ---")
            print("1. Search a Value")
            print("2. Sort Array")
            print("3. Filter Array")
            print("4. Go Back")

            try:
                search_choice = int(input("Enter your choice: "))

            except:
                print("\nPlease enter numbers only")
                continue

            if search_choice == 1:
                obj.search_value()

            elif search_choice == 2:
                obj.sort_array()

            elif search_choice == 3:
                obj.filter_array()

            elif search_choice == 4:
                break

            else:
                print("\nInvalid Choice")

    elif main_choice == 5:

        while True:

            print("\n--- AGGREGATES AND STATISTICS ---")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Go Back")

            try:
                stats_choice = int(input("Enter your choice: "))

            except:
                print("\nPlease enter numbers only")
                continue

            if stats_choice == 1:
                obj.array_sum()

            elif stats_choice == 2:
                obj.array_mean()

            elif stats_choice == 3:
                obj.array_median()

            elif stats_choice == 4:
                obj.array_std()

            elif stats_choice == 5:
                obj.array_variance()

            elif stats_choice == 6:
                break

            else:
                print("\nInvalid Choice")

    elif main_choice == 6:

        print("\nThank You For Using NumPy Analyzer!")
        break

    else:
        print("\nInvalid Choice")