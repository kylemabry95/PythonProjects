"""
Kyle Mabry
76361438
I worked alone and with no help.
"""


def detect_name(file):
    """Extracts the first line of a file and returns the name listed on the first line. If the first character
    of the name isn't uppercase this function will return a runtime error."""

    # open the file and store it to memory.
    with open(file) as fin:
        our_file = fin

        # reads the first line in the file, which should be the name. readline puts "\n" at the end of the line.
        first_line_name = our_file.readline()

        # strip the first line of any whitespace.
        first_line_name = first_line_name.strip()

        # if the first character in the first line isn't a capital letter, 0 corresponds to the first letter in str.
        if first_line_name[0] != first_line_name[0].capitalize():
            raise RuntimeError("The first line has to be a name with proper capitalization. " +
                               first_line_name + ", is not a valid name")

    return first_line_name


def detect_email_address(file):
    """Finds the line in a file that contains an email address. This function returns the email address as a string."""

    with open(file) as fin:
        our_file = fin

        # get the lines in the file.
        lines = our_file.readlines()

        # initialize test/check variables
        dot_com_or_edu = False
        at_symbol = False
        is_not_number = False
        # initialize this just in case our resume doesn't have an email line.
        line_with_email = None

        # find the @ symbol that indicates a potential email address.
        # For each line in the file, if file is iterable.
        for line in lines:
            # for each character in the current line
            for character in line:
                # if the character we're looking at is equal to @
                if character == '@':
                    # save that current line
                    line_with_email = line
                    # update one of our test variables.
                    at_symbol = True
                    break  # if we find the at symbol end the loop.

        # checking to see that we don't have a number in our email address.
        if line_with_email is not None:
            # for each character in the line.
            for character in line_with_email:
                # check to make sure that the email address doesn't contain numbers.
                if character.isnumeric():
                    # if the current character we're looking at is equal to a number return None for email.
                    return None
                # otherwise, our current character wasn't equal to a number
                else:
                    is_not_number = True

        if line_with_email is not None:
            # make sure the ending of the email address has .com or .edu iterate over last four characters.
            dot_split_line_with_email = line_with_email.split('.')
            # get the length of the list that we just created
            length_dot_split_line_with_email = len(dot_split_line_with_email)
            # last index in length_dot_split_line_with_email
            last_index = length_dot_split_line_with_email - 1
            # if the last split element is equal to .com or .edu
            if dot_split_line_with_email[last_index] == 'com\n' or dot_split_line_with_email[last_index] == 'edu\n':
                # set our check variable to true.
                dot_com_or_edu = True

        # if we pass all three checks.
        if dot_com_or_edu and at_symbol and is_not_number:
            # return the line with the email without any whitespace.
            return line_with_email.strip()
        # if any fail return None.
        else:
            return None


def detect_courses(file):
    """Looks for the word courses in a file and returns the lines that contain the word courses as a single string."""

    with open(file) as fin:
        our_file = fin

        # get all lines in our file using .readlines()
        lines = our_file.readlines()

        # create a new list for each line that contains the word courses.
        courses = []

        # for each line in the file look for the word "courses"
        for string in lines:
            # strip any whitespace
            string = string.strip()
            # split each sentence into separate words based on where spaces are, make words a list.
            words = string.split(" ")
            # for each word in a sentence list of words
            for word in words:
                # if the current word is equal to Courses.
                if word == 'Courses':
                    # save the courses as a list of words to the list courses.
                    courses.append(words)

        # get each "sentence" in the list called courses
        for sentence in courses:
            # initialize counter for each sentence
            new_sentence = []
            # for each word in the sentence.
            for word in sentence:
                # strip the whitespace just to be sure.
                word = word.strip()
                # if we have random punctuation after the word courses, can we exclude courses?
                # also get rid of white space/empty space.
                if word != ':-' and word != '-' and word != 'Courses' and word != '':
                    # make the new sentence
                    new_sentence.append(word)
        # make a second word list for a second time filtering.
        new_sentence2 = []
        # for each word in our new sentence
        for word in new_sentence:
            # split the word on the \t
            word = word.split("\t")
            # for each item in our new list.
            for item in word:
                # filter out the remaining garbage, nice trick.
                if item != ':-' and item != '-' and item != 'Courses' and item != '' and item != ',':
                    # append the word to our new sentence.
                    new_sentence2.append(item)

        # join the list of words into a single string with one space between each word.
        new_sentence = ' '.join(new_sentence2)
        # strip the "\n" character.
        new_sentence = new_sentence.strip("\n")
        print(new_sentence)

        # return the courses and strip any whitespace.
        return new_sentence.strip()


