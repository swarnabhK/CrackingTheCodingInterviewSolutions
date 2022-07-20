#Two strings are permutations of each other if they have the same characters but the arrangement is different.

def character_counts(string):
  maps = {}
  for s in string:
    if(s in maps):
      maps[s]+=1
    else:
      maps[s]=1
  return maps

def check_permutation_dictionary(string1,string2):
  
  if(len(string1)!=len(string2)):
    return False
  s1_counts = character_counts(string1)
  s2_counts = character_counts(string2)
  return s1_counts==s2_counts



print(check_permutation_dictionary("paper","apper"))
print(check_permutation_dictionary("paper","apper "))