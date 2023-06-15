from ting_file_management.file_management import txt_importer
import sys


def format_dict(path_file, file_length, file_lines):
    return {
        "nome_do_arquivo": path_file,
        "qtd_linhas": file_length,
        "linhas_do_arquivo": file_lines
    }


def process(path_file, instance):
    file_lines = txt_importer(path_file)
    # file_name = path_file.split("/")[-1]

    if path_file not in instance.search(None):
        instance.enqueue(path_file)

    file_data = format_dict(path_file, len(file_lines), file_lines)

    return print(file_data)


def remove(instance):
    path_file = instance.dequeue()

    if path_file is None:
        return print("Não há elementos")
    else:
        return print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    try:
        path_file = instance.search(position)
        file_lines = txt_importer(path_file)

        file_data = format_dict(path_file, len(file_lines), file_lines)

        return print(file_data)
    except IndexError:
        return print("Posição inválida", file=sys.stderr)
