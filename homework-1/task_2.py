import ipaddress  # подлючаю модуль для работы с ip адресами


# функция для перевода числа в ip адрес
def int32_to_ip(int32):
    return str(ipaddress.IPv4Address(int32))


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
assert int32_to_ip(32) == "0.0.0.32"
assert int32_to_ip(0) == "0.0.0.0"

print('All tests passed!')
