def string_compress(string):
  count = 0
  result = []
  for i in range(len(string)):
    #if the two characters are not equal, its the end of the count block.
    #So count is made zero.
    if(i!=0 and string[i]!=string[i-1]):
      result.append(string[i-1]+str(count))
      count = 0
    # Count will always be incremented by 1, because even if
    # the characters are different, in that iteration a new count block has to start.
    count+=1
  
  #to add the last block of characters and their count
  if(count):
    result.append(string[i]+str(count))
  return result


#tests
print(string_compress('aabcccccaaa'))
print(string_compress('aabcccccaab'))
print(string_compress('a'))