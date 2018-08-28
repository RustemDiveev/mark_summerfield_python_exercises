#Define variables
numbers = []
sum = 0
min = 0
max = 0

#On Windows - press ctrl + z to finish and raise EOFError
while True:
  try:
      print("Enter a number or ctrl+z to finish: ")
      line = input()
      if line:
          number = int(line)
          sum += number
          if min == 0 or min <= number:
              min = number
          if max == 0 or max >= number:
              max = number 
          list.append(numbers, number)
  except ValueError as err:
      print(err)
      continue
  except EOFError:
      break

print(numbers)

i = 0 
while i < len(numbers):
    j = i + 1
    while i < j < len(numbers):
        if numbers[i] > numbers[j]:
            x = numbers[j]
            numbers[j] = numbers[i]
            numbers[i] = x
        #print("x =", x, "numbers[i] =", numbers[i], "numbers[j] =", numbers[j])
        #print("array:", numbers)
        #print("result:", i, j)
        j += 1
    i += 1

if int(len(numbers) / 2) - (len(numbers) / 2) == 0:
    median = int(len(numbers) / 2) - 1
    median = float((numbers[median] + numbers[median + 1]) / 2)
else:
    median = numbers[int((len(numbers)) / 2)]


print(numbers)
print("count =", len(numbers) + 1, "sum =", sum, "lowest =", min, "highest =", 
max, "mean =", sum / (len(numbers) + 1), "median =", median)



