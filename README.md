Билет №3
Тема приложения
Приложение бронирования переговорок
Базовые функции
Получение информации о имеющихся переговорках
Получение информации о времени бронирования и наименовании переговорки
(Требует аутентификации)
Дополнение к функциям
При получении информации о времени бронирования и наименовании
переговорки, также возвращается ее этаж
Аутентификация
Аутентификация происходит путем сверки присылаемого пользователем значения
кода из СМС с имеющимися в БД. Если присланный код отсутствует в БД,
возвращается сообщение об ошибке.
Схема базы данных
База данных состоит из 2 таблиц, включающих следующие данные:
ID переговорки Наименование Этаж
1 Серенити 9
2 Сокол тысячелетия 17
3 Энтерпрайз 6
ID бронирования Код Переговорка Время Этаж
1 0000 Серенити 10:10 9
2 5811 Серенити 09:20 9
3 7813 Энтерпрайз 17:05 6