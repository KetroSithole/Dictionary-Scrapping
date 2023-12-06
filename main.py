import json

def process_line(line):
    data = {}
    parts = line.split(',')
    
    if len(parts) < 2:
        return None
    
    tsonga_word, definitions_part = parts[0].strip(), parts[1].strip()
    
    if tsonga_word.startswith('-'):
        data['tso'] = tsonga_word[1:].strip()
        data['type'] = ''
        data['origin'] = ''
        data['definitions'] = []
        data['related_words'] = []

        definitions = []
        for definition_part in definitions_part.split(';'):
            definition = definition_part.strip().strip('.').strip(',')
            definitions.append(definition)

        data['definitions'] = definitions

        return data
    else:
        return None

def read_and_convert(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    json_data = []

    for line in lines:
        entry = process_line(line)
        if entry:
            json_data.append(entry)

    with open(output_filename, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    input_filename = 'dictionary.txt'
    output_filename = 'output.json'
    read_and_convert(input_filename, output_filename)
