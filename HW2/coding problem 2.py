# Zachary Arroyo
# UHID 1810267

from datetime import datetime

# dates = []
# begin = input()
# while begin != '-1':
#     dates.append(begin)
#     begin = input()

readfile = open('inputDates.txt','r')
writefile = open('parsedDates.txt','w+')
dates = readfile.read().splitlines()

for line in dates:
    tempdate = []
    if line.find('January') != -1:
        tempdate = ['January']
        line = line.replace('January ','')
    elif line.find('February') != -1:
        tempdate = ['February']
        line = line.replace('February ', '')
    elif line.find('March') != -1:
        tempdate = ['March']
        line = line.replace('March ', '')
    elif line.find('April') != -1:
        tempdate = ['April']
        line = line.replace('April ', '')
    elif line.find('May') != -1:
        tempdate = ['May']
        line = line.replace('May ', '')
    elif line.find('June') != -1:
        tempdate = ['June']
        line = line.replace('June ', '')
    elif line.find('July') != -1:
        tempdate = ['July']
        line = line.replace('July ', '')
    elif line.find('August') != -1:
        tempdate = ['August']
        line = line.replace('August ', '')
    elif line.find('September') != -1:
        tempdate = ['September']
        line = line.replace('September ', '')
    elif line.find('October') != -1:
        tempdate = ['October']
        line = line.replace('October ', '')
    elif line.find('November') != -1:
        tempdate = ['November']
        line = line.replace('November ', '')
    elif line.find('December') != -1:
        tempdate = ['December']
        line = line.replace('December ', '')

    if line.find(',') != -1:
        ind = line.index(',') + 1
        if line[ind - 3:ind].lstrip() == '':
            tempdate.append(line[ind - 2:ind].lstrip())
        else:
            tempdate.append(line[ind - 3:ind].lstrip())
        tempdate.append(line[ind + 1:].lstrip())
    if len(tempdate) == 3:
        x = datetime.strptime(' '.join(tempdate), '%B %d, %Y')
        if datetime.today() >= x:
            parsed = (x.strftime('%#m/%#d/%Y'))
            print(parsed)
            writefile.write(parsed + '\n')