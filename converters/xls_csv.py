import xlrd
import csv

wb = xlrd.open_workbook('your_workbook.xls')
sh = wb.sheet_by_name('Sheet1')
your_csv_file = open('your_csv_file.csv', 'wb')
wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

for rownum in xrange(sh.nrows):
   wr.writerow(sh.row_values(rownum))

your_csv_file.close()
