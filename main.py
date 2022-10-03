import os
import re


def main():
    # Get the list of all files and directories
    dir_list = os.listdir("./data")

    data = [",".join(["date", "location", "male_conducted", "male_passes", "male_pass_rate", "female_conducted",
                      "female_passes", "female_pass_rate", "total_conducted", "total_passes", "total_pass_rate"])]

    for file in dir_list:
        data = data + parseTable(file)

    output = "\n".join(data)
    file = open("./output.csv", "w")
    file.write(output)


def parseTable(inputTable):
    file = open("./data/" + inputTable, "r")
    rows = file.readlines()
    file.close()

    table = []

    rows = list(filter(lambda item: re.search("[^,\\n\s]+", item), rows))

    rows.pop(len(rows) - 1)  # Removing the National Figures row

    ignoreRows = [0, 1, 2, 3]

    currentLocation = ""

    for i in range(len(rows)):
        if (i in ignoreRows):  # Ignoring the few rows
            continue
        row = rows[i]

        items = row.split(",")  # Splitting the row into items

        if (items[1] == ""):
            currentLocation = items[0]
            continue  # If the row has only one item, it is the start of a location

        if (items[0] == currentLocation):
            continue  # If the row is not empty and the first item is the location, it the total for the location
        date = items.pop(0)  # Removing the date from the items

        # Removing the last item which is the new line character
        items.pop(len(items) - 1)
        # Removing empty items
        items = list(filter(lambda item: item != " ", items))

        table.append(",".join([date, currentLocation, *items]))
    return table


main()
