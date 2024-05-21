import encryption
import Transformations

def get_loc(sheet, id):
    cell = sheet.find(id)
    idx = cell.row
    return idx

def new_entry(workbook, entry):
    idx = get_loc(workbook.worksheet("Legal"), entry[0])
    for i in range (len(entry)-1):
        workbook.worksheet("Legal").update_cell(idx, i+2, encryption.encrypt_element(entry[i+1], "L"))
    
    


