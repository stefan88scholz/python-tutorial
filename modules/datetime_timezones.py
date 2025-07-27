from datetime import datetime
import pytz




def main() -> None:
    munich_time = datetime.now()
    print(munich_time)
    print(pytz.all_timezones)
    print(pytz.all_timezones_set)

if __name__ == '__main__':
    main()
