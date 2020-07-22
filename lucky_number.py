"""Checks whether or not a lottery ticket is lucky or not. Takes ticket as user input and returns whether or not
the given ticket is lucky. """


def lucky_number():
    """Asks user for input of a lucky number and evaluates if it's lucky or not. """
    # remember that this ticket is still a string.
    ticket = ask_for_user_input()
    # get the length of the ticket.
    ticket_length = len(ticket)
    # get length of half the ticket
    half_ticket_length = int(ticket_length/2)
    # initialize a holder for each number in the first half of the ticket and the second half of the ticket.
    first_half = 0
    second_half = 0
    # get the sum of first half of the ticket's numbers
    for i in ticket[:half_ticket_length]:
        first_half += int(i)
    # get the sum of the second half of the ticket's numbers
    for i in ticket[half_ticket_length:]:
        second_half += int(i)
    # divide by number of numbers in first half to get the average, do the same for the second half.
    first_half_average = first_half/half_ticket_length
    second_half_average = second_half/half_ticket_length
    # now see if they're equal to each other.
    if first_half_average == second_half_average:
        return "You have a lucky ticket, congratulations!"
    else:
        return "You don't have a lucky ticket, try again!"


def ask_for_user_input():
    """Asks for user to input a ticket number and checks that it's valid."""
    correct_input = False
    while not correct_input:
        # get the ticket from the user.
        ticket = input("Please input your ticket number: ")

        # initialize counter
        counter = 0
        # if the length of the ticket is divisible by two and is still an integer (even number) then return the ticket.
        for i in ticket:
            counter += 1
        # if the remainder of floor division is 0 return ticket
        if (counter % 2) == 0:
            correct_input = True
            return ticket


def main():
    """Main function that runs our code."""
    print(lucky_number())


# entry point.
if __name__ == "__main__":
    main()
