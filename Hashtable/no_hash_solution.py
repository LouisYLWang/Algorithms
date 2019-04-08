from bisect import * ## https://docs.python.org/2/library/bisect.html

file = open("2sum.txt")
lines = file.readlines()
array = [int(line) for line in lines]
array.sort()
sum_values = set()


if __name__ == "__main__":
    for i in array:
        upper_bound = bisect_right(array, 10000 - i)
        lower_bound = bisect_left(array, -10000 - i)
        if array[lower_bound:upper_bound] != []:
            for j in array[lower_bound:upper_bound]:
                if i!=j:
                    sum_values.add(i+j)

print(len(sum_values))

