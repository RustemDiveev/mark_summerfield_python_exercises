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
print("count =", len(numbers) + 1, "sum =", sum, "lowest =", min, "highest =", max, "mean =", sum / (len(numbers) + 1))



