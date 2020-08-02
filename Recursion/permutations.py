# Approach: Iterate through the array and for every element, append the element in the permutations of {array - element}. Thus `perm(contains: n) = perm(without n) + n` thus it is recursive definition with base case being only 2 elements when the result is {a, b} & {b ,a}
# Optimize: Memoize results: use tuple(list)

# Note: frozenset can be used because an array of unique integers given. (or else frozenset() will obliterate non-unique numbers)
# Try thinking how you'll solve it of it was non-unique integers
# IMP: Notice that frozenset used for two things: a) to create key of dictionary (tuple can be used instead) b) to obtain set difference (will need new logic)
# Talk with your interviewer. Try to get a solution ready as below (consider only unoque numbers) which will fail some cases 

# IMP Learning:
# if you mutate an array stored in a dictionary after storing it, the value stored in doctionary also changes!
# d = {}
# arr = [3, 5, 6] 
# d[1] = arr
# arr.append(7)
# d[1] # [3,5,6,7] even though you did not change the dictionary value, the reference is the same!
# use tuples for non-mutation

def getPermutations(array, count = 0, dict = {}, result = []):
  # if count == 10:
  # 	return result
  # count += 1
  if len(array) == 2:
    return [[array[0], array[1]], [array[1], array[0]]]
  for integer in array:
    # get all permutations except current integer
    remainingSet = frozenset(set(array) - set([integer]))
    if remainingSet in dict:
      # print(dict)
      print("Existing: ",remainingSet, "::",dict[remainingSet])
      remaining = list(dict[remainingSet])
    else:
      remaining = getPermutations(list(remainingSet), count, dict, result)
      print(">>>>>",remainingSet, ":", remaining)
      dict[remainingSet] = remaining.copy()
      print("***", integer, dict[remainingSet])
      # append current integer in all results
    # print("::",integer, remaining)
    # count = 0
    for rem in remaining:
      rem.append(integer)
      # result.append(rem)
      # print(remaining)
      # count += 1
      # if count == 20:
      #   break
      # print(integer, rem)
      # return remaining
    # print("rem: ",remaining)
    result.extend(remaining)
  return result

print(getPermutations([1,2,3,4]))

