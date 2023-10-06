"""
Introduction to Programming: Coursework 1
Please write your name
@author: Tyler Brown

"""


# Reminder: You are not allowed to import any modules.


def wordsearch(puzzle: list, wordlist: list) -> None:
    # checks if puzzle and wordlist is valid
    if valid_puzzle(puzzle) and valid_wordlist(wordlist):
        # displays the solution
        final_list = []
        # iterates through words in word list
        for word in wordlist:
            # gets each words position
            temp = get_positions(puzzle, word)
            if temp is not None:
                # adds the found index to a list
                final_list.append(temp)
        # displays the found words in puzzle
        coloured_display(puzzle, final_list)
    else:
        # displays an error if the word list or puzzle isn't valid
        print("ValueError, invalid puzzle or wordlist")
    pass


def valid_puzzle(puzzle: list) -> bool:
    length = len(puzzle[0])
    # iterates through the list for each index
    for x in puzzle:
        # checks if each index is a string
        if isinstance(x, str):
            # makes each index in the list upper case
            x.upper()
            # checks the length for each index
            if len(x) != length:
                return False
        else:
            return False
    return True


def valid_wordlist(wordlist: list) -> bool:
    check = True
    # loops through all index in the list
    for x in wordlist:
        # checks if it is not a string
        if not isinstance(x, str):
            check = False
    # if all index is a string it returns true
    if check:
        return True
    else:
        return False


