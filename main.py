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


ignoreRows = [0, 1, 2, 3]
usedMonths = ["jan", "feb", "mar", "apr", "may",
              "jun", "jul", "aug", "sep", "oct", "nov", "dec"]


def parseTable(inputTable):
    file = open("./data/" + inputTable, "r")
    rows = file.readlines()
    file.close()

    table = []

    rows = list(filter(lambda item: re.search("[^,\\n\s]+", item), rows))

    rows.pop(len(rows) - 1)  # Removing the National Figures row

    currentLocation = ""

    for i in range(len(rows)):
        if (i in ignoreRows):  # Ignoring the few rows
            continue
        row = rows[i].replace("\n", "")

        cells = row.split(",")  # Splitting the row into cells

        if (cells[0] == "Jan-Mar 2021"):  # Ignoring combined months
            continue

        if ("Total tests" in cells):
            continue

        if (cells[1] == "" and not checkMonth(cells[0])):  # If the row is a month row
            currentLocation = cells[0]
            continue  # If the row has only one item, it is the start of a location

        if (cells[0] == currentLocation):
            continue  # If the row is not empty and the first item is the location, it the total for the location
        date = cells.pop(0)  # Removing the date from the cells

        # Removing empty cells
        cells = list(filter(lambda item: item != " " and item != "", cells))

        table.append(",".join([date, currentLocation, *cells]))
    return table


def checkMonth(cell):
    #  month = cells[0].lower().split("-")[0]
    found = False
    for month in usedMonths:
        if (cell.lower().startswith(month)):
            found = True
            break
    return found


main()
