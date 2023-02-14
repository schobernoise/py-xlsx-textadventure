import openpyxl


def get_workbook(xlsx, index):
    # get excel file and index as arguments
    # the index is to determine which sheet to return
    # the index should be the same name as the workbook title
    wb = openpyxl.load_workbook(xlsx)
    return wb[index]
