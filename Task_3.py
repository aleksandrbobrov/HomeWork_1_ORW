def read_files(file_names):
    files_data = []
    for file_name in file_names:
        with open(file_name, 'r') as file:
            file_content = file.readlines()
            files_data.append((file_name, len(file_content), file_content))
    return files_data

def merge_files(file_names, output_file):
    files_data = read_files(file_names)
    sorted_files_data = sorted(files_data, key=lambda x: x[1])  # Сортируем по количеству строк

    with open(output_file, 'w') as output:
        for file_data in sorted_files_data:
            file_name, num_lines, content = file_data
            output.write(f"{file_name}\n{num_lines}\n")
            output.writelines(content)

# Пример использования:
file_names = ['1.txt', '2.txt']
output_file = 'merged_file.txt'
merge_files(file_names, output_file)