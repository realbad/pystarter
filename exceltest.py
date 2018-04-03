import xlrd

path = ('17级分班.xlsx')
workbook = xlrd.open_workbook(path)
sheet_name = workbook.sheet_names()
#sheet = workbook.sheet_by_index()
#sheet = workbook.sheets()
#print(sheet_name)

for sheet in workbook.sheets():
    print('\n')
    print(sheet.name)
    for row in range(sheet.nrows):
        print()
        for col in range(sheet.ncols):
            print("%7s" % sheet.row(row)[col].value, '\t', end='')
# for sheet in workbook.sheet_by_name(sheet_name):
#     print(sheet)
#     for row in range(sheet.nrows):
#         print()
#         for col in range(sheet(row)[col]):
#             print("%7s"%sheet_name.row(row)[col].value,'\t',end ='')