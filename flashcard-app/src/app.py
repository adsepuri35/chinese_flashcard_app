import gspread
from oauth2client.service_account import ServiceAccountCredentials

# test google sheets api
def get_first_cell(sheet_url):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('../config/credentials.json')
    client = gspread.authorize(creds)

    sheet1 = client.open_by_url(sheet_url).sheet1
    first_cell = sheet1.cell(2,1).value
    return first_cell

def main():
    sheet_url = 'https://docs.google.com/spreadsheets/d/1A1lxacaMp3v9_S1K6dCCNyqq0icE0gBoMtr1Ro4jeVA/edit?gid=0#gid=0'
    first_cell_value = get_first_cell(sheet_url)
    print(first_cell_value)

if __name__ == "__main__":
    main()