import pandas as pd
import re
import csv

fhandle = open('onelinefile.txt')
fread = fhandle.read()
print(fread)
res = re.findall(r'(\d+)(\w+?)([-+]?\d*\.\d+|\d+)([a-zA-Z ]*)',fread)
print(res)
dataframe1 = pd.DataFrame(res)
writer = pd.ExcelWriter('Filename2.xlsx', engine='xlsxwriter')
dataframe1.to_excel(writer, sheet_name='data', index=None)
writer.save()
fhandle.close()
'''dataframe1 = pd.read_csv("onelinefile.txt")
dataframe1.to_csv('Filename2.csv', index = False) #convert file to csv
'''
