'''
# HexToSignedIntStr.py
# a simple python script that takes a hex number
# as input and returns its value as a signed
# integer. this is done by converting the hex
# to binary then using the 2's complement
# method to convert into the right integer value.
# date: 8/3/2021
# author: dnglokpor
'''

def hexToBin(hexValue: int) -> str:
   '''return the binary equivalent of the hex
      string passed as a string.
   '''
   return bin(int(hexValue, 16))[2:]

def bOr(a : str, b : str) -> str:
   '''does a OR operation on two string bits.
      return the result as a string.
   '''
   if a != b or a == 1:
      return '1'
   else:
      return '0'

def bXor(a : str, b : str) -> str:
   '''does a XOR operation on two string bits.
      return the result as a string.
   '''
   if a == b:
      return '0'
   else:
      return '1'

def bAnd(a : str, b : str) -> str:
   '''does a AND operation on two string bits.
      return the result as a string.
   '''
   if a == b == '1':
      return '1'
   else:
      return '0'

def signedBinaryConv(hexValue : str) -> int:
   '''using a passed string hexadecimal number, uses
      the method of 2's complement to convert it to
      a signed integer value. return the integer value.
   '''
   binValue = hexToBin(hexValue)
   print("binary " + str(binValue))
   # 2's complement:
   comp = str()
   for i in range(len(binValue)):
      if binValue[i] == '0':
         comp += '1'
      else:
         comp += '0'
   # addition of 1:
   print("flip " + str(comp))
   res = list()
   one = list()
   for i in range(len(comp) - 1):
      one.append('0')
   one.append('1')
   a = '0'
   b = '0'
   s = '0'
   c = '0'
   cin = '0'
   cout = '0'
   for i in range(len(comp)):
      if i != 0:
         cin = cout
      a = comp[-(i+1)]
      b = one[-(i+1)]
      s = bXor(bXor(a, b), cin)
      cout = bOr(bAnd(a, b), bAnd(cin, bXor(a, b)))
      res.append(s)
   resVal = str()
   # print("res " + str(res)) DEBUG
   for i in range(len(res)):
      resVal += res[-(i+1)]
   print("comp " + str(resVal))
   # conversion to decimal
   total = 0
   for i in range(len(res)):
      total += int(res[i]) * pow(2, i)
   if binValue[0] == '1':
      total = -1 * total
   return total

# run
if __name__ == "__main__":
   hexString = input("Enter HEX number: ")
   print(hexString + " = " + 
      str(signedBinaryConv(hexString))
   )