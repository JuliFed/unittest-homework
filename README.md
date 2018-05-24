# Домашнее задание

## Прежде чем начать:
* Постарайтесь не читать задания наперед.
* Делайте задания по одному.
* Для этой практики нет необходимости проверять неправильный ввод не указанный в задании.

## Задание:
Напишите метод add для объекта StringCalculator который, получая строку с разделенными числами возвращает сумму этих чисел
1. Пустая строка возвращает ноль ('' => 0)
2. Единственное число возвращает значение этого числа ('1' => 1 '2' => 2)
3. Два числа разделенные запятой возвращают сумму ('1,2' => 3 '10,20' => 30)
4. Два числа разделенные переходом строки возвращают сумму ('1\n2' => 3)
5. Три числа разделенные запятой или переходом строки возвращают сумму ('1\n2,3\n4' => 10)
6. Отрицательные числа возвращают ошибку с сообщением ('-1,2,-3' => 'отрицательные числа запрещены: -1,-3')
7. Числа больше чем 1000 игнорируются
8. Разделитель из одного знака может быть задан на первой строке начиная с // (к примеру //#\n1#2 для того чтобы задать ‘#’ как разделитель)
9. Разделитель из нескольких знаков может быть задан на первой строке начиная // (например //###\n1###2 для того чтобы задать ‘###’ как разделитель)



