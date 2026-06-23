import datetime


def main():
    now = datetime.datetime.now()

    if 9 < now.hour < 12:
        print(f"현재 시각은 {now.hour}로 오전입니다.")
    elif now.hour < 9:
        print(f"현재 시각은 {now.hour}로 새벽입니다.")
    else: 
        print(f"현재 시각은 {now.hour}로 오후입니다.")

if __name__ == "__main__":
    main()


now = now
print(now.month, type(now.month))




if __name__ == "__main__":
    main()