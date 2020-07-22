"""
Kyle Mabry
76361438
I worked alone, and with no help.
"""

"""
Additional functions:
"""


def bricks_are_almost_same(tower, index, brick_picked):
    """Makes sure that the brick to be placed at a certain index of a given tower isn't within +3 or -3 of the brick
    that's already in that index. This function keeps the computer from swapping between the same brick in the discard
     pile across multiple turns. Basically keeps computer from getting stuck on two numbers. eg. 51 and 52 across
     turns. Returns True if they are almost the same, and returns false if they are not."""

    brick_in_tower = tower[index]  # get the brick that's already in the tower at the index we specified.
    # for check within a range of +/- 3 is there already a brick in the tower that is within this range?
    for check in range(-3, 4):
        # check is equal to itself plus the brick in the tower. this gives us the range of +/- 3.
        check = check + brick_in_tower
        # if the brick picked is close to the brick that's already in this spot in the tower.
        if check == brick_picked:
            return True  # if there is already a brick in the tower at the index similar to brick in question.
    # if there wasn't already a brick in the tower at the index we're looking at that's similar to the picked brick.
    return False


def reverse_list(lst):
    """given a list, it reverses the order of the original list and returns a new list that is reversed. The original
    list itself is not changed."""

    # take the original list and reverse its order, new_list points to the reversed list.
    new_list = lst[::-1]
    return new_list


def which_pile_to_take_from(main_pile, discard):
    """Asks the user which pile they would like to take from this current turn. once the user selects which
    pile they would like to take from this function returns a tuple including that brick as well as a string indicating
    which pile the player picked their brick from. The brick will either be from the main pile, or from the
    discard pile."""

    asking = True
    while asking:
        which_pile = input("Would you like to take from the main pile, 'm', or from the discard pile, 'd'? "
                           "(if you have any questions press, 'H'): ")

        if which_pile == 'm' or which_pile == 'M':  # if the user input m for main pile.
            main_pile_brick = get_top_brick(main_pile)  # take the top card from the main pile.
            which_pile_picked = "main"
            return main_pile_brick, which_pile_picked  # return the main_pile brick for us to use.

        if which_pile == 'd' or which_pile == 'D':  # if the user input d for discard pile.
            discard_pile_brick = get_top_brick(discard)  # take the top card from the discard pile
            which_pile_picked = "discard"
            return discard_pile_brick, which_pile_picked  # return the discard pile brick for us to use.

        # if the user needs some help.
        if which_pile == 'h' or which_pile == 'H':
            print("The main pile you don't have direct access to and you won't know which brick you're going to get,"
                  "\nthe discard pile you know the value of and can use this card to replace a card within your tower"
                  "\nbe careful when making your choice because if you choose a card from the main pile and then "
                  "\ndiscard it, the computer might use this card.")


def which_brick_to_replace(tower):
    """This asks the player which brick in their tower they would like to replace, returns the brick they indicated."""

    # in the weird case that the player doesn't indicate a brick to replace.
    brick_to_replace = None
    # helps make sure that we get a valid answer from the player.
    asking = True
    while asking:
        brick_to_replace = input("please indicate a valid brick from your tower that you would like to "
                                 "replace with this brick that you have just picked."
                                 " (eg. if bricks value is 40, then input 40): ")

        # if we get a value error continue the while loop and ask again.
        try:
            brick_to_replace = int(brick_to_replace)
        except ValueError as error:
            print("please try inputting only an integer.")
            continue
        # if we didn't get an error while getting user input test to see that the bricks value is valid.
        if 0 < int(brick_to_replace) <= 60:  # if user gave valid answer then break out of the loop and return value
            # Making sure that the brick the user gave is actually a brick in the tower that we can replace.
            for bricks in tower:
                if brick_to_replace == bricks:
                    return brick_to_replace


