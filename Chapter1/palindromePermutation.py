import string

#for a string to be a permutation of a palindrome
#if length is even, each character must appear even no of times in the string
#if length is odd, each character must appear even no of times in the string and one character must appear odd number of times

def count_characters(s):
  dic = {}
  for i in s:
    if(i in dic):
      dic[i]+=1
    else:
      dic[i]=1
  return dic

def palindrome_permutation(s):
  cleaned_string = "".join([c for c in s.lower() if c in string.ascii_lowercase])
  dic = count_characters(cleaned_string)
  odd_count= 0
  if(len(cleaned_string)%2==0):
    for key in dic:
      if(dic[key]%2==1):
        return False
  else:
    for key in dic:
      if(dic[key]%2==1):
        odd_count+=1
      if(odd_count>1):
        return False
  return True
    
  

#Tests

print(palindrome_permutation("As*&!sA()m   "))
print(palindrome_permutation("Tact Coa"))
print(palindrome_permutation("issaaa"))

