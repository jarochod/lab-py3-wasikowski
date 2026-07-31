# R122. Przydatne funkcje do operacji na datach

# Praca z czasem i datami
# Czas w komputerach wyrażony jest w postaci ilości sekund od 1 stycznia 1970 roku, nazywamy taką wartość 
# czasem uniksowym (ang. Unix time lub epoch time).
# Python udostępnia wiele funkcji do operowania na datach dostępnych w module time. 

##################--------------------
print('\n----wykład-----\n')

import time
ticks = time.time()
print(ticks) # np 1742059031.157035 ilość sekund od 1.01.1970 do becnego czasu

# Bardziej przystępną funkcją zwracającą aktualny czas jest time.localtime(), która zwraca datę,
# jak również czas w formie przystępnej krotki (tzw named tuple).

import datetime
timeData = time.localtime()
print(timeData) # time.struct_time(tm_year=2025, tm_mon=3, tm_mday=15, tm_hour=18, tm_min=52, tm_sec=43, tm_wday=5, tm_yday=74, tm_isdst=0)
print(timeData.tm_year) # 2025 / rok
print(timeData.tm_mon) # 3 / miesiąc
print(timeData.tm_mday) # 15 / dzień miesiąca
print(timeData.tm_hour) # 18 / godzina
print(timeData.tm_min) # 55 / minuty
print(timeData.tm_sec) # 29 / sekundy
print(timeData.tm_wday) # 5 / dzien tygodnia od 0 do 6: 0 poniedziałek
print(timeData.tm_yday) # 74 / dzień roku od 1 do 366
print(timeData.tm_isdst) # 0 / oznacza że Python zarządza czasem zimowym / np -1 czas letni

# Do funkcji time.localtime() można przekazać również timestamp, czyli ilość sekund od 01.01.1970
# 0 sekund od 01.01.1970r
timeData = time.localtime(0)
print(timeData) # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=1, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

ticks = time.time()
print(ticks) # 1742066988.2198813
# Odjęcie jednej doby od aktualnego limestamp, zamiast 15 marca, dane z 14 marca
timeData = time.localtime( ticks - (24 * 60 * 60))
print(timeData) # time.struct_time(tm_year=2025, tm_mon=3, tm_mday=14, tm_hour=20, tm_min=29, tm_sec=48, tm_wday=4, tm_yday=73, tm_isdst=0)
print(timeData.tm_mday) # 14 / bo tm_mday=14

# Funkcja time.asctime() formatuje w wygodny sposób datę i czas dostarczoną przez time.localtime()
result = time.asctime( time.localtime(time.time()) )
print("Wynik:", result) # Wynik: Sat Mar 15 20:35:22 2025

# Funkcja time.strftime() formatuje data i czas na string według podane wzorca, koszysta z oznaczeń,
# które będą zastąpione konkretnymi wartościami w tekście: %Y - rok, %m - miesiąc, %d - dzień,
# %H - godzina, %M - minuty, %S - sekundy
timeData = time.localtime() # aktualny czas
timeStr = time.strftime("%m/%d/%T %H:%M:%S", timeData)
print(timeStr) # 03/15/20:44:06 20:44:06

# Funkcja time.strptime() parsuje łańcuch znaków i tworzy z niego krotkę z data i czasem.
import time
timeStr = "15 March, 2025"
timeData = time.strptime(timeStr, "%d %B, %Y")
print(timeData) # time.struct_time(tm_year=2025, tm_mon=3, tm_mday=15, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=74, tm_isdst=-1)

# Funkcja time.sleep() usypia głowny wątek programu na określoną ilość sekund
i = 0
while i < 10:
    time.sleep(0.1) # usypia wątek programu na sekundę
    print( time.asctime( time.localtime() ) )
    i += 1

# Sat Mar 15 20:55:54 2025
# Sat Mar 15 20:55:54 2025
# Sat Mar 15 20:55:54 2025
# Sat Mar 15 20:55:54 2025
# Sat Mar 15 20:55:54 2025
# Sat Mar 15 20:55:54 2025
# Sat Mar 15 20:55:54 2025
# Sat Mar 15 20:55:54 2025
# Sat Mar 15 20:55:54 2025
# Sat Mar 15 20:55:54 2025
# Sat Mar 15 20:55:54 2025
# Sat Mar 15 20:55:54 2025

# Pomiar czasu wykonywania programu
import time
# pomiar czasu wykonywania kodu
tStart = time.perf_counter()
time.sleep(0.1)
tEnd = time.perf_counter()

# measure wall time
interval = tEnd - tStart
print("Elapsed time:", interval, "second") # Elapsed time: 0.1003515999764204 second

# Praca z czasem i datami - Praca z obiektem datetime
import datetime

datetimeObj = datetime.datetime(2021, 3, 8) # utworzenie obiektu datetime z daty
datetime1 = datetime.datetime(2025, 5, 30, 23, 59, 0) #  utworzenie obiektu datetime z daty i godziny
print(datetime1) # 2025-05-30 23:59:00

