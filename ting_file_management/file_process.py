from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_lines = txt_importer(path_file)
    # file_name = path_file.split("/")[-1]

    if path_file not in instance.search(None):
        instance.enqueue(path_file)

    formatted_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines
    }

    return print(formatted_dict)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
