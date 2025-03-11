def main():
    print(calendar(input("Date: ")))
months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def calendar(date):
    date=date.strip()

    while True:
        try:
            if "," in date:
                date1=date.split(",")
                month,day=date1[0].split(" ")
                year=date1[1]
                # month=months.index(month)
            elif "/" in date:
                month,day,year=date.split("/")
            else:
                month,day,year=date.split(" ")
            if (date==f"{month}/{day}/{year}") and (1<=int(month)<=12) and (1<=int(day)<=30) :
                return f"{year}-{int(month):02}-{int(day):02}"
            elif (month in months) and (date==f"{month} {day},{year}")and (1<=int(months.index(month)+1)<=12) and (1<=int(day)<=30):
                return f"{year}-{int(months.index(month))+1:02}-{int(day):02}"
            date = input("Date: ")
        except ValueError:
            date = input("Date: ")





if __name__ == "__main__":
    main()
