import re
import pandas as pd

f = open('./text.txt', encoding='utf-8')
table = pd.DataFrame({'номер темы': [],
                     'аннотация темы': [],
                     'колличество пар': []})

isNewBlock = False

for line in f: 
    line = re.sub('\n', '', line)

    if re.search('Тема \d+', line):
        isNewBlock = True
        body = ''
        time = ''
        title = line[4:]
    
    if isNewBlock:
        if re.search('Время, отведённое на тему:', line):   
            time = re.sub('Время, отведённое на тему: ', '', line)
            isNewBlock = False
            table.loc[len(table)] = [title, body, time]
        elif not re.search('Тема \d+', line):
            body += line

table.to_csv('table.csv', index=False)