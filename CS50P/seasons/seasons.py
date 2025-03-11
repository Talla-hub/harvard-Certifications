from datetime import datetime,date
import sys
import inflect
def main():
    d=input("Date of Birth: ")
    date=Seasons(d)
    print(date)
p = inflect.engine()
class Seasons:
    def __init__(self,birth_date):
        try:
            format = "%Y-%m-%d"
            birth_date = datetime.strptime(birth_date, format).date()
            self.birth_date=birth_date
        except ValueError:
            sys.exit("Invalid date")
    def __str__(self):
        today = date.today()
        dur = today-self.birth_date
        words = p.number_to_words(dur.days*24*60)
        words=words.replace(" and "," ").capitalize()
        return f"{words} minutes"


if __name__ == "__main__":
    main()
