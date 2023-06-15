from ting_file_management.file_management import txt_importer


def format_dict(word, file_path, occurrences, content, by_word):
    formatted_occurences = []
    for index, occurrence in enumerate(occurrences):
        if not by_word:
            formatted_occurences.append({"linha": occurrence})
        else:
            formatted_occurences.append(
                {"linha": occurrence, "conteudo": content[index]}
            )

    return {
        "palavra": word,
        "arquivo": file_path,
        "ocorrencias": formatted_occurences
    }


def search_occurrences(word, instance):
    occurences = []
    files_paths = instance.search(None)
    for path in files_paths:
        file_lines = txt_importer(path)
        file_occurrences = []
        file_occurences_lines = []
        for index, line in enumerate(file_lines):
            if word in line.lower():
                file_occurrences.append(index + 1)
                file_occurences_lines.append(line)
        if len(file_occurrences) > 0:
            full_occurrence = {
                "word": word,
                "file_path": path,
                "occurrences": file_occurrences,
                "content": file_occurences_lines
            }
            occurences.append(full_occurrence)
    return occurences


def exists_word(word, instance):
    occurences = search_occurrences(word, instance)
    formatted_occurences = []
    for occurrence in occurences:
        formatted_occurence = format_dict(**occurrence, by_word=False)
        formatted_occurences.append(formatted_occurence)
    return formatted_occurences


def search_by_word(word, instance):
    occurences = search_occurrences(word, instance)
    formatted_occurences = []
    for occurrence in occurences:
        formatted_occurence = format_dict(**occurrence, by_word=True)
        formatted_occurences.append(formatted_occurence)
    return formatted_occurences
