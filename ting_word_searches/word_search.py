from ting_file_management.file_management import txt_importer


def format_dict(word, file_path, occurrences):
    formatted_occurences = []
    for occurrence in occurrences:
        formatted_occurences.append({"linha": occurrence})

    return {
        "palavra": word,
        "arquivo": file_path,
        "ocorrencias": formatted_occurences
    }


def exists_word(word, instance):
    occurences = []
    files_paths = instance.search(None)
    for path in files_paths:
        file_lines = txt_importer(path)
        file_occurrences = []
        for index, line in enumerate(file_lines):
            if word in line.lower():
                file_occurrences.append(index + 1)
        if len(file_occurrences) > 0:
            formatted_occurences = format_dict(word, path, file_occurrences)
            occurences.append(formatted_occurences)
    return occurences


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
