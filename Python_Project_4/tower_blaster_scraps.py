"""
# if the brick in the discard pile is greater than any brick we have in our pile take it and put it
# at the bottom of our pile.
if discard:  # if there are cards in the discard pile.
print("Ran up to discard")
brick_picked = get_top_brick(discard)  # look at the top card in the discard pile.
if brick_picked > largest_brick:  # if top of discard is greater then our towers largest brick.
which_pile = 'discard'
find_and_replace(brick_picked, tower[9], tower, discard)
replaced_brick = True
print('ran1')
break  # if this section ran then the computer's turn is over.

# if the brick in the discard pile is smaller than any brick we have in our pile, take it and put it at the top
# of our pile. find the smallest brick that's out of place.
if brick_picked < smallest_brick:
which_pile = 'discard'
find_and_replace(brick_picked, tower[0], tower, discard)
replaced_brick = True
print('ran2')
break  # if this section ran then the computer's turn is over.

# for the first item in the unsorted brick index, which should ultimately be the smallest.
# if the top brick in the discard pile is smaller than the brick we're looking at.
if brick_picked <= 10 and brick_picked <= tower[unsorted_brick_index[0]]:
which_pile = 'discard'
find_and_replace(brick_picked, tower[unsorted_brick_index[0]], tower, discard)
replaced_brick = True
print('ran3')
break  # if this section ran then the computer's turn is over.

# for the second item in the unsorted brick index, which should ultimately be the second smallest.
# if the top brick in the discard pile is smaller than the brick we're looking at.
if brick_picked <= 20 and brick_picked <= tower[unsorted_brick_index[1]]:
which_pile = 'discard'
find_and_replace(brick_picked, tower[unsorted_brick_index[1]], tower, discard)
replaced_brick = True
print('ran4')
break  # if this section ran then the computer's turn is over.

# for the third item in the unsorted brick index, which should ultimately be the third smallest.
# if the top brick in the discard pile is smaller than the brick we're looking at.
if brick_picked <= 30 and brick_picked <= tower[unsorted_brick_index[2]]:
which_pile = 'discard'
find_and_replace(brick_picked, tower[unsorted_brick_index[2]], tower, discard)
replaced_brick = True
print('ran5')
break  # if this section ran then the computer's turn is over.
# reverse the order of the unsorted_brick_index list so that we can index the first variable
# which is actually the last index of the unsorted brick, which should be the largest brick.
reversed_unsorted_brick_index_copy = reverse_list(unsorted_brick_index.copy())  # first make a real copy
# of the original, And then reverse the order of the list using our reverse_list function.
# If the first item in the discard pile is greater than the "last" index of the last unsorted bricks
# take that brick and insert it into our tower.
if brick_picked >= 50 and brick_picked >= tower[reversed_unsorted_brick_index_copy[0]]:
which_pile = 'discard'
find_and_replace(brick_picked, tower[reversed_unsorted_brick_index_copy[0]], tower, discard)
replaced_brick = True
print('ran6')
break  # if this section ran then the computer's turn is over.

# If the second item in the discard pile is greater than the "second to last" index of the last unsorted bricks
# take that brick and insert it into our tower.
if brick_picked >= 40 and brick_picked >= tower[reversed_unsorted_brick_index_copy[1]]:  # indexing second item.
which_pile = 'discard'
find_and_replace(brick_picked, tower[reversed_unsorted_brick_index_copy[1]], tower, discard)
replaced_brick = True
print('ran7')
break  # if this section ran then the computer's turn is over.
# if none of the above could be run then we don't want to use the card in the discard pile and instead
# want to pick a fresh card from the main pile. so set brick_picked to be false, since we are allowed to
# look at the top of the discard pile.
else:
brick_picked = False
"""

"""
if not replaced_brick:  # making sure this doesn't run if we've replaced a brick by now.

if brick_picked > largest_brick:  # if top of the main pile is greater then our towers largest brick.
    find_and_replace(brick_picked, tower[9], tower, discard)  # replace the main pile with the
    replaced_brick = True
    print('ran8')
    break  # if this section ran then the computer's turn is over.

if brick_picked < smallest_brick:  # if top of the main pile is greater then our towers largest brick.
    find_and_replace(brick_picked, tower[0], tower, discard)
    replaced_brick = True
    print('ran9')
    break  # if this section ran then the computer's turn is over.

# for the first item in the unsorted brick index, which should ultimately be the smallest.
# if the top brick in the main_pile pile is smaller than the brick we're looking at.
# make sure we're not putting a huge brick in the top spot.
if brick_picked <= 10 and brick_picked <= tower[unsorted_brick_index[0]]:
    find_and_replace(brick_picked, tower[unsorted_brick_index[0]], tower, discard)
    replaced_brick = True
    print('ran10')
    break  # if this section ran then the computer's turn is over.

# for the second item in the unsorted brick index, which should ultimately be the second smallest.
# if the top brick in the main_pile pile is smaller than the brick we're looking at.
# make sure we're not putting a huge brick in a near top spot.
if brick_picked <= 20 and brick_picked <= tower[unsorted_brick_index[1]]:
    find_and_replace(brick_picked, tower[unsorted_brick_index[1]], tower, discard)
    replaced_brick = True
    print('ran11')
    break  # if this section ran then the computer's turn is over.

# for the third item in the unsorted brick index, which should ultimately be the third smallest.
# if the top brick in the main_pile pile is smaller than the brick we're looking at.
# make sure we're not putting a huge brick in a near top spot.
if brick_picked <= 30 and brick_picked <= tower[unsorted_brick_index[2]]:
    find_and_replace(brick_picked, tower[unsorted_brick_index[2]], tower, discard)
    replaced_brick = True
    print('ran12')
    break  # if this section ran then the computer's turn is over.

# Remember our reversed unsorted_brick_index from before? We're going to use that again here.
reversed_unsorted_brick_index_copy = reverse_list(unsorted_brick_index.copy())  # Make real copy of list.
# If the first item in the main pile is greater than the "last" index of the last unsorted bricks
# take that brick and insert it into our tower.
# Make sure we're not putting a small brick at the bottom of the tower.
if brick_picked >= 50 and brick_picked >= tower[reversed_unsorted_brick_index_copy[0]]:
    find_and_replace(brick_picked, tower[reversed_unsorted_brick_index_copy[0]], tower, discard)
    replaced_brick = True
    print('ran13')
    break  # if this section ran then the computer's turn is over.

# If the second item in the main pile is greater than the "last" index of the last unsorted bricks
# take that brick and insert it into our tower.
# Make sure we're not putting a small brick at the bottom of the tower.
if brick_picked >= 40 and brick_picked >= tower[reversed_unsorted_brick_index_copy[1]]:
    find_and_replace(brick_picked, tower[reversed_unsorted_brick_index_copy[1]], tower, discard)
    replaced_brick = True
    print('ran14')
    break  # if this section ran then the computer's turn is over.
"""
