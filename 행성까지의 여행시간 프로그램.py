planet = {"수성":91700000 ,"금성":41400000, "화성":78400000,
           "목성":628700000, "토성":1277400000, "천왕성":2750400000,
           "해왕성":4347400000}

planetname = input("행성 이름: ")
speed = int(input("이동속도(단위는km/h): "))

time = planet[planetname] / speed
year = time // (365*24)
month = (time - year*365*24) // (30*24)
day = (time - year*365*24 - month*30*24) // 24
hour = time - year*365*24 - month*30*24- day*24

print("이동시간: 약", time, "시간")
print("이동시간: 약", year, "년", month, "월", day, "일", hour, "시간")
