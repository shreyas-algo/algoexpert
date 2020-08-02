# Approach: Iterate through the array and for every element, append the element in the permutations of {array - element}. Thus `perm(contains: n) = perm(without n) + n` thus it is recursive definition with base case being only 2 elements when the result is {a, b} & {b ,a}
# Optimize: Memoize results: use tuple(list)

# IMP Learning 1:
# if you mutate an array stored in a dictionary after storing it, the value stored in doctionary also changes!
# d = {}
# arr = [3, 5, 6] 
# d[1] = arr
# arr.append(7)
# d[1] # [3,5,6,7] even though you did not change the dictionary value, the reference is the same!
# ***BIG: use tuples to store lists in dictioanry for non-mutation

# IMP Learning 2:
# lists cannot be hashed as keys in dictionary. Use tuples

#TODO:
# 1. Note issue with array of array iteration when appending inner array (except for list in dict issue)
# 2. why result had to be init for every call

# Note: frozenset can be used because an array of unique integers given. (or else frozenset() will obliterate non-unique numbers)
# Try thinking how you'll solve it of it was non-unique integers
# IMP: Notice that frozenset used for two things: a) to create key of dictionary (tuple can be used instead) b) to obtain set difference (will need new logic)
# Talk with your interviewer. Try to get a solution ready as below (consider only unoque numbers) which will fail some cases 

def getPermutations(array, dict = {}):
  result = []
  if len(array) == 2:
    return ((array[0], array[1]), (array[1], array[0]))
  for integer in array:
    # get all permutations except current integer
    remainingSet = frozenset(set(array) - set([integer]))
    if tuple(remainingSet) in dict:
      remaining = dict[tuple(remainingSet)]
    else:
      remaining = getPermutations(list(remainingSet), dict)
      dict[tuple(remainingSet)] = tuple(remaining)
    # append current integer in all results
    remaining_list = []
    for rem in remaining:
      rem_list = list(rem)
      rem_list.append(integer)
      remaining_list.append(rem_list)
    result.extend(remaining_list)
  # print(array, result)
  return result

print(getPermutations([1,2,3,4]))

