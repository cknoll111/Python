# Visual Fortunte 500 Project
# lets a user enter a year and displays a graph of the Revenue for each of the top 15 Fortune 500 companies for that year.
# Import modules #

import matplotlib.pyplot as plt
import pandas as pd

# Define Functions #

def getDataByYear(df,year):
  # Filter by Year
  ndf = df.loc[df["Year"] == year, :]

# Filter by Top 15
  ndf = ndf.loc[ndf["Rank"] <= 15, :]

  return ndf

def drawGraph(df,title):
  df.plot.bar(x="Company", y="Revenue (in millions)", color='red')
  plt.title(f"Top 15 Companies in {userYear}")
  plt.show()  

# main program #
print("Welcome to Visual Fortune 500!")

df = pd.read_csv('fortune500.csv')

userYear = 0
userYear = int(userYear)

while ((userYear < 1955) or (userYear > 2005)):
  userYear = input("Please enter a year to view (between 1955 and 2005):")
  userYear = int(userYear)

# calling functions #
df = getDataByYear(df,userYear) 
drawGraph(df,f"Top 15 Companies in {userYear}") 