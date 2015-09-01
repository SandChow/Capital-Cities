import urllib
from bs4 import BeautifulSoup

# website is parsed and a dictionary is returned. Key = country and Value = capital.
def capitalOf():
    sourceCode = urllib.urlopen("http://www.manythings.org/vocabulary/lists/2/words.php?f=countries_and_capitals").read()
    parsedHTML = BeautifulSoup(sourceCode, 'html.parser')
    lists = parsedHTML.find_all("li")
    countryCapitalMapper = {}

    for each in lists:
        countryCapitalMapper[each.b.string] = each.i.string
    return countryCapitalMapper

# User is asked for input and if it is a known country, capital is printed. Otherwise, capital is unknown.
def whatIsTheCapital():
    country = raw_input("Key in the country: ").capitalize()
    countryCapitalMapper = capitalOf()
    if country in capitalOf():
        capital = countryCapitalMapper[country]
        print "The capital is " + capital + "."
    else:
        print "Unknown."

whatIsTheCapital()




