import re
import math
import numpy as np



x = raw_input("Enter the first name and last name of the lead\n")

y = raw_input("Enter the possible domain of the lead's email. If not available, press Enter\n")




names = x.split(' ')

hosts = ["gmail.com", "hotmail.com"]


if y != "":
	hosts.append(str(y))


emails = []


for i in hosts:
	emails.append(names[0] + "." + names[1] + "@" + i)
	emails.append(names[0][0] + names[1] + "@" + i)
	emails.append(names[0] + "@" + i)
	emails.append(names[0][0] + "." + names[1] + "@" + i)


for i in emails:
	print i