def ask_yes_or_no(prompt):
    """This function prompts the user to answer yes or no and returns their response. Yes will be returned as True
    and no will return as False. Useful for prompting user whether or not they want to roll again. If the user
    responds with an inappropriate answer it will continue to prompt them for a response until they respond
    with an acceptable answer."""

    ensure_correct = True  # initializing this to true so that our while loop runs until we get an acceptable answer.
    while ensure_correct:
        # Prints the prompt and waits for an answer.
        player_resp = input(prompt)
        # If answer is yes, return True.
        if (player_resp == 'y') or (player_resp == 'Y'):
            result = True
            ensure_correct = False
        # If answer is no, return False.
        elif (player_resp == 'n') or (player_resp == 'N'):
            result = False
            ensure_correct = False

    # Returns boolean true or false depending on the players answer.
    return result


def print_instructions():
    """"Prints the instructions of the game to the user."""

    # I copied and pasted this directly from the homework assignment PDF. Sources cited. That would have been a lot of
    # typing!
    print("\nWelcome to Tower Blaster, this is a strategy game. You will be playing against the computer. "
          "\nTower Blaster starts with a main pile of 60 bricks, each numbered from 1 to 60. Think of the numbers on "
          "\nthe bricks as the width of the bricks. The objective is to be the"
          "\nfirst player to arrange 10 bricks in your own tower from lowest to highest "
          "\n(from the top down), because the tower will be unstable otherwise. The bricks in the main pile are "
          "\nshuffled at the start and both the user and the computer are dealt 10 bricks from the main pile. As a "
          "\nplayer receives each brick, they must place it on top of their current tower in the order it is received. "
          "\nYes, initially your tower is likely to be unstable. After the first 10 bricks are dealt to the user and "
          "\nthe computer, there will be 40 bricks remaining in the main pile. The top brick of the main pile is "
          "\nturned over to begin the discarded brick pile. On each player’s turn, the player chooses to pick up the "
          "\ntop brick from the discard pile or to pick up the top brick from the main pile. The top brick from the "
          "\ndiscard pile is known. In other words, the discard pile is ‘face up’ and everyone knows how wide the top "
          "\nbrick is. The main pile is ‘face down’. Choosing the top brick from the main pile can be risky, because "
          "\nthe player does not know what the brick is. Once a player chooses a brick, either from the discard pile "
          "\nor from the main pile, the player decides where in the tower to put the brick. The tower is always 10 "
          "\nbricks high, so placing a brick means that an existing brick in the tower is removed and replaced with "
          "\nthe new brick. If the player takes a brick from the main pile (the one that is ‘face down’), the player "
          "\ncan reject it and place it in the discard pile. This means that nothing in that player’s tower changes "
          "\nduring that turn. If the player takes a brick from the discard pile (the one that is ‘face up’), the "
          "\nplayer MUST place it into the tower. The first player to get their 10 bricks in order wins. If, at any "
          "\npoint, all of the cards have been removed from the main pile of bricks, then all of the cards in the "
          "\ndiscard pile are shuffled and moved to the main pile. Then the top card is turned over to start "
          "\nthe new discard pile.")


"""
Required functions:
"""


def setup_bricks():
    """This creates the main pile of 60 bricks, represented as a list of integers from 1 to 60, inclusive.
    This function also creates a discard pile of zero bricks, represented as an empty list."""

    # Creating our list of bricks.
    main_bricks = list(range(1, 61))
    # Creating our list of discarded bricks, for now there are none.
    discard_pile = []

    # Returns a tuple of discard_pile and bricks, parenthesis are redundant, the comma alone will create a tuple.
    return (main_bricks, discard_pile)


def shuffle_bricks(bricks):
    """This function does not return anything. It takes the list of bricks as an input and shuffles the
    original list. using the built-in random shuffle function. """

    # import the random module
    import random
    # use the random.shuffle method to shuffle our list of bricks, don't return anything, original list is shuffled.
    random.shuffle(bricks)


def check_bricks(main_pile, discard):
    """This function checks to see if there are any cards left in the given main pile of bricks.
    if there aren't it will shuffle the discard pile and move those bricks to the main pile. It will then turn
    over the top card, starting the new discard pile."""

    # if the main pile is empty
    if not main_pile:
        # shuffle the bricks within the discard pile.
        shuffle_bricks(discard)
        # make the main_pile a copy of the discard pile.
        main_pile = discard.copy()
        # flip over the first card in the main pile, assign it to the discard pile, and remove it from the main pile.
        discard = [main_pile[0]]
        main_pile.pop(0)

    # Again using redundant parenthesis here just to make sure that we return a tuple.
    return (main_pile, discard)


