"""
Напишите метод add для объекта StringCalculator который,
получая строку с разделенными числами возвращает сумму этих чисел
"""


class StringCalculator:
    def add(self, input_str):
        if input_str == '':
            result = 0
        else:
            input_str = input_str.replace(',', ' ')
            splitted = input_str.split()
            if splitted[0].startswith("//"):
                separator = splitted[0][2:len(splitted[0])]
                splitted = splitted[1].split(separator)

            arr = list(map(int, splitted))

            negative = [x for x in arr if x < 0]
            if len(negative) == 0:
                result = 0
                for x in arr:
                    if x < 1000:
                        result += x
            else:
                result = "отрицательные числа запрещены: " + ','.join(map(str, negative))
        return result
