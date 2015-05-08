
import csv

import re

funnyWords =  ['true',
'funny',
'hilarious',
'lmao',
'lol',
'haha',
'lmfao',
'omg'
'best',
'amazing',
':P',
':)',
'laugh',
'love',
'XD']

# on how much people identified with the content
agreeWords = ['true',
'accurate',
'correct',
'yes',
'relate',
'relatable',
'perfect',
'brilliant',
'genius',
'enjoy',
'relevant']

# on the negative reactions to the content, believing its perpetuating stereotypes
negativeWords = ['racist',
'stereotypical',
'awful',
'terrible',
'not funny',
'stereotype',
'cruel',
'guilt',
'offend',
'depressing'
'ignorant',
'ignorance',
'dumb']

# shows race dialogue being brought up due to the satire
neutralRaceWords = ['white',
'black',
'brown',
'Hispanic',
'Latino']

# shows dialogue typically associated racist intentions against whites
whiteSlurWords = ['honkey',
'cracker',
'hick',
'hillbilly'
'paleface',
'whitetrash',
'KKK',
'vanilla']

# shows dialogue typically associated racist intentions against blacks
blackSlurWords = ['nigger',
'monkey',
'baboon',
'negroid',
'African',
'colored',
'nigga',
'big lip',
'coon',
'savage',
'mandingo',
'niegress',
'watermelon',
'chicken'
'welfare',
'slave',
'white power']

# shows dialogue typically associated racist intentions against Hispanics
hispanicSlurWords = ['blue collar',
'fence-hopper',
'landscaper',
'lawnmover'
'manual labor',
'mudslide',
'wetback',
'pregnant',
'border',
'fence',
'river']

# some negative words are 
generalSlurs = ['gang',
'criminal',
'violent',
'drug',
'crime',
'lazy',
'dealer',
'stupid',
'minorities',
'minority']

file1 = open('ChrisRock.csv', 'rU')
file2 = open('ChrisRock2.csv', 'wb')
reader = csv.reader(file1)
writer = csv.writer(file2)
# writer.writerow(('Video Title', 'Video ID', 'User' , 'Comment', 'Published', 'SentimentScore', 'PositiveWords', 'NegativeWords', 'AgreeableWords', 'NeutralRaceWords', 'WhiteSlurWords' , 'BlackSlurWords' , 'HispanicSlurWords', 'GeneralSlurs'))
i = 0
writer.writerow(('Video_Title', 'Video_ID', 'User_Name' , 'Comment_Content', 'Published_Date', 'PositiveWords', 'NegativeWords', 'AgreeableWords', 'NeutralRaceWords', 'WhiteSlurWords' , 'BlackSlurWords' , 'HispanicSlurWords', 'GeneralSlurs'))

for row in reader:
  # print ('row[0] is ' + row[0])
  if i == 0:
    i = i + 1
    continue;
  comment = row[3]
  newDate = row[4]
  newDate2 = newDate[:10]
  # print ("newDate[0] is " + newDate[0])
  # print ("newDate[1] is " + newDate[1])
  # print ("newDate[2] is " + newDate[2])
  # month = newDate[0]
  # if len(month) < 2:
  #   month = "0" + month
  # day = newDate[1]
  # if len(day) < 2:
  #   day = "0" + day
  # year = newDate[2]
  # if len(year) < 3:
  #   year = "20" + year
  # new_str_date = year + "-" + month + "-" + day
  # print ("new_str is " + new_str_date)

  # print ('newDate is ' + newDate)

  print ("COMMMENT ")
  print (comment)
  negativeWordCount = 0
  positiveWordCount = 0
  agreeWordCount = 0
  neutralRaceCount = 0
  whiteSlurCount = 0
  blackSlurCount = 0
  hispanicSlurCount = 0
  generalSlurCount = 0
  for negWord in negativeWords:
      match = re.search(negWord, re.escape(comment), re.IGNORECASE)
      if match:
          print ("We got a match of a negative word with: " + str(match.group())) 
          negativeWordCount += 1
  for posWord in funnyWords:
      match = re.search(re.escape(posWord), re.escape(comment), re.IGNORECASE)
      if match:
          print ("We got a match of a positive word with: " + str(match.group())) 
          positiveWordCount += 1
  for agWord in agreeWords:
      match = re.search(agWord, re.escape(comment), re.IGNORECASE)
      if match:
          print ("We got a match of an agreeable word with: " + str(match.group())) 
          agreeWordCount += 1
  for neutralWord in neutralRaceWords:
      match = re.search(neutralWord, re.escape(comment), re.IGNORECASE)
      if match:
          print ("We got a match of a neutral race word with: " + str(match.group())) 
          neutralRaceCount += 1
  for whiteSlur in whiteSlurWords:
      match = re.search(whiteSlur, re.escape(comment), re.IGNORECASE)
      if match:
          print ("We got a match of a white slur word with: " + str(match.group())) 
          whiteSlurCount += 1
  for blackSlur in blackSlurWords:
      match = re.search(blackSlur, re.escape(comment), re.IGNORECASE)
      if match:
          print ("We got a match of a black slur word with: " + str(match.group())) 
          blackSlurCount += 1
  for hispanicSlur in hispanicSlurWords:
      match = re.search(hispanicSlur, re.escape(comment), re.IGNORECASE)
      if match:
          print ("We got a match of a hispanic slur word with: " + str(match.group())) 
          hispanicSlurCount += 1
  for genSlur in generalSlurs:
      match = re.search(genSlur, re.escape(comment), re.IGNORECASE)
      if match:
          print ("We got a match of a general slur word with: " + str(match.group())) 
          generalSlurCount += 1
  # print ('negativeWords: ' + str(negativeWordCount))
  # print ('positiveWords: ' + str(positiveWordCount))
  # print ('agreeableWords: ' + str(agreeWordCount))
  # print ('neutralRaceWords: ' + str(neutralRaceCount))
  # print ('whiteSlurCount: ' + str(whiteSlurCount))
  # print ('blackSlurCount: ' + str(blackSlurCount))
  # print ('hispanicSlurCount: ' + str(hispanicSlurCount))
  # print ('generalSlurCount: ' + str(generalSlurCount))



  new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', row[3])
  mystring = new_str.replace('\n', ' ').replace('\r', '')
  # print ('newDate is ' + newDate)
  # writer.writerow(('Video_Title', 'Video_ID', 'User_Name' , 'Comment_Content', 'Published_Date', 'SentimentScore', 'PositiveWords', 'NegativeWords', 'AgreeableWords', 'NeutralRaceWords', 'WhiteSlurWords' , 'BlackSlurWords' , 'HispanicSlurWords', 'GeneralSlurs'))
  writer.writerow((row[0], row[1], row[2], mystring, newDate2, positiveWordCount,negativeWordCount,agreeWordCount,neutralRaceCount,whiteSlurCount, blackSlurCount, hispanicSlurCount, generalSlurCount))
