def count_total_characters_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return len(content)

# Example usage
file_path = './text_count.txt'
total = count_total_characters_from_file(file_path)
print("Total characters:", total)