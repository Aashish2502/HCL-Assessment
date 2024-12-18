import os
import re
import pandas as pd

def validate_email(text_file):
    with open(text_file, 'r') as file:
        content = file.read()

    expression = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z.]{2,7}'
    words = re.split(r'\s+|[,!?;]', content)
    result = [word.strip(".,!?;") for word in words if re.fullmatch(expression, word)]

    df = pd.DataFrame(result,columns=['Valid Email IDs'])
    file_name = 'test.xlsx'

    if not os.path.exists(file_name):
        df.to_excel('test.xlsx')
    else:
        print('Found an existing file! Updating it to a new one.')
        os.remove(file_name)
        df.to_excel('test.xlsx')

    return f'Email extracted: {len(df)-1}\nExtraction Successful!'

print(validate_email('test.txt'))