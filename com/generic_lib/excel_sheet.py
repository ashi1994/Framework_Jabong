import xlrd
import sys, traceback

class ExcelSheet():

    def __init__(self):
        # self.rowNum = rowNum
        # self.colNum = colNum
        # self.sheetName = sheetName
        self.excelPath = "E:\Automation\BackUp\Git\Jabong\TestData.xlsx"

#     def readExcelData(self,sheetName, rowNum, colNum):
#         workbook = xlrd.open_workbook(self.excelPath)
#         worksheet = workbook.sheet_by_name(sheetName)
# #       for current_Row in range(worksheet.nrows):
#         cellValue = worksheet.cell_value(rowNum, colNum)
#         return cellValue

    def readData(self,testCaseId,sheetName):
            data = []
    #    try:
            workbook = xlrd.open_workbook("E:\Automation\BackUp\Git\Framework_Jabong\TestData.xlsx")
            worksheet = workbook.sheet_by_name(sheetName)
            for current_Row in range(worksheet.nrows):
                current_Id = str(worksheet.row(current_Row)[0])[6:15]
                if current_Id == testCaseId:
                    for current_cell in range(worksheet.ncols):
                        data.append(worksheet.cell_value(current_Row, current_cell))
                    break
            return data

        #except:
            traceback.print_exception("there is some exception.")