def check_tower_blaster(tower):
    """Checks the input tower to see whether stability has been achieved or not. Stability means bricks are in
    ascending order. This function will return a boolean value."""

    # sort the input tower and assign it to tower_sorted.
    tower_sorted = sorted(tower)
    # if the input tower is equal to the sorted tower then we have achieved stability.
    if tower == tower_sorted:
        stability = True
    # otherwise the two towers won't be equal to one another, which means the input tower wasn't stable.
    else:
        stability = False

    # returns stability as True or False
    return stability


def get_top_brick(brick_pile):
    """Remove and return the top brick from any given pile of bricks. Removes and returns the first element of any
    given list."""

    # Set the top brick, the first index of 0, equal to top_brick. "Int" is to ensure that we return an integer.
    top_brick = int(brick_pile[0])
    # Remove the top brick from the pile of bricks.
    brick_pile.pop(0)

    # Return the top brick back to us and the updated brick pile.
    return top_brick


def deal_initial_bricks(main_pile):
    """Start the game by dealing two sets of 10 bricks each, from the main_pile. Follows the normal conventions of
    dealing. One to user, one to computer and so on. Computer is always first to get dealt and always plays first.
    This function returns a tuple containing two lists, one for each player's hand."""

    # initializing the computer's and player's hand.
    computer_tower = []
    player_tower = []
    # first create the list of the computer_tower, dealing the computer the first card in the list.
    counter = 0
    for card in main_pile[0:20]:
        # dealing first computer card first.
        if (counter % 2) == 0 or counter == 0:
            computer_tower.append(card)
            counter += 1
        # dealing player's card second.
        elif (counter % 2) != 0:
            player_tower.append(card)
            counter += 1
        # After each card is dealt from the top of the pile, remove the card from the main pile.
        main_pile.pop(0)

    # now reverse the list of the computer hand using the reverse function we built above.
    # reverse the order of the cards in the hand so that they appear to have been dealt one on top of the other.
    computer_tower = reverse_list(computer_tower)
    player_tower = reverse_list(player_tower)

    # return a tuple of the computer's hand and the player's hand.
    return (computer_tower, player_tower)


def add_brick_to_discard(brick, discard):
    """Add the given brick (represented as an integer) to the top of the given discard pile (list). This function
    returns nothing."""

    # insert, at the first index of the discard pile, the current brick.
    discard.insert(0, brick)


def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    """Find the given brick to be replaced (represented as an integer) in the given tower and replace it with the given
    new brick. The given brick is placed on the top of the discard pile. Returns True if brick is replaced,
    otherwise returns False."""
    # initialize a counter to get the index of the brick to be replaced in the tower.
    index_counter = 0
    # for bricks in the tower
    for brick in tower:
        # if the current brick is equal to the brick that we're looking to replace, aka it exists in the tower.
        if brick == brick_to_be_replaced:
            # save the index of the brick that we want to replace.
            index_of_brick = index_counter
            # get rid of the brick that we want to replace from the tower.
            tower.pop(index_of_brick)
            # add the brick in the place of the brick that we just got rid of.
            tower.insert(index_counter, new_brick)
            # return true if we were able to replace the brick successfully.
        # increment the counter after each run of the for loop.
        index_counter += 1

    # Make a true copy of the discard file so that we can make sure an additional card was added to it later on.
    initial_discard = discard.copy()
    # add the brick to the discard.
    add_brick_to_discard(brick_to_be_replaced, discard)
    # if the lengths of the discard pile didn't change then we know our brick wasn't replaced properly.
    if len(discard) == len(initial_discard):
        return False
    # And if the discard pile was updated correctly return true.
    if discard[0] == brick_to_be_replaced:
        return True


