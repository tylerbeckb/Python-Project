"""
Please write your name
@author: Tyler Brown

"""

import csv


class Leopard:
    def __init__(self, filepath: str) -> None:
        # Attributes
        self.header = []
        self.data = []
        self.is_found = True
        try:
            # Opens the csv file
            with open(filepath, "r") as csv_file:
                self.csvreader = csv.reader(csv_file)
                # Checks if the file is empty
                self.is_empty = csv_file.read(1)
                if not self.is_empty:
                    print(self.is_empty)
                    print("empty file")
                else:
                    # Reads are the beginning of the file
                    csv_file.seek(0)
                    # Adds the header into a list
                    self.header = next(self.csvreader)
                    # Reads the file and adds the data to a list
                    reader = csv.reader(csv_file)
                    self.data = list(reader)
        # Checks if the file is not found
        except FileNotFoundError:
            print("file not found.")
            self.is_found = False

    def get_header(self) -> list:
        if not self.is_found or not self.is_empty:
            return None
        return self.header

    def get_data(self) -> list:
        if not self.is_found or not self.is_empty:
            return None
        return self.data

    def stats(self) -> dict:
        # Sets variables
        stats_dict = {}
        len_people = len(self.data)
        count = -1
        # Iterates through all elements in header
        for i in self.header:
            total = 0
            count = count + 1
            counter = 0
            is_int = False
            # Iterates through all the people
            for z in range(len_people):
                # Checks if the col has int values
                try:
                    is_int = True
                    counter = counter + 1
                    digit = int(self.data[z][count])
                    total = total + digit
                except ValueError:
                    is_int = False
            # Creates a dictionary to go in the dictionary
            if is_int:
                stats_dict[i] = {'count': 0, 'mean': 0, 'min': 0, 'max': 0}
                # Adds the number of people
                stats_dict[i]['count'] = counter
                # Rounds the mean
                total = total / counter
                total = round(total, 2)
                # Adds the mean
                stats_dict[i]['mean'] = total
                # Iterates through all the people
                value_list = []
                for people in range(len_people):
                    # Checks if the space is blank
                    if self.data[people][count] == '' \
                            or self.data[people][count] == 'NA':
                        continue
                        # Adds values to a list
                    else:
                        value_list.append(int(self.data[people][count]))
                # Adds the min and max to the dictionary
                stats_dict[i]['min'] = min(value_list)
                stats_dict[i]['max'] = max(value_list)
        return stats_dict

    def html_stats(self, stats: dict, filepath: str) -> None:
        # delete pass and this comment to write your code
        with open(filepath, 'w') as html:
            # html style tags
            html.write("<html>\n")
            html.write("<head>\n")
            html.write("<meta charset=\"UTF-8\">\n")
            html.write("<style>\n")
            html.write("table, th, td {\n")
            html.write("border: 1px solid black; \n")
            html.write("}\n")
            html.write("</style>\n")
            html.write("<table>\n")
            # Creates the headers in the table
            html.write("<tr>\n")
            html.write("<th> Column</th>\n ")
            html.write("<th> Count</th>\n")
            html.write("<th> Mean</th>\n")
            html.write("<th> Min</th>\n")
            html.write("<th> Max</th>\n")
            html.write("</tr>\n")
            # Iterates through all the elements in stats
            for row in stats:
                html.write("<tr>\n")
                # Writes the name of the row
                html.write("<td>" + row + "</td>\n")
                # Writes count
                count = str(stats[row]['count'])
                html.write("<td>" + count + "</td>\n")
                # Writes mean
                mean = str(stats[row]['mean'])
                html.write("<td>" + mean + "</td>\n")
                # Writes min
                min_dig = str(stats[row]['min'])
                html.write("<td>" + min_dig + "</td>\n")
                # Writes max
                max_dig = str(stats[row]['max'])
                html.write("<td>" + max_dig + "</td>\n")
            # Close tags
            html.write("</table>\n")
            html.write("</head>\n")
            html.write("</html>\n")

    def count_instances(self, criteria: dict) -> int:
        """
        Takes criteria as a dictionary with the header as the key and
        criteria a value.
        It is case-sensitive. For example, criteria { 'Age': 20 }.
        This function returns the number of people that meet the criteria
        For example if the criteria was { 'Age' : 20 , 'Gender' : 'Male' }
        it would output the number of people that are a 20 years old male.
        An integer doesn't have to be a string in the dictionary but
        character has to be put in as a string.
        Same data type as the csv file to be put in the dictionary
        """
        # Iterates through all elements in dictionary

        values_list = self.data
        new_values = []
        # Loops through the dictionary
        for i in criteria:
            found = False
            count = 0
            # Iterates through header
            for header in self.header:
                if header == i:
                    found = True
                if not found:
                    count = count + 1
            # Iterates through all the data
            for people in values_list:
                str_criteria = str(criteria[i])
                # Checking if it matches the criteria
                if people[count] == str_criteria:
                    new_values.append(people)
            values_list.clear()
            values_list = new_values
            new_values = []
        return len(values_list)


if __name__ == "__main__":
    # test diabetes_data.csv
    test = Leopard("diabetes_data.csv")
    # print(test.get_header())
    # print(test.get_data())
    # stats = test.stats()
    # print(stats)
    # test.html_stats(stats, "diabetes.html")
    # print()

    # test fide2021.csv
    # test2 = Leopard("fide2021.csv")
    # print(test2.get_header())
    # print(test.get_data())
    # stats2 = test2.stats()
    # print(stats2)
    # test2.html_stats(stats2, "fide2021.html")
    # print()

    # test student.csv
    # test3 = Leopard("student.csv")
    # print(test3.get_header())
    # print(test.get_data())
    # stats3 = test3.stats()
    # print(stats3)
    # test3.html_stats(stats3, "student.html")
