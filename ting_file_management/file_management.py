import sys


def txt_importer(path_file):
    try:
        with open(path_file, "r") as file:
            if '.txt' not in path_file:
                print("Formato inválido", file=sys.stderr)
            else:
                return file.read().splitlines()
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)


print(txt_importer('statics/arquivo_teste.txt'))
