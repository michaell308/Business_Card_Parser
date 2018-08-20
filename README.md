# Entegra Coding Challenge - Business Card Parser

### How to run:

1) Install necessary dependencies
	```
	pip install numpy
	pip install nltk
	```

2) Run using python (main.py contains unit tests)
	```
	python main.py
	```

### Documentation:

The BusinessCardParser extracts ContactInfo (name, phone number, email address) from a string representing information on a business card.

#### Example Usage:
```
from BusinessCardParser import BusinessCardParser

businessCardInfo = "Entegra Systems
John Doe
Senior Software Engineer
(410)555-1234
john.doe@entegrasystems.com"

ci = BusinessCardParser.getContactInfo(businessCardInfo) 
ci.getName() #John Doe
ci.getPhoneNumber() #4105551234
ci.getEmail() #john.doe@entegrasystems.com
```

#### Name:
The name extraction is done using nltk. Each line in the given string is split into chunks. Each chunk labeled as a 'PERSON' is stored in a list of people. Then, we iterate through each line to tally points. For each people entry contained in the line, that line gains a point.
Example:
```
people=['John','Doe','Software']
John Doe => 2 points (one for 'John' and one for 'Doe')
Senior Software Engineer => 1 point (one for 'Software')
(410)555-1234 => 0 points
```
The line with the most points is returned as the name. If all the lines have 0 points, then an empty string will be returned instead.

#### Phone Number:
The phone number extraction handles many cases, including:
* 4105551234
* (410)5551234
* (410)555-1234
* (410)-555-1234
* (410) - 555 - 1234
* Tel: +1 (410) 555-1234

The extraction is done using a regular expression: 
* any text(?): accounts for prepended text like 'Tel:' or 'Phone:'
* left parenthesis(?)
* 3 digits: area code
* right parenthesis(?)
* 0 to 3 non-digits: hypen or space/hypen/space
* 3 digits: first three digits of the phone number
* 0-3 non-digits: hypen or space/hypen/space
* 4 digits: last four digits of the phone number

If no phone number is found, then the phone number will be an empty string

#### Email Address:
The email address is extracted by taking the first line that contains an '@' symbol
If no '@' symbol is found, then the email address will be an empty string