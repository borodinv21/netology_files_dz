import os

files_count = 3 # Сюда можно вписать количество файлов с которыми будем работать
files_list = []

for i in range(1, files_count + 1):
    file_path = os.path.join(os.getcwd(), f'file{i}.txt')

    with open(file_path, 'r') as file:
        text = ''
        lines_count = 0

        for j in file:
            text += j
            lines_count += 1

        files_list.append(
            {
                'file_name': f'file{i}.txt',
                'lines_count' : lines_count,
                'text': text
            }
        )

files_list.sort(key=lambda dictionary: dictionary['lines_count'])

for i in files_list:
    with open('result.txt', 'a') as file:
        file.write(i['file_name'].strip() + '\n')
        file.flush()
        file.write(str(i['lines_count']) + '\n')
        file.flush()
        file.write(i['text'] + '\n' * 2)
        file.flush()
