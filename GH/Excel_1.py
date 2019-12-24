import openpyxl
wb = openpyxl.load_workbook("zhc.xlsx")
type(wb)
wb.get_sheet_names()