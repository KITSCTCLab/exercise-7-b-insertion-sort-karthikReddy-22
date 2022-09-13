from typing import List

def insertionSort(array) -> List[int]:
    for n in range(1,len(array)):
        key = array[n]
        num = n-1
        while num >= 0 and key < array[num]:
            array[num + 1] = array[num]
            num -= 1
        array[num + 1] = key
    return array
# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