def get_positions(puzzle: list, word: str) -> list:
    # finds length of the parameter word
    word = word.upper()
    length = len(word)
    y = -1
    # creates the list to be returned
    index_list = []
    my_dict = {}
    number_found = 0
    # iterates through all the rows
    for x in puzzle:
        y = y + 1
        z = -1
        # iterates through all the columns
        for i in x:
            count = 0
            z = z + 1
            # validates that only valid data goes through the code
            try:
                # checks if first  character is the same as the first character on word
                if i == word[count]:
                    count = 1
                    # creates variables needed for movement of the grid
                    down = puzzle[(y + 1)]
                    up = puzzle[(y - 1)]
                    # checks if the character on the right is the same as the 2nd character for word
                    if x[z + 1] == word[count]:
                        # adds the index of the first character to a tuple in a list
                        index_list.append(tuple((y, z)))
                        temp_z = z + 2
                        count = count + 1
                        # adds the index of matching character to a tuple in a list
                        index_list.append(tuple((y, (z + 1))))
                        # keeps checking the right characters until the word is found or a character is no the same
                        while count <= length:
                            # checks if characters is the same
                            if x[temp_z] == word[count]:
                                # adds index to the list as a tuple
                                index_list.append(tuple((y, temp_z)))
                                # changes the temporary index on z by 1 to move on to another value
                                temp_z = temp_z + 1
                                count = count + 1
                            else:
                                # clears the list word is not found
                                index_list.clear()
                                break
                            # checks if the word has been found
                            if count == length:
                                number_found = number_found + 1
                                # adds the index to a dictionary 
                                my_dict[number_found] = []
                                my_dict[number_found] += index_list
                    count = 1
                    # checks characters to the left
                    if x[(z - 1)] == word[count]:
                        # adds index to the list as a tuple
                        index_list.append(tuple((y, z)))
                        temp_z = z - 2
                        count = count + 1
                        # adds index to the list as a tuple
                        index_list.append(tuple((y, (z - 1))))
                        # loops checking each left character
                        while count <= length:
                            if x[temp_z] == word[count]:
                                # adds index to the list as a tuple
                                index_list.append(tuple((y, temp_z)))
                                temp_z = temp_z - 1
                                count = count + 1
                            else:
                                # clears the list
                                index_list.clear()
                                break
                            if count == length:
                                number_found = number_found + 1
                                my_dict[number_found] = []
                                my_dict[number_found] += index_list
                    count = 1
                    # checks characters downwards
                    if down[z] == word[count]:
                        # adds index to the list as a tuple
                        index_list.append(tuple((y, z)))
                        temp_y = y + 2
                        count = count + 1
                        # adds index to the list as a tuple
                        index_list.append(tuple(((y + 1), z)))
                        # loops checking each down character
                        while count <= length:
                            # sets down to the next row
                            downward = puzzle[temp_y]
                            if downward[z] == word[count]:
                                # adds index to the list as a tuple
                                index_list.append(tuple((temp_y, z)))
                                temp_y = temp_y + 1
                                count = count + 1
                            else:
                                # clears the list
                                index_list.clear()
                                break
                            if count == length:
                                number_found = number_found + 1
                                my_dict[number_found] = []
                                my_dict[number_found] += index_list
                    count = 1
                    # checks characters upwards
                    if up[z] == word[count]:
                        # adds index to the list as a tuple
                        index_list.append(tuple((y, z)))
                        index_list.append(tuple(((y - 1), z)))
                        temp_y = y - 2
                        count = count + 1
                        # loops through characters upwards
                        while count <= length:
                            # sets up as the new row
                            upward = puzzle[temp_y]
                            # checks character to the corresponding character for word
                            if upward[z] == word[count]:
                                # adds index to the list as a tuple
                                index_list.append(tuple((temp_y, z)))
                                temp_y = temp_y - 1
                                count = count + 1
                            else:
                                # clears the list
                                index_list.clear()
                                break
                            if count == length:
                                number_found = number_found + 1
                                my_dict[number_found] = []
                                my_dict[number_found] += index_list
                    count = 1
                    # checks characters of the bottom right
                    if down[(z + 1)] == word[count]:
                        # adds index to the list as a tuple
                        index_list.append(tuple((y, z)))
                        index_list.append(tuple(((y + 1), (z + 1))))
                        temp_y = y + 2
                        temp_z = z + 2
                        count = count + 1
                        # loops through checking each character
                        while count <= length:
                            bottom_right = puzzle[temp_y]
                            if bottom_right[temp_z] == word[count]:
                                index_list.append(tuple((temp_y, temp_z)))
                                temp_y = temp_y + 1
                                temp_z = temp_z + 1
                                count = count + 1
                            else:
                                # clears list
                                index_list.clear()
                                break
                            if count == length:
                                number_found = number_found + 1
                                my_dict[number_found] = []
                                my_dict[number_found] += index_list
                    count = 1
                    # checks characters in the bottom left
                    if down[(z - 1)] == word[count]:
                        # adds index to the list as a tuple
                        index_list.append(tuple((y, z)))
                        index_list.append(tuple(((y + 1), (z - 1))))
                        temp_y = y + 2
                        temp_z = z - 2
                        count = count + 1
                        # loops through each character in the direction
                        while count <= length:
                            # sets the variable to the new row
                            bottom_left = puzzle[temp_y]
                            if bottom_left[temp_z] == word[count]:
                                # adds index to the list as a tuple
                                index_list.append(tuple((temp_y, temp_z)))
                                temp_y = temp_y + 1
                                temp_z = temp_z - 1
                                count = count + 1
                            else:
                                # clears list
                                index_list.clear()
                                break
                            if count == length:
                                number_found = number_found + 1
                                my_dict[number_found] = []
                                my_dict[number_found] += index_list

                    count = 1
                    # checks characters in the top right
                    if up[(z + 1)] == word[count]:
                        # adds index to the list as a tuple
                        index_list.append(tuple((y, z)))
                        index_list.append(tuple(((y - 1), (z + 1))))
                        temp_y = y - 2
                        temp_z = z + 2
                        count = count + 1
                        # loops through characters in the direction
                        while count <= length:
                            top_right = puzzle[temp_y]
                            if top_right[temp_z] == word[count]:
                                # adds index to the list as a tuple
                                index_list.append(tuple((temp_y, temp_z)))
                                temp_y = temp_y - 1
                                temp_z = temp_z + 1
                                count = count + 1
                            else:
                                # clears list
                                index_list.clear()
                                break
                            if count == length:
                                number_found = number_found + 1
                                my_dict[number_found] = []
                                my_dict[number_found] += index_list
                    count = 1
                    # checks characters top left
                    if up[(z - 1)] == word[count]:
                        # adds index to the list as a tuple
                        index_list.append(tuple((y, z)))
                        index_list.append(tuple(((y - 1), (z - 1))))
                        temp_y = y - 2
                        temp_z = z - 2
                        count = count + 1
                        # loops through characters in the direction
                        while count <= length:
                            top_left = puzzle[temp_y]
                            if top_left[temp_z] == word[count]:
                                # adds index to the list as a tuple
                                index_list.append(tuple((temp_y, temp_z)))
                                temp_y = temp_y - 1
                                temp_z = temp_z - 1
                                count = count + 1
                            else:
                                # clear list
                                index_list.clear()
                                break
                            if count == length:
                                number_found = number_found + 1
                                my_dict[number_found] = []
                                my_dict[number_found] += index_list

            except IndexError:
                # moves on to the next index in there is an IndexError
                continue
    # checks if word is found
    if number_found > 0:
        # converts the dictionary in a list, removing the keys
        new_list = list(my_dict.values())
        # returns the list of the index of the found words
        return new_list
    else:
        # adds quotation marks around the word
        result = f"'{word}'"
        # outputs the message
        print(result, 'not found.')


