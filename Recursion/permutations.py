# Approach: Iterate through the array and for every element, append the element in the permutations of {array - element}. Thus `perm(contains: n) = perm(without n) + n` thus it is recursive definition with base case being only 2 elements when the result is {a, b} & {b ,a}
# Optimize: Memoize results: use tuple(list)

# IMP Learning 1:
# if you mutate an array stored in a dictionary after storing it, the value stored in doctionary also changes!
# d = {}
# arr = [3, 5, 6] 
# d[1] = arr
# arr.append(7)
# d[1] # [3,5,6,7] even though you did not change the dictionary value, the reference is the same!
# ***BIG: use tuples to store lists in dictioanry for non-mutation or use list copy to do modifications

# IMP Learning 2:
# lists cannot be hashed as keys in dictionary. Use tuples or frozensets

# Note: frozenset can be used because an array of unique integers given. (or else frozenset() will obliterate non-unique numbers)
# Try thinking how you'll solve it of it was non-unique integers
# IMP: Notice that frozenset used for two things: a) to create key of dictionary (tuple can be used instead) b) to obtain set difference (will need new logic)
# Talk with your interviewer. Try to get a solution ready as below (consider only unoque numbers) which will fail some cases 

def getPermutations(array, dict = {}):
  result = []
  # for edge case [1]
  if len(array) == 1:
    return [[array[0]]]
  if len(array) == 2:
    return [[array[0], array[1]], [array[1], array[0]]]
  for integer in array:
    # get all permutations except current integer
    remainingSet = frozenset(set(array) - set([integer]))
    if remainingSet in dict:
      # print("existing:", remainingSet, dict[remainingSet])
      remaining = dict[remainingSet]
    else:
      remaining = getPermutations(list(remainingSet), dict)
      dict[remainingSet] = remaining
    # append current integer in all results
    for rem in remaining:
      # IMP: create a copy of rem & remaining or else the dictionary will change
      rem_copy = list(rem)
      # .copy() is another way to create copy
      # rem_list = rem.copy()
      rem_copy.append(integer)
      result.append(rem_copy)
  # print(array, result)
  # print(dict)
  return result

print(getPermutations([1,2,3,4]))

