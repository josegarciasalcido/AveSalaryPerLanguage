from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
import pandas as pd

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"

data  = requests.get(url).text # get the contents of the webpage in text format and store in a variable called data
soup = BeautifulSoup(data,"html5lib")  # create a soup object using the variable 'data'
#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>

# Initialize empty lists to store data
prog_languages = []
mean_ave_salaries = []


# Initialize a counter variable
row_counter = 0

for row in table.find_all('tr'): #Get all rows from the table
    cols = row.find_all('td')

    # Check if it's the header row (first row)
    if row_counter > 0:
        prog_language = cols[1].getText()
        Mean_Ave_Salary = cols[3].getText()

        prog_languages.append(prog_language)
        mean_ave_salaries.append(Mean_Ave_Salary)

        print("{}--->{}".format(prog_language, Mean_Ave_Salary))

    # Increment the counter variable
    row_counter += 1

# Create a DataFrame
df = pd.DataFrame({
    'Programming Language': prog_languages,
    'Mean Ave Salary': mean_ave_salaries })

# Print the DataFrame
print(df)


# Write the DataFrame to an Excel file
csv_file_path = 'popular-languages.csv'
df.to_csv(csv_file_path, index=False)
print(f"Job counts by location have been stored in {csv_file_path}")