def basic_display(grid: list) -> None:
    # loops through the list
    for x in grid:
        new_grid = ""
        # loops through all the characters in each index
        for i in x:
            # adds it to a new variable to add the spaces
            new_grid = new_grid + " " + i
        print(new_grid.upper())
    pass


def coloured_display(grid: list, positions: list) -> None:
    count = -1
    new_grid = []
    word_count = []
    count_list = []
    # finds the length of the rows
    length = len(grid[0])
    # iterates through the rows in the grid
    for p in grid:
        # iterates through the letters in each row
        for b in p:
            # adds them to separate index in a new list
            new_grid.append(b)
            # for each letter adds 1 to a new list
            # needed so the grid can be displayed inline
            count_list.append(1)
            # iterates through all the word index
    for v in positions:
        # gets the length of the word
        word_count.append(len(v))
    # iterates through all the words
    for x in word_count:
        count = count + 1
        # iterates through all the word index
        for i in positions[count]:
            for a in positions[count][0]:
                temp_y = a[0]
                temp_z = a[1]
                y = -1
                counter = -1
                # iterates through all the letters in grid
                for letter_y in grid:
                    y = y + 1
                    z = -1
                    for letter_z in letter_y:
                        z = z + 1
                        counter = counter + 1
                        # compares the index for the word and index of letters in the grid
                        if temp_z == z and temp_y == y:
                            # changes the background to green
                            new = f"\033[42m {grid[temp_y][temp_z]} \033[0m "
                            # changes the original letter to the same but with a green background
                            new_grid[counter] = new
                            # changes a 1 for a 2 in the same position
                            count_list[counter] = 2
    row_count = 0
    space_counter = -1
    # iterates through all the letters
    for i in new_grid:
        space_counter = space_counter + 1
        # if reaches the end of a row create a new line
        if row_count == length:
            print('')
            row_count = 0
        if count_list[space_counter] == 2:
            # the background has a larger border therefore for every letter to be inline needs to be a smaller gap
            # between background and letters
            print(i, end=' ')
        else:
            # adds larger space for letters next to letters
            print(i, end='    ')
        row_count = row_count + 1

# =============================================================================
# Do not remove the followings. To test your functions
# =============================================================================


def test_valid_wordlist():
    """
    Test function valid_wordlist()
    """
    good_wordlist = ["scalar", "tray", "blew", "sevruc", "testing"]
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    bad_wordlist2 = ["scalar", "tray", "blew", "sevruc", 59]

    print("wordlist is", valid_wordlist(good_wordlist))
    print("wordlist is", valid_wordlist(good_wordlist2))
    print("wordlist is", valid_wordlist(bad_wordlist2))


def test_valid_puzzle():
    good_puzzle = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle1 = ['RUNAROUNDDL', 'EDCITOAHC', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle2 = ['RUNAROUNDDL', ['EDCITOAHCYV'], ('ZYUWSWEDZYA'),
                   'AKOTCONVOYV', 'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL',
                   'ISTREWZLCGY', 'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    print("puzzle is", valid_puzzle(good_puzzle))
    print("puzzle is", valid_puzzle(bad_puzzle1))
    print("puzzle is", valid_puzzle(bad_puzzle2))


def test_basic_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    basic_display(puzzle1)
    basic_display([['a', 'b', 'c', 'd', 'e'], ['h', 'l', 'j', 'k', 'l']])


def test_get_positions():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    get_positions(puzzle1, "TESTING")
    print(get_positions(puzzle1, "TRAY"))


def test_coloured_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    final_list = []
    for word in good_wordlist2:
        temp = get_positions(puzzle1, word)
        if temp is not None:
            final_list.append(temp)
    coloured_display(puzzle1, final_list)


def test_wordsearch():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    wordsearch(puzzle1, good_wordlist2)


if __name__ == "__main__":
    # uncomment the test function individually
    # basic solution
    # test_valid_puzzle()
    # test_valid_wordlist()
    # test_basic_display()

    # full solution
    # test_coloured_display()
    # test_get_positions()
    test_wordsearch()