def computer_play(tower, main_pile, discard):
    """This is the function that includes the computer's strategy. The computer can't cheat and look into any of
    the piles that the player does not have access to. This function returns the new tower for the computer. This
    function assumes that the computer hasn't already won the game and has at least one brick that's still
    out of place. returns an updated tower, which brick the computer picked, which brick was replaced in the tower,
    which pile the computer picked from and the updated main pile and the updated discard pile. I must admit,
    this is a pretty agro strategy, the computer beats me at least half of the time."""

    # initialize these so we don't get annoying messages.
    brick_picked = None
    replaced_brick = None
    which_pile = None

    turn_over = False  # initialize variable to keep the turn going until we replace a brick in the tower or discard.
    # while it's still the computer's turn.
    while not turn_over:

        if discard:  # if there's a card in the discard pile.
            brick_picked = get_top_brick(discard)  # remove the top brick from the discard pile.
            which_pile = 'discard'  # identifying which pile the computer took from, this is important for telling the
            # player which pile the computer picked from later on.

            # I decided to inflate the index of the tower by 6 so that each index for the tower corresponded to a range
            # of possible bricks that should belong in the tower. For example. index 1 should only be replaced with a
            # brick that is between 3 and 9, and index 5 should only be replaced by a brick that is between 27 and 33.
            for inflated_index in range(0, 61, 6):
                # find the index where this brick belongs.
                if inflated_index + 3 >= brick_picked >= inflated_index - 3:
                    # deflate the index if it's not equal to zero so that we can use find_and_replace soon.
                    if inflated_index != 0:
                        # divide the inflated index by 6 to get the regular index of the tower.
                        index = int(inflated_index / 6)
                        if index > 9:  # hack to make sure that we don't index something that's out of range.
                            index = 9
                    else:  # in the case that index was equal to zero, we obviously can't divide zero by 6.
                        index = inflated_index  # just set equal to self if the inflated index was zero.
                    # if the index of the tower scales relatively (multiply index by 6)
                    # to the brick, place it in that index. If not we'll just take a brick from the main pile in the
                    # next for loop below.
                    # if there isn't already a brick in the tower at the index we're looking at that is close to
                    # the value of the brick that we are evaluating from the discard pile. This following code keeps the
                    # computer from getting stuck placing and removing the same two bricks from the discard pile
                    # across turns.
                    if tower[index] + 3 >= brick_picked >= tower[index] - 3:
                        # if the brick in the tower isn't within +/- 3 of the brick that we're looking at from the
                        # discard pile.
                        if not bricks_are_almost_same(tower, index, brick_picked):
                            find_and_replace(brick_picked, tower[index], tower, discard)
                            replaced_brick = True  # we've replaced a brick and will return this for the user to know.
                            turn_over = True  # end the while loop on its next iteration.
                            break  # break out of the for loop.
            else:
                # if we didn't take the discard brick, put it back on the top of the discard pile.
                add_brick_to_discard(brick_picked, discard)
        if turn_over:  # if the computer has taken their turn, break out of the while loop.
            break
        # now do the same thing that the last few blocks of code did, except look at the first card at the
        # top of the main pile. Because at this point, if none of the following blocks were run, we probably will need
        # a fresh card to look at. At this point, we've chosen to not take a card from the discard pile, but to
        # take a card from the main pile instead.
        # if none of the above were run then do the former: Take a brick from the main pile.
        if not turn_over:
            brick_picked = get_top_brick(main_pile)  # remove the top brick from the main pile.
            which_pile = 'main'  # identifying which pile the computer took from, this is important for telling the
            # player which pile the computer picked from later on.

            turn_over = True  # Also, since we took a brick from the main pile, regardless of whether or not we use it,
            # our turn is effectively over.

            # again we're looking at the inflated index to see which spot in the tower the brick should belong for
            # maximum stability to be achieved.
            for inflated_index in range(0, 61, 6):
                if inflated_index + 3 >= brick_picked >= inflated_index - 3:
                    # deflate the index if it's not equal to zero so that we can use find_and_replace
                    if inflated_index != 0:
                        index = int(inflated_index / 6)
                        answer = True
                        if index > 9:  # hack to make sure that we don't index something that's out of range.
                            index = 9
                    else:  # in the case that index was equal to zero.
                        index = inflated_index  # just so we have agreement with the index in the next line.
                        answer = True
                    if answer:
                        # if there isn't already a brick in the tower at the index we're looking at that's close to
                        # the value of the brick that we are evaluating from the main pile.
                        if not bricks_are_almost_same(tower, index, brick_picked):
                            find_and_replace(brick_picked, tower[index], tower, discard)
                            replaced_brick = True  # this will be returned by the function for the user to see.
                            turn_over = True  # end the while loop on its next iteration.
                            break  # break out of the for loop once we've placed a brick
                        else:
                            # otherwise the computer won't be using the card from the main pile and end the turn.
                            add_brick_to_discard(brick_picked, discard)  # add the brick to the top of the main pile.
                            turn_over = True  # the computer's turn is over.
                            break  # break out of the for loop.
                    # if we haven't replaced a brick in the tower by now then it's time to discard the brick we're
                    # looking at. This if statement is here just in case the "if not bricks_are_almost_same" statement
                    # wasn't run.
                    if not answer:
                        # add the card to the discard pile.
                        add_brick_to_discard(brick_picked, discard)
                        # break out of the while loop.
                        turn_over = True
        if turn_over:  # if the computer has taken their turn, break out of the while loop.
            break

    # returns an updated tower, which brick the computer picked, which brick was replaced in the tower, which pile
    # the computer picked from and the updated main pile and the updated discard pile.
    return tower, brick_picked, replaced_brick, which_pile, main_pile, discard


