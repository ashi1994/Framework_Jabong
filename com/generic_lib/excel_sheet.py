import xlrd
import xlsxwriter
from com.generic_lib.initilization import *



import sys, traceback
import os

class ExcelSheet():

    def readData(self,testCaseId,sheetName):
            data = []
    #    try:
            workbook = xlrd.open_workbook(Initilization.path+"TestData.xlsx")
            worksheet = workbook.sheet_by_name(sheetName)
            for current_Row in range(worksheet.nrows):
                current_Id = str(worksheet.row(current_Row)[0])[7:18]
                if current_Id == testCaseId:
                    for current_cell in range(worksheet.ncols):
                        data.append(worksheet.cell_value(current_Row, current_cell))
                    break
            return data

        #except:
            traceback.print_exception("there is some exception.")



    def write_data(self):

        os.chdir(Initilization.log_path)
        workbook = xlsxwriter.Workbook(Initilization.path+"Report\Excel_Sheet\Status"+"-" + Initilization.now + ".xlsx")
        worksheet = workbook.add_worksheet()
        row = 0
        col = 1
        testCaseId = []
        count = 0
        with open('Logs.txt') as infile:
            value = "TestCase_"
            for line in infile:
                if value in line:
                    testCaseId = line.split(":")[2]
                    print testCaseId
                    testCaseId = testCaseId.split("=")[0]
                    testStatus = testCaseId.split("=")[1]
                    # valueStatus = "passed"
                    # testStatus = lientestID.split(" ")[2]
                    print (testCaseId + "==" + testStatus)
                    worksheet.write(count, 0, testCaseId)
                    worksheet.write(count, 1, testStatus)
                    count = count + 1
                    print count
                    # row +=1
                    # col+=1
            workbook.close()

    def write_data(self, sheetName, testCaseId, status):
        wb = xlsxwriter.Workbook("D:\CBT_Automation\Python\Workspace_Python_2\Framework_Jabong\WriteData.xlsx")
        sheet = wb.add_worksheet()
        sheet.write('D5', 'Hi Ashish')

