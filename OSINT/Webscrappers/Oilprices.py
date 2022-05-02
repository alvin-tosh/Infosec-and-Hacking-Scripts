#import module for parsing the data
from bs4 import BeautifulSoup
import statistics
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
#create a URL get function 
def getdata(url):
    r = requests.get(url)
    return r.text
#link for extracting html data
htmlurl = getdata("https://www.globalpetrolprices.com/gasoline_prices/")

soup = BeautifulSoup(htmlurl,'lxml')

#find the countryname, inspect table with id as 'outsidelinks'
country_name = soup.find_all('div', id='outsideLinks')
#find the date when the data was last updated
date = soup.select('h1')[0].text.strip()
#inspect the webpage and find the petrol price for the 170 countries
petrol_value = soup.find_all('div', id='graphic')

# Loop through the html and find all text/string with div tag and id=’outsideLinks’.
for country in country_name:
    # A bit of cleaning up
    cname = country.div.text.split('\n\n')
    cname = cname[1:-1]
    cname = [item.strip() for item in cname]
    cname = map(lambda s: s.replace("*", ""), cname)
    # Print (cname) :- list that contains the country name strings , look for further anomalies. We do find that for some countries it has an * . 
    # If there is an * next to a country than its data is updated weekly , and if there isn’t then it is updated once a month . 
    # Most of the countries without * have minimal fluctuation in their fuel prices. For the sake of analysis I’ve removed the “*” from the dataset

petrol_value = soup.find_all('div', id='graphic'
for price in petrol_value:
    petrol_price = price.div.text.split()
    petrol_price.pop()
    petrol_head = [float(i) for i in petrol_price]
)

# Write the data to an excel .

df = pd.DataFrame ({'Country': cname, 'Price': petrol_head}
df.to_excel('check.xlsx', index= False))

# Read data from excel.

sumstat = pd.read_excel('check.xlsx', sheet_name='Sheet1', header=None)

# Create summary statistics , and provide data for normal distribution using the cost (i.e. petrol_head ) and deriving mean & standard deviation . 
# Create an input variable and ask for user input . This is followed by some statistical analysis conditions
#Create summary statistic
#sort the data
sort = np.sort(petrol_head)
#mean rounded up to 3 decimals	
mu = round(np.mean(petrol_head), 3)
#mean Not needed but recorded anyway and rounded up to 3 decimals
median = round(np.median(petrol_head), 3)
#mode Not needed but recorded anyway and rounded up to 3 decimals
mode = round(statistics.mode(petrol_head), 3)
#Standard Deviation 
sigma = round(np.std(petrol_head), 3)
#Values for normal distribution 
#data that lies in the area between mean and one standard deviation to the right of the mean 
o_std = sigma + mu
#data that lies in the area between one standard deviation & two standard deviation to the right of the mean 
t_std = o_std + sigma
#data that lies in the area between mean and negative one standard deviation to the right of the mean
nv_mu_80 = mu - sigma
#data that lies in the area between -ve one standard deviation & two standard deviation to the right of the mean
nv_mu_95 = mu - nv_mu_80
#Print the world average petrol price and standard deviation
print(f'The average world gas price / liter in world is {mu} with σ {sigma}.')
#Ask for the user input 
q = input("Type your country's name to compare its gas prices against world:-  ")

try:
	#Loop through the index 0  which is country name & find a match and retrive the first value against it in column 1 in the excel.
    value = sumstat[sumstat[0] == q][1].values[0]
	#print the date provided in h1
    print(f'The {date} in {q}  is  : {value}''$')
	#condition to find the incermental/decremental  value in %
    if value > mu:
        print(q + "'s " + f"gas price at {value}$ is {(round(((value-mu)/value)*100))}% higher than world mean i.e.{mu}$")
    else:
        print(q + "'s " + f"gas price at {value}$ is{(round(((value-mu)/value)*100))}%  than world average price i.e.{mu}$")
        print("Review interactive normal distribution curve to find where your country lies  ")
    #condition to find where are value (i.e. gas price) lies in the normal distribution
	if value < o_std and value > mu:
        print(f'{q} is paying close to what 68% of the world is paying. ')
    if value < mu and value >nv_mu_80 :
        print(f'{q} is paying close to what 68% of the world is paying. ')
    elif value < nv_mu_80 and value > nv_mu_95 :
        print(f'{q} is paying less than what the 80% of the world is paying. ')
    elif value < nv_mu_95:
        print(f'{q} is paying less than what the 95% of the world is paying. ')
    elif value > o_std and value > mu and value < t_std:
        print(f'{q} is paying more than what the 80% of the world is paying. ')
    elif value > t_std and value > mu:
        print(f'{q} is paying more than what the 95% of the world is paying. ')
except IndexError:
    print('Name not found')

# Plot the data

#normal distribution curve plotting
sigma = np.std(petrol_head)
data = np.random.normal(mu, sigma, 170)
count, bins, ignored = plt.hist(data, 30, density=True, stacked=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
plt.title("Normal Distribution for  world gas (petrol) prices ")
plt.show()