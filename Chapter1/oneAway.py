import string

#Method returns a dictinary with the character and their counts in a string
def count_characters(s):
  dic = {}
  for i in s:
    if(i in dic):
      dic[i]+=1
    else:
      dic[i]=1
  return dic


def isOneEditAway_update(s1,s2):
  # case: check if only one character is different in both the strings.
  edited = False
  for c1,c2 in zip(s1,s2):
    if(c1!=c2):
      if edited:
        return False
      edited=True
  return True
    

def isOneEditAway_insertDelete(s1,s2):
  #case: remove a character and insert a character.  
  try:
    longer_string = max([s1,s2],key=len)
    shorter_string = min([s1,s2],key=len)
    dictionary_longer = count_characters(longer_string)
    for s in shorter_string:
      dictionary_longer[s]-=1
      if(dictionary_longer[s]==0):
        del dictionary_longer[s]
    return len(dictionary_longer)==1 and list(dictionary_longer.values())[0]==1
  except:
    return False


def isOneEditAway(s1,s2):
  if((len(s1)+1==len(s2)) or (len(s1)-1==len(s2))):
    return isOneEditAway_insertDelete(s1,s2)
  if(len(s1)==len(s2)):
    return isOneEditAway_update(s1,s2)


#Tests
print(isOneEditAway('bale','ple'))
print(isOneEditAway('paleabc','pleabc'))
print(isOneEditAway('pale','pkle'))