datetimeObj = datetime.datetime.now() # aktualny czas i data
print(datetimeObj) # 2025-03-19 13:33:38.301911

print("date():", datetimeObj.date() ) # date(): 2025-03-19
print("time():", datetimeObj.time() ) # time(): 13:33:38.301911
print("timestamp():", datetimeObj.timestamp() ) # timestamp(): 1742387618.301911
print("weekday():", datetimeObj.weekday() ) # weekday(): 2
print("today():", datetimeObj.today() ) # today(): 2025-03-19 13:33:38.302928
print("year:", datetimeObj.year ) # year: 2025
print("month:", datetimeObj.month ) # month: 3
print("day:", datetimeObj.day ) # day: 19
print("hour:", datetimeObj.hour ) # hour: 13
print("minute:", datetimeObj.minute ) # minute: 33
print("second:", datetimeObj.second ) # second: 38
print("microsecond:", datetimeObj.microsecond ) # microsecond: 301911
print("format:", datetimeObj.strftime("%m/%d/%Y %H:%M:%S") ) # format: 03/19/2025 13:33:38

# Daty łatwo porównywać jak np zwykłe liczby
import datetime

datetime1 = datetime.datetime(2025, 5, 30, 23, 59, 0) # Year Month Day Hour Minute Second
datetime2 = datetime.datetime(2025, 5, 30, 23, 59, 10)

print( datetime1 > datetime2 ) # False
print( datetime1 < datetime2 ) # True
print( datetime1 == datetime2 ) # False
print( datetime2 == datetime2 ) # True

date1 = datetime.date(2019, 4, 16) # Year Month Day
date2 = datetime.date(2020, 11, 3)

print( date1 > date2) # False
print( date1 < date2) # True
print( date1 == date2) # False
print( date2 == date2) # True


print('\n----wykład - ćwiczenia-----\n')

import time
import datetime

ticks = time.time() # ilość sekund od 1.01.1970 do becnego czasu
print(ticks) # 1742388492.9221559

timeData = time.localtime() # krotka z aktualną datą i czasem
print(timeData) # time.struct_time(tm_year=2025, tm_mon=3, tm_mday=19, tm_hour=15, tm_min=47, tm_sec=0, tm_wday=2, tm_yday=78, tm_isdst=0)

print(timeData.tm_year) # 2025
print(timeData.tm_mon) # 3
print(timeData.tm_mday) # 19
print(timeData.tm_hour) # 15


# Do funkcji time.localtime() można przekazać również timestamp, czyli ilość sekund od 01.01.1970
timeData = time.localtime(10) # 10 sekund od 01.01.1970r
print(timeData) # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=1, tm_min=0, tm_sec=10, tm_wday=3, tm_yday=1, tm_isdst=0) 
print(timeData.tm_year) # 1970

# Funkcja time.asctime() formatuje w wygodny sposób datę i czas dostarczoną przez time.localtime()
result = time.asctime( time.localtime() )
print(result) # Wed Mar 19 16:23:16 2025


# Funkcja time.strftime() formatuje data i czas na string według podane wzorca, koszysta z oznaczeń,
# które będą zastąpione konkretnymi wartościami w tekście: %Y - rok, %m - miesiąc, %d - dzień,
# %H - godzina, %M - minuty, %S - sekundy
timeData = time.localtime() # krotka - aktualny czas
print( time.strftime( "%d/%m/%Y %H:%M:%S", timeData ) ) # 19/03/2025 16:38:17

# Funkcja time.strptime() parsuje łańcuch znaków i tworzy z niego krotkę z data i czasem.
timeStr = "17:23:45 08.12.2021"
timeData = time.strptime(timeStr, "%H:%M:%S %d.%m.%Y")
print(timeData) # time.struct_time(tm_year=2021, tm_mon=12, tm_mday=8, tm_hour=17, tm_min=23, tm_sec=45, tm_wday=2, tm_yday=342, tm_isdst=-1) 


i = 0
while i < 5:
    time.sleep(0.1) # Wstrzymuje program na 0.1 sekundy
    print( time.asctime(time.localtime()))
    i += 1
# Wed Mar 19 17:10:07 2025
# Wed Mar 19 17:10:07 2025
# Wed Mar 19 17:10:08 2025
# Wed Mar 19 17:10:08 2025
# Wed Mar 19 17:10:09 2025



# time.sleep(1) w Pythonie powoduje wstrzymanie (opóźnienie) działania programu na 1 sekundę.
# Kiedy używać?
# Do wprowadzenia pauzy w pętli (np. czekanie na dane z serwera).
# W testach, np. symulacja opóźnienia użytkownika.
# W animacjach lub efektach wizualnych.
tStart = time.perf_counter() # Zapisuje czas początkowy przed rozpoczęciem pomiaru
time.sleep(1.5) # Wstrzymuje działanie programu na 1,5 sekundy
tEnd = time.perf_counter() # Zapisuje czas końcowy po zakończeniu pomiaru
print("Code took:", (tEnd - tStart), "seconds") # Code took: 1.5004360999446362 seconds / # Oblicza i wyświetla czas wykonania kodu

