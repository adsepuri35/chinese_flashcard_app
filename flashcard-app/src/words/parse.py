import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import time

# create a csv file in the lesson_lists folder for lesson x
def spreadsheet_to_csv(sheet_url):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('../../config/credentials.json')
    client = gspread.authorize(creds)

    # col structure: lesson #, hanzi, pinyin, translation, proficiency (0 = trash, 1 = goated)

    data = []

    for lesson_num in range(1, 21):
        curr_lesson = "Lesson" + str(lesson_num)
        curr_sheet = client.open_by_url(sheet_url).worksheet(curr_lesson)
        
        hanzi_column = curr_sheet.col_values(1)
        pinyin_column = curr_sheet.col_values(2)
        translation_column = curr_sheet.col_values(3)

        df = pd.DataFrame({
            'lesson_number': [lesson_num] * len(hanzi_column),
            'hanzi': hanzi_column,
            'pinyin': pinyin_column,
            'translation': translation_column,
            'proficiency': [0] * len(hanzi_column)
        })

        data.append(df)

        print("Added Lesson " + str(lesson_num))
        time.sleep(1)

    combined_df = pd.concat(data, ignore_index=True)

    combined_df.to_csv('integrated_chinese_1.csv', index=False, encoding='utf-8')

def main():
    sheet_url = 'https://docs.google.com/spreadsheets/d/1A1lxacaMp3v9_S1K6dCCNyqq0icE0gBoMtr1Ro4jeVA/edit?gid=0#gid=0'

    spreadsheet_to_csv(sheet_url)
    # first_cell_value = get_first_cell(sheet_url, sheet_name)
    # print(first_cell_value)

if __name__ == "__main__":
    main()