def detect_projects(file):
    """Looks for the word projects in a file and returns the subsequent lines, which are the projects.
    Returns each line after the word projects in a list and stops after encountering a line with ten dashes. """

    # open our file as fin.
    with open(file) as fin:

        # save the file to our computers memory.
        our_file = fin

        # get each line in the file using .readlines(), produces a list.
        lines = our_file.readlines()

        # initialize some checking variables.
        found_projects = False
        project_line_counter = 0

        # while we haven't come across the word 'Projects'.
        while not found_projects:
            # for each sentence in our list of lines.
            for sentence in lines:
                # update the current index counter.
                project_line_counter += 1
                # split the sentence into a list of words on the whitespace.
                sentence = sentence.split(' ')
                # if we've already found the word projects, break this for loop.
                if found_projects:
                    break
                # otherwise, for each word in the list
                for word in sentence:
                    # again, if we've already found our project break this loop.
                    if found_projects:
                        break
                    # if the word that we're looking at is equal to Projects, or is equal to projects with a new line.
                    if word == 'Projects' or word == 'Projects\n':
                        # update found_projects to True.
                        found_projects = True
                        # subtract one from the project_line_counter.
                        project_line_counter -= 1
                        # break out of this for loop.
                        break

        # initialize a list and some testing variables.
        project_lines = []
        ten_dashes = False
        dash_counter = 0

        # while the current line doesn't contain ten dashes.
        while not ten_dashes:
            # for each line in the slice of the lines that we're now looking at. Using the project_line_counter.
            for line in lines[project_line_counter:]:
                # if we've already encountered ten_dashes break.
                if ten_dashes:
                    break
                # otherwise, for each word in the line we're looking at.
                for word in line:
                    # split each work up into a list of characters.
                    word = word.split()
                    # for each character in the word.
                    for characters in word:
                        # if the character is equal to a dashed line
                        if characters == '-':
                            # update the dashed line counter.
                            dash_counter += 1
                        # once our counter gets to ten
                        if dash_counter == 10:
                            # say that we've seen ten dashes.
                            ten_dashes = True
                            # break out of the most recent for loop.
                            break
                # if we haven't encountered ten dashes yet.
                if not ten_dashes:
                    # remove any whitespace in the line
                    line = line.strip()
                    # add the current line to the project_lines.
                    project_lines.append(line)

        # rejoin the list of strings on the newline command.
        project_lines = '\n'.join(project_lines)
        # Create a list of separate projects.
        project_lines = project_lines.split("\n")
        # Make sure none of the project lines are blank, if they are ignore them.
        not_empty_project_lines = [line for line in project_lines if line.strip() != ""]

    # returns each line after the word projects and stops after encountering a line with ten dashes.
    return not_empty_project_lines


def surround_block(tag, text):
    """This function takes the given text and surrounds it with the given HTML tag. It returns the string."""

    # create the back tag
    back_tag = "<" + tag + ">"
    # create the front tag
    front_tag = "</" + tag + ">"
    # create the entire formatted text string.
    surrounded_text = back_tag + text + front_tag

    # return the string with tags attached.
    return surrounded_text


def list_to_string(our_list):
    """Takes a given list and converts it to a string. Especially useful for rejoining separated words."""

    # Determine how we want to space each character, in this case no space.
    separator = ""

    # returns the joined list as a string. We need to assign a variable to hold the output of this function.
    return separator.join(our_list)


def create_email_link(email_address):
    """This function creates an email link in html format given the input email address."""

    # Create a new list that will contain each character in the email address.
    new_email = []
    # if the email address doesn't exist return None.
    if email_address is None:
        return None
    # for each character in the given email address.
    for character in email_address:
        # if the character we're looking at is equal to "@", then replace it with "aT"
        if character == "@":
            character = "[aT]"
            # add this new character to the list.
            new_email.append(character)
        else:
            # otherwise, add each character to the list we created.
            new_email.append(character)
    # join our new email from a list to a string.
    new_email = list_to_string(new_email)

    # return the result in html format for an active email address.
    return "<a href=\"mailto:" + email_address + "\">" + new_email + "</a>"


