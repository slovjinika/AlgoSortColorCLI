import time
import random
import math

#print("\033[2J")

class Sorting:

    def bubbleSort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.print_square(arr)
                    time.sleep(0.1)
                    #print("\033[2J")
        return arr

    def selectionSort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            self.print_square(arr)  # Предполагаем, что у вас есть функция print_square
            time.sleep(0.1)
        return arr


    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            self.print_square(arr)
            time.sleep(0.1)
        return arr

    def shellSort(self, arr):
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
            self.print_square(arr)
            time.sleep(0.1)
        return arr


    def pigeonHoleSort(self, arr):
        my_min = min(arr)
        my_max = max(arr)
        size = my_max - my_min + 1
        holes = [0] * size
        for x in arr:
            assert type(x) is int, "integers only please"
            holes[x - my_min] += 1
        i = 0
        for count in range(size):
            while holes[count] > 0:
                holes[count] -= 1
                arr[i] = count + my_min
                i += 1
            self.print_square(arr)
            time.sleep(0.1)
        return arr




    def heapify(self, arr, n, i):
        largest = i # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i] # swap
            self.heapify(arr, n, largest)

    def heapSort(self, arr):
        n = len(arr)
        # Build a max heap.
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
        # One by one extract elements from the heap
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            self.heapify(arr, i, 0)
            self.print_square(arr)
            time.sleep(0.1)
        return arr

    # Gnome Sort
    def gnomeSort(self, arr):
        index = 0
        n = len(arr)
        while index < n:
            if index == 0:
                index = index + 1
            if arr[index] >= arr[index - 1]:
                index = index + 1
            else:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                index = index - 1
            self.print_square(arr)
            time.sleep(0.1)
        return arr

    def stoogeSort(self, arr, l, h):
        if l >= h:
            return
        if arr[l] > arr[h]:
            arr[l], arr[h] = arr[h], arr[l]
            self.print_square(arr)
            time.sleep(0.1)
        if h - l > 1:
            t = int((h - l + 1) / 3)
            self.stoogeSort(arr, l, h - t)
            self.stoogeSort(arr, l + t, h)
            self.stoogeSort(arr, l, h - t)


    def pancakeSort(self, arr):
        curr_size = len(arr)
        while curr_size > 1:
            mi = self.findMax(arr, curr_size)
            if mi != curr_size - 1:
                self.flip(arr, mi)
                self.print_square(arr)  # Added print_square
                time.sleep(0.1)        # Added sleep
                self.flip(arr, curr_size - 1)
                self.print_square(arr)  # Added print_square
                time.sleep(0.1)        # Added sleep
            curr_size -= 1
        return arr





    def bogoSort(self, arr):
        n = len(arr)
        while (self.is_sorted(arr) == False):
            self.shuffle(arr)
            # self.print_square(arr)  # Add print_square if needed
            # time.sleep(0.1)          # Add sleep if needed
        return arr

    def is_sorted(self, arr):
        n = len(arr)
        for i in range(0, n - 1):
            if (arr[i] > arr[i + 1]):
                return False
        return True

    def shuffle(self, arr):
        n = len(arr)
        for i in range(0, n):
            r = random.randint(0, n - 1)
            arr[i], arr[r] = arr[r], arr[i]


    def quickSort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)
            self.print_square(arr)  # Assuming you have a print_square function
            time.sleep(0.1)
        return arr

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.print_square(arr)  # Assuming you have a print_square function
                time.sleep(0.1)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.print_square(arr)  # Assuming you have a print_square function
        time.sleep(0.1)
        return i + 1

    def cocktailSort(self, arr):
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1
        while swapped == True:
            swapped = False
            for i in range(start, end):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
                    self.print_square(arr)  # Assuming you have a print_square function
                    time.sleep(0.1)
            if swapped == False:
                break
            swapped = False
            end = end - 1
            for i in range(end - 1, start - 1, -1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
                    self.print_square(arr)  # Assuming you have a print_square function
                    time.sleep(0.1)
            start = start + 1
        return arr

    def brickSort(self, arr):
        n = len(arr)
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, n, 2):
                if arr[i] < arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
                    swapped = True
                    self.print_square(arr)  # Assuming you have a print_square function
                    time.sleep(0.1)
            for i in range(2, n-1, 2):
                if arr[i] < arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
                    swapped = True
                    self.print_square(arr)  # Assuming you have a print_square function
                    time.sleep(0.1)
        return arr


    def radixSort(self, arr):
        max_element = max(arr)  # Find the largest element
        exp = 1
        while max_element // exp > 0:
            self.countSort(arr, exp)
            exp *= 10
            self.print_square(arr)  # Assuming you have a print_square function
            time.sleep(0.1)
        return arr

    def countSort(self, arr, exp):
        n = len(arr)
        output = [0] * n  # Create an output array
        count = [0] * 10  # Create a count array for digits 0-9

        # Count occurrences of each digit at the current exponent place
        for i in range(0, n):
            index = (arr[i] // exp) % 10
            count[index] += 1

        # Modify count array to store cumulative counts
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array in sorted order
        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1

        # Copy the sorted elements back to the original array
        for i in range(0, n):
            arr[i] = output[i]
            self.print_square(arr)  # Assuming you have a print_square function
            time.sleep(0.1)

    def combSort(self, arr):
        n = len(arr)
        gap = n
        shrink_factor = 1.3
        swapped = True
        while gap > 1 or swapped:
            gap = max(1, int(gap / shrink_factor))
            swapped = False
            for i in range(0, n - gap):
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    swapped = True
                    self.print_square(arr)  # Assuming you have a print_square function
                    time.sleep(0.1)
        return arr

    def cycleSort(self, arr):
        n = len(arr)
        for cycle_start in range(n - 1):
            item = arr[cycle_start]
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1
            if pos == cycle_start:
                continue

            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
            self.print_square(arr)  # Assuming you have a print_square function
            time.sleep(0.1)

            while pos != cycle_start:
                pos = cycle_start
                for i in range(cycle_start + 1, n):
                    if arr[i] < item:
                        pos += 1
                while item == arr[pos]:
                    pos += 1
                arr[pos], item = item, arr[pos]
                self.print_square(arr)  # Assuming you have a print_square function
                time.sleep(0.1)
        return arr


    def merge_lists(self, list1, list2):
        result = []
        while list1 and list2:
            if list1[0] < list2[0]:
                result.append(list1.pop(0))
            else:
                result.append(list2.pop(0))
        result += list1
        result += list2
        return result


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

        for i in range(col_size):
            row = "".join([block_chars[arr[i + j * col_size]] for j in range(row_size)])
            print(row + "")  # Add \n for a new line after each row

sorter = Sorting()

color_blocks = [22, 18, 16, 6, 20, 10, 5, 23, 21, 14, 7, 2, 9, 1, 16, 0, 11, 15, 13, 4, 19, 8, 3, 12, 17]

start_time = time.time()
#sorted_blocks = sorter.bubbleSort(color_blocks)
#sorted_blocks = sorter.selectionSort(color_blocks)
#sorted_blocks = sorter.insertionSort(color_blocks)
#sorted_blocks = sorter.shellSort(color_blocks)
#sorted_blocks = sorter.pigeonHoleSort(color_blocks)
#sorted_blocks = sorter.heapSort(color_blocks)
#sorted_blocks = sorter.gnomeSort(color_blocks)
#sorted_blocks = sorter.stoogeSort(color_blocks, 0, len(color_blocks)-1)
#sorted_blocks = sorter.pancakeSort(color_blocks)
#sorted_blocks = sorter.bogoSort(color_blocks)
#sorted_blocks = sorter.quickSort(color_blocks, 0, len(color_blocks) - 1)
#sorted_blocks = sorter.cocktailSort(color_blocks)
#sorted_blocks = sorter.radixSort(color_blocks)
#sorted_blocks = sorter.combSort(color_blocks)
sorted_blocks = sorter.cycleSort(color_blocks)
end_time = time.time()

elapsed_time = end_time - start_time

if elapsed_time >= 60:
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"{minutes} minutes {seconds} seconds")
else:
    print(f"{elapsed_time:.2f} seconds")
