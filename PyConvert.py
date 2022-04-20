import csv,json

#column_name = input('wanted_values: ')
#with open('test-csv.csv', 'r') as csvFile:
    ##reader = csv.reader(csvFile)
    #reader = csv.DictReader(csvFile, skipinitialspace = True, delimiter=',')
    #next(reader)
    #wanted_values = {'candles': []}
    #column_name = input('wanted_values: ')
    #for csvRow in reader:
        ##column_name = input('wanted_values: '
        #try:
            #if csvRow[column_name] in wanted_values:
                #wanted_values['candles'].append({'column_name': csvRow[int(column_name)]})#, 'open': csvRow[1], 'close': csvRow[4]})
        #except:           
            #with open ('test-json.json', 'w') as jsonFile:
                #json.dump(wanted_values, jsonFile, indent=4)

with open('test-csv.csv') as csvFile:
    reader = csv.reader(csvFile)
    next(reader)
    
    wanted_values = {'candles': []}
    for csvRow in reader:
        wanted_values['candles'].append({'time': csvRow[0], 'open': csvRow[1], 'close': csvRow[4]})
with open ('test-json.json', 'w') as jsonFile:
    json.dump(wanted_values, jsonFile, indent=4)    
