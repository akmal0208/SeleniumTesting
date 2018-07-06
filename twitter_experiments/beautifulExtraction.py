from bs4 import BeautifulSoup

# page_url = (open(r"C:\testDir\Bots\twitter_experiments\appKey.html"), "html.parser")
# soup = BeautifulSoup(page_url,"html.parser")#,"lxml")
soup = BeautifulSoup(open(r"C:\testDir\Bots\twitter_experiments\appKey.html"), "html.parser")
# print(soup)
app_settings = soup.body.find('div', attrs={'class': 'app-settings'})

divs = app_settings.find_all('div',attrs={'class':'row'})

print("######### PRINTING DIVS #################")
print(divs)


print(type(divs))


print("######### FOR I IN DIVS, FIND ALL SPANS #################")

consumer = []
access = []
# count = 0
for i in divs:
	# print(i.findAll('span'))
	for j in i.findAll('span'):
		# print(j)
		if j.has_attr('class'):
			# print(j)
			pass
		else:
			print("No Class:", j)
			print('text of j',j.get_text())	
			# count += 1
			# print(count)
			consumer.append(j.get_text())

print(consumer)

consumerKey = consumer[0]
consumerSecret = consumer[1]


app_settings = soup.body.find('div', attrs={'class': 'access'})

divs = app_settings.find_all('div',attrs={'class':'row'})


for i in divs:
	# print(i.findAll('span'))
	for j in i.findAll('span'):
		# print(j)
		if j.has_attr('class'):
			# print(j)
			pass
		else:
			print("No Class:", j)
			print('text of j',j.get_text())	
			# count += 1
			# print(count)
			access.append(j.get_text())

print(access)

accessKey = access[0]
accessSecret = access[1]

print("\n\nconsumer key:",consumerKey,"\nconsumer secret:",consumerSecret)
print("\n\nAcccess key:",accessKey,"\nAcccess secret:",accessSecret)







		# 	if count == 2:
		# 		break
		# 	else:
		# 		continue
		# # break			
		# ,attrs={'class':'heading'}):
	# 	print('has class')

	# spans = i.findAll('span')

# print("######### FOR I IN SPANS #################")


# for i in spans:
# 	print(i)	

# spans = divs.findAll('span',attrs={})
# print(spans)

# for span in divs.span.find_all('span'):
# 	print(span)

# print(divs)
accessList = []
print('\n\n####### USING SELECT ########')
access = soup.select("div[class=access] > div[class=row] > span")
for i in access:
	# print(i)
	if(i.has_attr('class')):
		# print(i)
		pass
	else: 
		# print(i)	
		accessList.append(i.get_text())

print('\n\naccess key',accessList[0],'\naccess secret',accessList[1])


# print('###')	
# print(access)
# print(type(access),type(i))
# # > div[class=row] > span[class=heading] > span
# print(consumerKey)



# app_settings = soup.body.find('div', attrs={'class': 'access'})

# divs = app_settings.find_all('div',attrs={'class':'row'})


# for i in divs:
# 	# print(i.findAll('span'))
# 	for j in i.findAll('span'):
# 		# print(j)
# 		if j.has_attr('class'):
# 			# print(j)
# 			pass
# 		else:
# 			print("No Class:", j)
# 			print('text of j',j.get_text())	
# 			# count += 1
# 			# print(count)
# 			access.append(j.get_text())

# print(access)

# accessKey = access[0]
# accessSecret = access[1]

# print("\n\nconsumer key:",consumerKey,"\nconsumer secret:",consumerSecret)
# print("\n\nAcccess key:",accessKey,"\nAcccess secret:",accessSecret)





# for span in consumerKey:
# 	print(span)
# badges = soup.body.find('div', attrs={'class': 'badges'})
# for span in badges.span.find_all('span', recursive=False):
#     print span.attrs['title']
# driver.close()