def isSubstring(s1,s2):
  if(s1 in s2):
    return True
  return False
  
def is_rotation(s1,s2):
  return isSubstring(s2,s1*2)


print(is_rotation('erbottlewat','waterbottle'))
print(is_rotation('erbottlewat','waterbottles'))
print(is_rotation('alayahim','himalaya'))