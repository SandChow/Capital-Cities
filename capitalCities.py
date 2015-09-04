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
if __name__ == "__main__":
    while True:
        country = raw_input("Key in the country or quit to exit: ").capitalize()
        if country == "quit":
            break
        countryCapital = capitalOf()
        if country in capitalOf():
            capital = countryCapital[country]
            print "The capital is " + capital + "."
        else:
            print "Unknown."




