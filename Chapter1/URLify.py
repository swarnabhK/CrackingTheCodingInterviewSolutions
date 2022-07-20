# variable ends keeps track of the true length of the string
# Removes the trailing spaces in the string.
def remove_trailing_spaces(s):
  ends = len(s)-1
  for i in range(ends,-1,-1):
    if(s[i]==' '):
      ends-=1
    else:
      break
  return ends

#Function to replace the spaces in a string with "%20"(apart from trailing spaces)
def urlify(s):
  ends = remove_trailing_spaces(s)
  s = list(s)
  for i in range(ends+1):
    if(s[i]==' '):
      s[i] = '%20'
  return "".join(s[:ends+1])


def urlify_pythonic(s):
  ends = remove_trailing_spaces(s)
  return s[:ends+1].replace(" ","%20")

print(urlify("Mr John Smith     "))
print(urlify_pythonic("Betty White #    "))