def main():
    """This is the main function that will run our game."""

    # Starting the while loop if the player wants to play.
    playing = ask_yes_or_no("Would you like to play the tower blaster game?('y' or 'n'): ")

    # initialize variables so that if they aren't re-assigned we don't get an error.
    computer_tower = None
    player_tower = None
    main_pile = None
    discard = None

    if playing:
        # Set this up regardless of whether or not the player is playing. It doesn't hurt.
        starting_bricks = setup_bricks()  # initialize the bricks.
        main_pile = starting_bricks[0]  # separate main pile from discard pile
        discard = starting_bricks[1]  # define the discard pile from the tuple.
        shuffle_bricks(main_pile)  # shuffle the main bricks.
        add_brick_to_discard(main_pile[0], discard)  # add a brick to the discard pile.
        computer_tower, player_tower = deal_initial_bricks(main_pile)  # deals the initial bricks to user and computer.
        need_instructions = ask_yes_or_no("\nWelcome to Tower Blaster, if you need "
                                          "the instructions please press (y or n): ")
        if need_instructions:
            print_instructions()
        print("\nThis is the computer's starting hand, take note, you will only see it once:")
        # print the computer's hand once before the game starts.
        print(computer_tower)

    while playing:
        # check to be sure that there are bricks left in the main pile before the computer's turn.
        main_pile, discard = check_bricks(main_pile, discard)
        # let's the computer go first. We're collecting the returned variables.
        print("\nNow it's the computer's turn!")
        computer_tower, computer_brick_picked, computer_replaced_brick, which_pile, main_pile, discard = \
            computer_play(computer_tower, main_pile, discard)
        # print which pile the computer picked from
        print("\nThe computer picked:", computer_brick_picked, "from the", which_pile, "pile.")

        # print whether or not the computer decided to pick a brick or not.
        if computer_replaced_brick:
            print("The computer chose to replace a brick this turn.")
        else:
            print("The computer did not choose to replace a brick this turn.")

        # checking to see if the computer won the game.
        did_computer_win = check_tower_blaster(computer_tower)
        if did_computer_win:
            print("The computer has won the game with a tower of:")
            print(computer_tower)
            # if the computer won the game ask if the player would like the play again. if they say no exit the program.
            playing = ask_yes_or_no("Would you like to play again? ('y' or 'n'): ")
            if not playing:
                break
            if playing:  # initialize another game.
                starting_bricks = setup_bricks()  # initialize the bricks.
                main_pile = starting_bricks[0]  # separate main pile from discard pile
                discard = starting_bricks[1]  # define the discard pile from the tuple.
                shuffle_bricks(main_pile)  # shuffle the main bricks.
                add_brick_to_discard(main_pile[0], discard)  # add a brick to the discard pile.
                computer_tower, player_tower = deal_initial_bricks(
                    main_pile)  # deals the initial bricks to user and computer.
                # ask if the user needs instructions, the rest should be pretty self explanatory.
                need_instructions = ask_yes_or_no("\nWelcome to Tower Blaster, if you need "
                                                  "the instructions please press (y or n):")
                if need_instructions:
                    print_instructions()
                # print the computer's hand once before the game starts.
                print(
                    "\nThis is the computer's starting hand, take note, you will only see it once:")
                print(computer_tower)
                continue  # return to the top of the while loop in this case so that the computer goes first and not
                # the player.

        # now it's the player's turn, it will take a brick from the pile that they specify.
        # check to be sure that there are bricks left in the main pile before the computer's turn.
        main_pile, discard = check_bricks(main_pile, discard)
        print("\nNow it's your turn!")
        print("This is your tower:", player_tower)
        print("the top card on the discard pile is", discard[0], "\n")
        user_brick, which_pile_picked = which_pile_to_take_from(main_pile, discard)
        print("You picked", user_brick, "From the", which_pile_picked)
        if which_pile_picked != "discard":  # if the player picked from the main pile
            use_brick = ask_yes_or_no("Do you want to use this brick? (type 'y' or 'n'): ")
            if use_brick:
                brick_to_replace = which_brick_to_replace(player_tower)
                find_and_replace(user_brick, brick_to_replace, player_tower, discard)
                print("You replaced:", brick_to_replace, "with:", user_brick)
                print("Your new tower is:", player_tower)
            else:
                # if the player decides not to use the brick that they picked
                # from either pile then put it in the discard pile.
                print("you chose not to use the brick you picked.")
                print("Your tower is still:", player_tower, "and your turn is over.")
                add_brick_to_discard(user_brick, discard)
        else:  # This gets executed if the player picked from the discard pile. They won't get a choice
            # of whether or not to not use the brick.
            brick_to_replace = which_brick_to_replace(player_tower)
            find_and_replace(user_brick, brick_to_replace, player_tower, discard)
            print("You replaced:", brick_to_replace, "with:", user_brick)
            print("Your new tower is:", player_tower)

        # checking to see if the player won the game.
        did_player_win = check_tower_blaster(player_tower)
        if did_player_win:
            print("You have won the game with a tower of:")
            print(player_tower)
            print("congratulations!!!")
            # if the player won the game ask if they would like to play again. if they say no exit the program.
            playing = ask_yes_or_no("Would you like to play again?(type 'y' or 'n'): ")
            if not playing:
                break
            if playing:  # initialize another game.
                starting_bricks = setup_bricks()  # initialize the bricks.
                main_pile = starting_bricks[0]  # separate main pile from discard pile
                discard = starting_bricks[1]  # define the discard pile from the tuple.
                shuffle_bricks(main_pile)  # shuffle the main bricks.
                add_brick_to_discard(main_pile[0], discard)  # add a brick to the discard pile.
                computer_tower, player_tower = deal_initial_bricks(
                    main_pile)  # deals the initial bricks to user and computer.
                # ask if the user needs instructions, the rest should be pretty self explanatory.
                need_instructions = ask_yes_or_no("\nWelcome to Tower Blaster, if you need "
                                                  "the instructions please press (y or n): ")
                if need_instructions:
                    print_instructions()
                print(
                    "\nThis is the computer's starting hand, take note, you will only see it once:")
                # print the computer's hand once before the game starts.
                print(computer_tower)
                # no need for continue at the bottom of this block of code becauase the computer will go first anyway.

    # if the game is over and the user does not indicate whether they want to play again.
    print("\nThe game is over! thank you for playing, it was truly a pleasure.")


# Entry point to our program.
if __name__ == '__main__':
    main()
