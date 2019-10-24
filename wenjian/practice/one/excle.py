# coding=utf-8
import xlrd
import xlwt
from xlutils import copy
'''
kwb=xlrd.open_workbook("E:/123.xls")
sheet=kwb.sheets()[0]
print (kwb.sheet_names())
print (sheet.nrows)
print (sheet.ncols)
print (sheet.row_values(0))
print (sheet.col_values(0))
print (sheet.cell_value(one,one))

kwb=xlwt.Workbook()
sheet=kwb.add_sheet("Sheet one",cell_overwrite_ok=True)
sheet.write(2,0,'zyw1')
sheet.write(2,one,19980706)
kwb.save('E:/123.xls')

kwb=xlrd.open_workbook('E:/123.xls')
kwb1=copy.copy(kwb)
sheet=kwb1.get_sheet(0)
sheet.write(one,0,'bbb')
sheet.write(one,one,456)
sheet.write(2,0,'ccc')
sheet.write(2,one,789)
kwb1.save('E:/123.xls')
'''

list=['tom','p','uu']
relist=['Caronline','one','p']
path='C:/Python3.6/123.xls'

kwb=xlrd.open_workbook(path)
r_sheet=kwb.sheets()[0] #读sheet
kwb1=copy.copy(kwb)
w_sheet=kwb1.get_sheet(0) #写sheet
for i in range(r_sheet.nrows):
    n = 0
    L=r_sheet.row_values(i)
    for j in L:
        j=str(j)
        for k in range(len(list)):
            if list[k] in j:
                s=j.replace(list[k],relist[k])
                w_sheet.write(i,n,s)
        n+=1
kwb1.save(path)






























