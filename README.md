### About

This repo contains a simple script I wrote to parse the data from https://www.gov.uk/government/statistical-data-sets/car-theory-test-data-by-test-centre into a more usable format which can be used for data science.

##### Why?

I have started to learn Power BI in my job and a colleague of mine linked me to https://datasetsearch.research.google.com where i did a random search and the [DVLAs](https://en.wikipedia.org/wiki/Driver_and_Vehicle_Licensing_Agency) data showed up and I challenged myself to use this data. This data is not formatted to be used in Power BI hence this script. Some of the data I'm not including because i don't trust it and i can use Power BI to work it out such the totals.

##### How?

1. I started off by looking at what data was there and how it was laid out. Sheets per year and how the locations where grouped together
2. I then began by pulling all of the data into CSV files which can be easily used in python. I did this by searching around and finding a [marco script](scripts/exportPages.vbs) this script loops through all of the sheets and exports them as CSVs into a chosen directory
3. I then started to learn python again after years of not using it. This started out by trying out getting the list of files in a directory.
4. Then I started to process the data. Looping over the rows, removing empty rows and ignore the first few rows of text (I hardcoded the column names) and finally splitting the row by `,`
5. I added testing to see if the row was a location row and then set a location variable, this was used for the column and testing another row.
6. Then began testing to see if the first cell was the same as the location as that would show it was the end of a block and would contain the totals (which i have ignored)
7. Finally i then added the row along with the location into an array joined together with `,`
8. This process was looped over for all of the files generated from the macro script and was added to a master array which was then finally saved to output.csv
