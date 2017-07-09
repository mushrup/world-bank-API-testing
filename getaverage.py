#this module convert xls/xlsx file to list
#and from list to array
#then calculate the average of list
#!/local/bin/python
import xlrd
book = xlrd.open_workbook('wage1.xls')
sheet = book.sheet_by_name('WAGE1')
data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
# Profit !
wage= [item[1] for item in data]
average=sum(wage)/float(len(wage))
print "The average wage in 1976 dollar:",average
