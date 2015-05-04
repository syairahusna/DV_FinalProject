import csv
import itertools

# with open('crime_rate_ngram.txt', 'r') as in_file:
#     stripped = (line.strip() for line in in_file)
#     lines = (line for line in stripped if line)
#     grouped = itertools.izip(*[lines] * 3)
#     with open('extracted.csv', 'w') as out_file:
#         writer = csv.writer(out_file)
#         writer.writerow(('title', 'intro', 'tagline'))
#         writer.writerows(grouped)

# with open('crime_rate_ngram.txt', 'r') as in_file:
#     for line in in_file:
#     	print ('--- ' + line + '\n')

# with open('crime_rate_ngram.txt', 'r') as in_file:
# 	lines = [line.strip() for line in in_file if line.strip()]
# 	for i, line in enumerate(lines):
# 	    # csv.SetCell(i % 3, line)
# 	    print ('--- ' + line[i] + '\n')

z = open('white_power_ngram.txt', 'r')
for line in z.readlines():
    cols = line.split('\t')
z.close()
writer = csv.writer(open('white_power_ngram.csv', 'wb'), quoting=csv.QUOTE_NONNUMERIC)
writer.writerow(('Year', 'Match_Count','Page_Count','Volume_Count'))
for i in cols:
	print ('---- ' + i)
	values = i.split(',')
	if (len(values) > 3):
		print ('values[0] = ' + values[0])
		print ('values[1] = ' + values[1])
		print ('values[2] = ' + values[2])
		print ('values[3] = ' + values[3])
		writer.writerow((values[0], values[1], values[2], values[3]))

