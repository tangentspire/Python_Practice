import csv
import openpyxl

# Takes a .csv file and returns and excel file. It makes sure all rows are text
# to ensure 15+ digit numbers are not truncated.

# wb = openpyxl.Workbook()
#ws = wb.worksheets[0]
#col_data_types = [str, str, str, str, str]
#order_of_columns = ['Job Id','Queue Name','Actor Name','Actor Id','Decisions String']

#with open('test.csv') as f:
    #reader = csv.reader(f, delimiter=',')
        #headers = next(reader)
        ## process headers
        #for row in reader:	
            #row = [dt(obj) for dt, obj in zip(col_data_types, row)]
                # process row
                #ws.append(row)
        #wb.save('file.xlsx')


# put the columns in the right order. Can do this is in .csv or pyxl whatever
# is easier.

# wb.insert_cols(2, 1)
# wb.save('file.xlsx')



