from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()
        self.__length = 0

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        self._data.append(value)
        self.__length += 1

    def dequeue(self):
        if self.__length == 0:
            return None
        self.__length -= 1
        return self._data.pop(0)

    def search(self, index):
        if index is None:
            return self._data
        elif index < 0 or index > self.__length - 1:
            raise IndexError("Índice Inválido ou Inexistente")
        else:
            return self._data[index]

    def __str__(self):
        str_items = ""
        for i in range(len(self._data)):
            value = self._data[i]
            str_items += str(value)
            if i + 1 < len(self._data):
                str_items += ", "

        return "Queue(" + str_items + ")"
