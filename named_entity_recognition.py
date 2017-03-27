from nltk import word_tokenize, pos_tag, ne_chunk
import os, csv
import sys  
import codecs 
reload(sys)  
sys.setdefaultencoding('utf8')


test = "Bob jumped over the fence and then travelled to India"

print ne_chunk(pos_tag(word_tokenize(test)))

contents = codecs.open("techcrunch-posts-scraper/data/posts/2017_03_24__13_46_17.csv", "r","utf-8")


emails = []
counter = 0
for line in contents:
	counter += 1
	if counter > 7:
		break
	line2 = line.encode('utf8')
	chunks =  ne_chunk(pos_tag(word_tokenize(line2)))
	file = open("cur_chunks", "w")
	for i in chunks:
		file.write(str(i))
		file.write('\n')
	file.close()

	entities = []
	file = open("cur_chunks", "r")
	for line in file:
		if "PERSON" in line or "ORGANIZATION" in line:
			entities.append(line)

	print entities


	people = []
	organizations = []

	for i in entities:
		if len(i.split(' ')) >= 3 and i[1] == "P":
			j = i.split(' ')
			firstname = j[1].split('/')[0]
			lastname = j[2].split('/')[0]
			if [firstname, lastname] not in people:
				people.append([firstname, lastname])
		else:

			if i.split(' ')[1].split('/')[0] not in organizations:
				organizations.append(i.split(' ')[1].split('/')[0])


	print people
	print organizations
		
	hosts = []
	for i in organizations:
		j = i + ".com"
		hosts.append(j)

	for i in hosts:
		for j in people:
			emails.append(j[0] + "." + j[1] + "@" + i)
			emails.append(j[0][0] + j[1] + "@" + i)
			emails.append(j[0] + "@" + i)
			emails.append(j[0][0] + "." + j[1] + "@" + i)



for i in emails:
	print i

