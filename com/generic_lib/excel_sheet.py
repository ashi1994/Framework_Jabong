import xlrd
import xlsxwriter

import sys, traceback

class ExcelSheet():

    def readData(self,testCaseId,sheetName):
            data = []
    #    try:
            workbook = xlrd.open_workbook("D:\CBT_Automation\Python\Workspace_Python_2\Framework_Jabong\TestData.xlsx")
            worksheet = workbook.sheet_by_name(sheetName)
            for current_Row in range(worksheet.nrows):
                current_Id = str(worksheet.row(current_Row)[0])[7:16]
                if current_Id == testCaseId:
                    for current_cell in range(worksheet.ncols):
                        data.append(worksheet.cell_value(current_Row, current_cell))
                    break
            return data

        #except:
            traceback.print_exception("there is some exception.")


    def write_data(self, sheetName, testCaseId, status):
        wb = xlsxwriter.Workbook("D:\CBT_Automation\Python\Workspace_Python_2\Framework_Jabong\WriteData.xlsx")
        sheet = wb.add_worksheet()
        sheet.write('D5', 'Hi Ashish')
