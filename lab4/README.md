1. Перевірка чи докер встановлений і працює правильно на віртуальній машині:


2. Імедж із Django сайтом зробленим у попередній роботі:
![ф](1.PNG)

3. Створюю Dockerfile.

4. Створюю акаунт і репозеторій на docker.hub: https://hub.docker.com/u/viktoriiacherevan; https://hub.docker.com/r/viktoriiacherevan/lab4

5. Білд і пуш Docker імеджа:
sudo docker build -t viktoriiacherevan/lab4:django .
sudo docker images
sudo dokcer push viktoriiacherevan/lab4:django
![ф](2.PNG)
![ф](3.PNG)

6. Запуск docker імедж:
sudo docker build --no-cache -t viktoriiacherevan/lab4:monitoring --file Dockerfile.site .

7. Запуск контейнерів:
sudo docker run -it --name=django --rm --publish 8000:8000 viktoriiacherevan/lab4:django . ;
sudo docker run --net=host --name=monitoring --rm -it viktoriiacherevan/lab4:monitoring .
