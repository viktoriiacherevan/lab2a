1. Перейшовши у папку з даними файлами запустіть виконання програми командою наведеною нижче. Результат виконання команди впишіть у Ваш README файл:

We are in the __main__
2020-10-17 17:17:18.788576
win32

2. Прокоментуйте що виконує дана програма та звідки беруться виведені стрічки;
a. Що буде якщо запустити програму через: python . -h;
usage: . [-h] [-o OPT] [-l]

optional arguments:
  -h, --help            show this help message and exit

b. Якщо передати параметри? python . -o "Цей текст також має вивестись";
  -o OPT, --optional OPT
                        Цей параметр є вибірковим.

We are in the __main__
2020-10-17 17:31:56.315068
win32
З консолі було передано аргумент
 ========== >> Цей текст також має вивестись; << ==========

d. Також познайомтесь з логуванням. Запустіть з консолі python . --logs:
  -l, --logs            Якщо виконати команду з цим параметром будуть виводитись логи.

2020-10-17 17:32:30,034 root INFO: Тут буде просто інформативне повідомлення
2020-10-17 17:32:31,327 root WARNING: Це Warning повідомлення
2020-10-17 17:32:31,331 root ERROR: Це повідомлення про помилку


За допомогою функції parser.parse_args() зчитуємо передані аргументи в змінну args. Після цього перевіряємо, чи передали аргумент logs. Якщо так - визиваємо функцію how_to_write_logs(), якщо ні - визиваємо функцію main і передаємо в неї аргумент opt. Після цього в функції main йде провірка, чи передано дані через opt. Якщо так -виводимо це в консоль.

3. Створіть Власну функцію у файлі common.py яка буде виводить всі парні числа до 100 якщо у функцію передати значення True і непарні якщо значення False. Викличте Вашу функцію з __main__ та виведіть результат.

        def show_numbers(pair):
         i = 0
          while i < 101:
              if i % 2 == 0 and pair:
                  print(i)
              elif i % 2 != 0 and not pair:
                  print(i)
              i += 1
        

4.Створіть функцію яка може виконуватись з помилкою. У випадку її виникнення виведіть ERROR повідомлення за допомогою логування (Використайте бібліотеку logging). Якщо функція відпрацювала без помилки виведіть INFO повідомлення.

    def get_factorial(number):
     try:
          i = 1
          factorial = 1
          while i <= number:
              factorial *= i
              i += 1
          logging.info(factorial)
     except Exception as e:
          logging.warning(e)
