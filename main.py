def Hexal(num):
  hexal = []
  while num > 0:
    hexal.append(num % 16)
    num = int(num / 16)
  hexal.reverse()
  Condition = False
  for i in hexal:
    if i > 9:
      Condition = True
    else:
      pass
  if Condition == True:
    for i in range(len(hexal)):
      if hexal[i] == 10:
        hexal[i] = "A"
      if hexal[i] == 11:
        hexal[i] = "B"
      if hexal[i] == 12:
        hexal[i] = "C"
      if hexal[i] == 13:
        hexal[i] = "D"
      if hexal[i] == 14:
        hexal[i] = "E"
      if hexal[i] == 15:
        hexal[i] = "F"
  global hexal_result
  hexal_result = " "
  a = [x for x in hexal]
  for i in a:
    hexal_result += str(i)


def Octal(num):
  octal = []
  temp2 = num
  while temp2 > 0:
    octal.append(temp2 % 8)
    temp2 = int(temp2 / 8)
  octal.reverse()
  global octal_result
  octal_result = " "
  a = [x for x in octal]
  for i in a:
    octal_result += str(i)
  Hexal(num)


def Binary(num):
  temp1 = num
  binary = []
  while temp1 > 0:
    binary.append(temp1 % 2)
    temp1 = int(temp1 / 2)
  binary.reverse()
  global binary_result
  binary_result = " "
  a = [x for x in binary]
  for i in a:
    binary_result += str(i)
  Octal(num)


def Conversion(num):
  if num < 0:
    print("abhi itna hi bna h\nplease enter only num greater than 0")
  elif num == 0:
    print(" Answer = 0")
  else:
    Binary(num)
  return


n = int(input("enter the no. of conversion you want to do : "))
for i in range(n):
  num = int(input("enter the %d number in base 10 : " % (i)))
Conversion(num)
# w="Decimal"
# x="Binary"
# y="Octal"
# z="Hexadecimal"
# print(f"{w} {x} {y} {z}")
# print(num,f"{binary_result} {octal_result} {hexal_result}")
from prettytable import PrettyTable

myTable = PrettyTable(["Decimal", "Binary", "Octal", "Hexadecimal"])
myTable.add_row([num, binary_result, octal_result, hexal_result])
print(myTable)
