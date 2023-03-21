class NewList:
    def __init__(self, lst=None):
        self._lst = lst if type(lst) == list else []

    def get_list(self):
        return self._lst

    def __sub__(self, other):
        if type(other) not in (list, NewList):
            raise ArithmeticError("первый операнд должен быть типом list или NewList")
        other_list = other if type(other) == list else other.get_list()
        return NewList(self.__diff_list(self._lst, other_list))

    def __rsub__(self, other):
        if type(other) != list:
            raise ArithmeticError("второй операнд должен быть типом list или NewList")
        return NewList(self.__diff_list(other, self._lst))

    @staticmethod
    def __diff_list(list1, list2):
        if len(list2) == 0:
            return list1

        temp = list2[:]
        return [x for x in list1 if not NewList.__is_elem(x, temp)]

    @staticmethod
    def __is_elem(val, temp_lst):
        res = any(map(lambda k: type(k) == type(val) and k == val, temp_lst))
        if res:
            temp_lst.remove(val)
        return res