with open("Log - 284ccb82e8f74080a3fa670198c930b5.txt", "r") as file:
    count=0
    for each in file:
        count+=1
    print(count)
time_sec = 80 * count * 8
time_day = ((time_sec/60)/60)
print(f"Expected time: {time_day}")