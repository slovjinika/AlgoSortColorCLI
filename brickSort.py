import time

class Sorting:

    def print_square(self, arr):
        block_chars = {
            0: "\033[48;5;255m    \033[0m",
            1: "\033[48;5;254m    \033[0m",
            2: "\033[48;5;253m    \033[0m",
            3: "\033[48;5;252m    \033[0m",
            4: "\033[48;5;251m    \033[0m",
            5: "\033[48;5;250m    \033[0m",
            6: "\033[48;5;249m    \033[0m",
            7: "\033[48;5;248m    \033[0m",
            8: "\033[48;5;247m    \033[0m",
            9: "\033[48;5;246m    \033[0m",
            10: "\033[48;5;245m    \033[0m",
            11: "\033[48;5;244m    \033[0m",
            12: "\033[48;5;243m    \033[0m",
            13: "\033[48;5;242m    \033[0m",
            14: "\033[48;5;241m    \033[0m",
            15: "\033[48;5;240m    \033[0m",
            16: "\033[48;5;239m    \033[0m",
            17: "\033[48;5;238m    \033[0m",
            18: "\033[48;5;237m    \033[0m",
            19: "\033[48;5;236m    \033[0m",
            20: "\033[48;5;235m    \033[0m",
            21: "\033[48;5;234m    \033[0m",
            22: "\033[48;5;233m    \033[0m",
            23: "\033[48;5;232m    \033[0m",
        }

        row_size = 25  # Fixed size for rows
        col_size = 1  # Fixed size for columns

        # Pad the array if it's shorter than 25 elements
        arr = arr + [0] * (row_size - len(arr))  # Add 0s to reach 25 elements

        for i in range(col_size):
            row = "".join([block_chars[arr[i + j * col_size]] for j in range(row_size)])
            print(row + "")  # Add \n for a new line after each row

    def brickSort(self, arr):
        """Sorts an array using a brick sort algorithm."""
        n = len(arr)
        isSorted = False
        while not isSorted:
            #print("\nIteration:")
            self.print_square(arr)  # Print the array at the start of each iteration
            time.sleep(0.1)
            isSorted = True
            for i in range(1, n, 2):
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                    isSorted = False
            for i in range(2, n, 2):  
                if i < n and arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                    isSorted = False
        return arr

sorter = Sorting()

color_blocks = [22, 18, 16, 6, 20, 10, 5, 23, 21, 14, 7, 2, 9, 1, 16, 0, 11, 15, 13, 4, 19, 8, 3, 12, 17]

start_time = time.time()
sorted_blocks = sorter.brickSort(color_blocks)
end_time = time.time()
print(f"{end_time - start_time:.4f} seconds")
#sorter.print_square(sorted_blocks)
