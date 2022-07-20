#O(n) solution
def is_unique_dictionary(string):
  maps = {}
  for s in string:
    if s in maps:
      return False
    maps[s]=1 
  return True

#O(n) solution
def is_unique_set(string):
  #a set will only contain unique values. If the length of the set of string #characters = length of characters in the string, implies the string only
  #contains unique characters.
  return len(set(string))==len(string)


#O(nlogn) solution
# if the string is sorted,same characters will appear consecutively.
# Used a pointer to keep track of the previous character and compare with the current character. If same the string is not unique
def is_unique_sorting(string):
  sorted_string = sorted(string)
  prev = None
  for s in sorted_string:
    if(s==prev):
      return False
    prev = s
  return True



#Tests
print(is_unique_dictionary('abcde'))
print(is_unique_dictionary('axc!%ka'))
print(is_unique_set('abcde'))
print(is_unique_set('axc!%ka'))
print(is_unique_sorting('abcde'))
print(is_unique_sorting('axc!%ka'))