datetimeObj = datetime.datetime.now()
print(datetimeObj) # 2025-03-20 01:12:51.628591
# print( dir(datetimeObj) ) # po

datetimeObj = datetime.datetime.now()
# print( dir(datetimeObj) ) #  zwraca listę atrybutów i metod dostępnych dla obiektu datetimeObj, który jest instancją klasy datetime.datetime

datetimeObj = datetime.datetime(2025, 3, 10)
datetimeObj = datetime.datetime(2025, 3, 10, 22, 59, 59)

print("date():", datetimeObj.date() ) # date(): 2025-03-10
print("time():", datetimeObj.time() ) # time(): 22:59:59
print("timestamp():", datetimeObj.timestamp() ) # timestamp(): 1741643999.0
print("today():", datetimeObj.today() ) # today(): 2025-03-20 01:23:12.911127
print("year:", datetimeObj.year ) # year: 2025
print("month:", datetimeObj.month ) # month: 3
print("day:", datetimeObj.day ) # day: 10
print("hour:", datetimeObj.hour ) # hour: 22
print("minute:", datetimeObj.minute ) # minute: 59
print("second:", datetimeObj.second ) # second: 59

# datetimeObj.strftime(...) – konwertuje obiekt datetime na łańcuch znaków według podanego wzorca.
# "%H:%M:%S" – godzina (%H – godziny, %M – minuty, %S – sekundy).
# "%d.%m.%y" – data (%d – dzień, %m – miesiąc, %y – rok w formacie dwucyfrowym).
print("Format:", datetimeObj.strftime("%H:%M:%S %d.%m.%y") ) # Format: 22:59:59 10.03.25

datetimeObj = datetimeObj.now()
print("Format:", datetimeObj.strftime("%H:%M:%S %d.%m.%y") ) # Format: 01:51:10 20.03.25

# Porównania daty i czasu
datetime1 = datetime.datetime(2025,1,1, 23,59,59) # Year Month Day Hour Minute Second
datetime2 = datetime.datetime(2030,1,1, 23,59,59)

print( datetime2 > datetime1) # True
print( datetime2 < datetime1) # False
print( datetime2 == datetime1) # False
print( datetime2 == datetime2) # True


date1 = datetime.datetime(2025,1,1) # Year Month Day
date2 = datetime.datetime(2030,1,1) 

print( date2 > date1)  # True
print( date2 < date1)  # False

"""
##################--------------------
print('\n----wykład - ćwiczenia-----\n')

import time
import datetime

ticks = time.time()
print(ticks)

timeData = time.localtime()
print(timeData)
print(timeData.tm_year)

timeData = time.localtime(10)
print(timeData)
print(timeData.tm_year)

result = time.asctime( time.localtime() )
print(result)

timeData = time.localtime()
print( time.strftime( "%d/%m/%Y %H:%M:%S ", timeData ) ) # 09/03/2021 09:25:53

timeStr = "17:23:45 08.12.2021"
timeData = time.strptime(timeStr, "%H:%M:%S %d.%m.%Y")
print(timeData)


i = 0
while i < 12:
    time.sleep(0.000001)
    print( time.asctime(time.localtime()) )
    i += 1


tStart = time.perf_counter()
time.sleep(0.0001)
tEnd = time.perf_counter()
print("Code took: ", (tEnd - tStart), " seconds" )


datetimeObj = datetime.datetime.now()
print(datetimeObj)
# print( dir(datetimeObj) )

datetimeObj = datetime.datetime(2025, 3, 10)
datetimeObj = datetime.datetime(2025, 3, 10, 22, 59, 59)

print("date(): ", datetimeObj.date() )
print("time(): ", datetimeObj.time() )
print("timestamp(): ", datetimeObj.timestamp() )
print("today(): ", datetimeObj.today() )
print("year: ", datetimeObj.year )
print("month: ", datetimeObj.month )
print("day: ", datetimeObj.day )
print("hour: ", datetimeObj.hour )
print("minute: ", datetimeObj.minute )
print("second: ", datetimeObj.second )

print("format: ", datetimeObj.strftime("%H:%M:%S %d.%m.%Y") )

datetimeObj = datetimeObj.now()
print("format: ", datetimeObj.strftime("%H:%M:%S %d.%m.%Y") )


datetime1 = datetime.datetime(2025,1,1, 23,59,59)
datetime2 = datetime.datetime(2030,1,1, 23,59,59)

print( datetime2 > datetime1 )  
print( datetime2 < datetime1 )  

date1 = datetime.date(2025,1,1)
date2 = datetime.date(2027,1,1)

print( date2 > date1 )
print( date2 < date1 )

"""