#  Port Scanner

Учебный проект по пентесту: простой TCP-портсканер на Python.  
Сканирует порты, определяет, открыты ли они, и пытается получить баннер сервиса.  

 **Использовать только в образовательных целях.  
Не сканируйте чужие хосты без разрешения!**

---

##  Установка
Клонируем репозиторий:
```bash
git clone git@github.com:0xsmk/port-scanner.git
cd port-scanner
python3 scanner.py -t 127.0.0.1 -p 1-100

---

##  Пример работы
[+] Starting scan on 127.0.0.1
[OPEN] Port 22: SSH-2.0-OpenSSH_8.9p1
[OPEN] Port 80: No banner

---

##  To-Do
 Многопоточность
 UDP-сканирование
 Вывод в JSON/CSV