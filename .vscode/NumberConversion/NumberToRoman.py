numerals = {"I":1, "V":5, "X":10, "L": 50, "C": 100, "D": 500, "M": 1000 }

def convert_roman(input_number):
  range_flag = None
  for symbol, integer in numerals.items():
    if integer == input_number: return symbol
    if input_number > integer:
      range_flag = symbol
      
  remaining = input_number - numerals[range_flag]
  return range_flag + convert_roman(remaining)
    
    
print(convert_roman(1)) # I
print(convert_roman(11)) # XI
print(convert_roman(111)) # CXI