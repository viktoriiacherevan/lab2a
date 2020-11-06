1. інсталювання pipenv: 

        pip install pipenv
        pipenv --python 3.8
        pipenv shell

2. встановлення бібліотек requests:

        pipenv install requests
        pipenv install ntplib

3.

    def greetings(hour=None):
      result = ""
    if hour is None:
        hour = datetime.now().time().hour
    if 6 <= hour <= 9:
        result = "Good morning!"
    elif 10 <= hour <= 19:
        result = "Good day!"
    elif 20 <= hour <= 22:
        result = "Good evening!"
    else:
        result = "Good night"
    return result

4. 
   
        def test_my_method(self):
              self.assertTrue(self.test_result == "Good day!") 

5. результат тесту:
    
        ========================================
        Результат без параметрів:
        No URL passed to function
        ========================================
        Результат з правильною URL:
        Time is:  11:01:21 AM
        Date is:  11-06-2020

5. перенаправлення результатів:

            pytest tests/tests.py > results.txt
            python app.py >> results.txt

6. створення Makefile.+
