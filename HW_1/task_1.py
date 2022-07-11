# Написать метод domain_name, который вернет домен из url адреса:
# Подключаем стандартную библеотеку для работы с URL
from urllib.parse import urlparse


# Функция для преобразования URL в домен
def domain_name(url):
    domain = urlparse(url).netloc  # Вытаскиваем netloc
    if domain == '':  # Если netloc пуст, то адрес начинается с WWW
        domain = urlparse(url).path.split('.')  # делаем список
        return domain[1] if domain[0].lower() == 'www' else domain[0]  # делаем проверку, чтобы отрабатывал кейс без www
    else:
        domain = domain.split('.')
        return domain[1] if domain[0].lower() == 'www' else domain[0]  # делаем проверку, что в домене есть http и www


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
assert domain_name("http://github.com/carbonfive/raygun") == "github"
assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
assert domain_name("https://www.cnet.com") == "cnet"

print('All tests passed!')