def write_intro_section(file):
    """Writes the introduction (basic information section) of our resume. First name and an active email link."""

    # create inner first by finding email.
    email = create_email_link(detect_email_address(file))
    # if email doesn't exist leave it blank.
    if email is None:
        email = ""
    # create next layer now
    email_surrounded = surround_block("p", "Email: " + email)
    # create the header with the name.
    header_with_name = surround_block("h1", detect_name(file))
    # put it all together within "div" now.
    intro = surround_block("div", "\n" + header_with_name + email_surrounded + "\n")

    return intro


def write_projects_section(file):
    """Writes the projects section of our resume. """

    # get the lines of the projects and assign to list variable.
    project_lines = detect_projects(file)
    # surround the word projects with the appropriate header.
    project_surrounded = surround_block("h2", "Projects")
    # initialize new list.
    projects_surrounded = []
    # for each line in the project list, surround the text with the appropriate headers and append to new list.
    for line in project_lines:
        projects_surrounded.append(surround_block("li", line))
    # rejoin the projects from a list to a single string on the newline command.
    projects_surrounded = "\n".join(projects_surrounded)
    # surround all projects with the appropriate header.
    projects_surrounded_final = surround_block("ul", "\n" + projects_surrounded + "\n")
    # concatenate the projects section into a single string.
    projects_section = surround_block("div", "\n" + project_surrounded + "\n" + projects_surrounded_final + "\n")

    return projects_section


def write_courses_section(file):
    """writes the courses section of our resume. Includes the necessary surrounding text."""

    # get the courses as string.
    courses = detect_courses(file)
    # surround the word Courses with the appropriate header.
    course_surrounded = surround_block("h3", "Courses")
    # Surround the projects with the appropriate header.
    courses_surrounded = surround_block("span", courses)
    # concatenate the courses section into a single string.
    courses_section = surround_block("div", "\n" + course_surrounded + "\n" + courses_surrounded + "\n")

    return courses_section


def remove_last_two_lines_in_html(file_lines):
    """Removes the last two lines in the given lines list from an html file. Makes sure that the last two lines
    contain </body> and </html> before removing them. This function also adds the </div id="page-wrap">."""

    # make sure that we have enough lines in our file_lines. We should, but just in case.
    if len(file_lines) >= 2:
        # delete last two lines from the file_lines.
        file_lines.pop()
        file_lines.pop()
        # now add the </div... line
        file_lines.append("</div id=\"page-wrap\">")

    # return file_lines
    return file_lines


def add_back_last_two_lines_in_html():
    """Adds back the last two lines in a given lines list from an html file,
    these lines will be: </body> and </html>."""

    # return the last three lines as a string.
    return "\n</div>" + "\n</body>" + "\n</html>"


def read_and_write_html_resume(html_file, new_resume_file, resume_file):
    """Programmatically opens an already defined html file, reads our resume from a text file and writes in our
    resume data into a second output file."""

    # now get the information we need from our resume_file and write it to our html file.
    # open our html file in read and write mode.
    resume_html_file = open(html_file, "r+")
    # read lines in file.
    resume_html_file_lines = resume_html_file.readlines()
    # remove last two lines in file and add the appropriate line back in.
    resume_html_file_lines = remove_last_two_lines_in_html(resume_html_file_lines)
    # write the introduction
    introduction = write_intro_section(resume_file)
    # write the projects section
    projects = write_projects_section(resume_file)
    # write the courses section
    courses = write_courses_section(resume_file)
    # append intro, projects and courses to resume_html_file_lines.
    resume_html_file_lines.append(introduction)
    resume_html_file_lines.append(projects)
    resume_html_file_lines.append(courses)
    # add the last three lines back in.
    resume_html_file_lines.append(add_back_last_two_lines_in_html())
    # make sure at the very end that we close template file.
    resume_html_file.close()
    # open our output file.
    read_new_resume_file = open(new_resume_file, "a")
    # add all of the lines into our new file.
    read_new_resume_file.writelines(resume_html_file_lines)
    # make sure at the very end that we close our new_resume_file.
    read_new_resume_file.close()


def main():
    """This is the main function that runs our code."""

    # read the resume template, get our resume information and then output new resume template with
    # updated info to a second html file.
    read_and_write_html_resume('resume_template.html', 'kyle_resume.html', 'mabry_resume.txt')


# entry point for our main function.
if __name__ == '__main__':
    main()
