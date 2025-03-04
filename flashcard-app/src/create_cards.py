import pandas as pd

def read_csv(filepath):
    df = pd.read_csv(filepath)
    return df

def filter_lesson(df, lesson_number):
    filtered_df = df[df['lesson_number'] == lesson_number]
    return filtered_df



file_path = "./words/integrated_chinese_1.csv"
df = read_csv(file_path)
lesson_9_df = filter_lesson(df, 9)
print(lesson_9_df)