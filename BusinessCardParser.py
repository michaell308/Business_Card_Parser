from ContactInfo import ContactInfo
import re
import nltk

class BusinessCardParser:

	#returns the line from 'text' that is most likely to be the name
	@staticmethod
	def extract_name(text):
		textList = [line for line in text.splitlines()]
		#add every chunk with a person label to the 'people' list
		people = []
		for sent in textList:
			for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
				if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
					people.append(chunk[0][0])
		#tally points for each line
		points = [0] * len(textList)
		for idx, line in enumerate(textList):
			for person in people:
				if person in line:
					points[idx]+=1
		maxPoints = max(points)
		#return line with most points (as it is most likely to be the name); or empty string if max points is 0
		return textList[points.index(maxPoints)] if maxPoints != 0 else ''

	#returns a ContactInfo obj that has a name, phone number, and email extracted from the given 'document' string
	@staticmethod
	def getContactInfo(document):
		#extract name
		name = BusinessCardParser.extract_name(document)

		#extract phone number using regular expression:
		#any text(?), left parenthesis(?), 3 digits, right parenthesis(?), 0 to 3 non-digits, 3 digits, 0-3 non-digits, 4 digits
		r = re.compile(r"(.*?\(?\d{3}\)?\D{0,3}\d{3}\D{0,3}\d{4})")
		foundPhoneNumber = r.search(document)
		#if a phone number was found, only keep the digits; otherwise phoneNumber is an empty string
		phoneNumber = re.sub("\D", "", foundPhoneNumber[0]) if foundPhoneNumber is not None else ''

		#extract email by taking first line that has an '@'
		emailAddress = ''
		for line in document.splitlines():
			if "@" in line:
				emailAddress = line
				break

		return ContactInfo(name,phoneNumber,emailAddress)
