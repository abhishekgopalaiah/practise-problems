import xlrd


def format_excel(filename):
    # check if excel file is empty or not
    print('checking excel to find any issues..')
    opened_sheet = xlrd.open_workbook(filename)
    non_empty_sheets_col = [sheet for sheet in opened_sheet.sheets() if sheet.ncols > 0]
    non_empty_sheets_col_lst = [sheet.name for sheet in non_empty_sheets_col]
    # ignore header row
    non_empty_sheets_row = [sheet for sheet in opened_sheet.sheets() if sheet.nrows > 1]
    non_empty_sheets_row_lst = [sheet.name for sheet in non_empty_sheets_row]
    len_col = len(non_empty_sheets_col_lst)
    len_row = len(non_empty_sheets_row_lst)

    return len_row, len_col


if __name__ == "__main__":
    format_excel('path_of_file')
