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
            18: "\033[48;5;237m    \033[0m",  # Add the missing key for 18
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

    def merge_list(self, a, b):
        """Merges two sorted lists into a single sorted list."""
        out = []
        while a and b:
            if a[0] < b[0]:
                out.append(a.pop(0))
            else:
                out.append(b.pop(0))
        out.extend(a)
        out.extend(b)
        return out

    def strand(self, a):
        """Forms a strand from the input list."""
        s = [a.pop(0)]
        i = 0
        while i < len(a):
            if a[i] > s[-1]:
                s.append(a.pop(i))
            else:
                i += 1
        return s

    def strand_sort(self, a):
        """Sorts the input list using the strand sort algorithm."""
        out = self.strand(a)
        while a:
            #print("\nIteration:")  # Mark the beginning of each iteration
            #time.sleep(0.1)
            #self.print_square(a)  # Print the current state of 'a'
            out = self.merge_list(out, self.strand(a))
            #self.print_square(a)  # Print the current state of 'a'
            self.print_square(out)  # Print the result after merging
            time.sleep(0.1)
        return out

sorter = Sorting()

color_blocks = [22, 18, 16, 6, 20, 10, 5, 23, 21, 14, 7, 2, 9, 1, 16, 0, 11, 15, 13, 4, 19, 8, 3, 12, 17]

start_time = time.time()
sorted_blocks = sorter.strand_sort(color_blocks)
end_time = time.time()
#sorter.print_square(sorted_blocks)


print(f"{end_time - start_time:.4f} seconds")
