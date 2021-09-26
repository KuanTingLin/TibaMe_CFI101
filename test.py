import sys
from datetime import datetime, timedelta
import time
import os
from test.test_file import current_file_dir
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('-g',
                    '--group',
                    help='Type of mail',
                    dest='group',
                    type=str,
                    default='C0203000063')

parser.add_argument('-t',
                    '--time',
                    help='due time',
                    dest='due_time',
                    type=str)

parser.add_argument('-s',
                    '--seconds',
                    help='seconds of countdown',
                    dest='seconds',
                    type=int)


def clock(due_time, fmt="%Y-%m-%d %H:%M:%S"):
    """
    :param due_time: str or datetime object, example: 2020-09-26 11:02:11
    :param fmt: str
    :return:
    """
    if isinstance(due_time, str):
        due_time = datetime.strptime(due_time, fmt)
    elif isinstance(due_time, datetime):
        pass
    else:
        return False

    if due_time < datetime.today():
        return False

    while due_time.strftime("%H:%M:%S") > datetime.today().strftime("%H:%M:%S"):
        today = datetime.today()
        delta_seconds = (due_time - today).seconds
        if (delta_seconds <= 10):
            print("\r",
                  "現在時間為:",
                  today.strftime("%H:%M:%S"),
                  "距離目標時間",
                  due_time.strftime("%H:%M:%S"),
                  "剩餘 {} 秒鐘".format(str(delta_seconds).zfill(2)), end="")
            time.sleep(1)
    print()
    print("Ring~~~~~")


def countdown(second=0, minute=0, hour=0):
    total_time = hour * 3600 + minute * 50 + second
    for i in range(total_time):
        print("\r剩餘{}秒".format(str(total_time - i).zfill(len(str(total_time)))),
              end="")
        time.sleep(1)
    print("\n", "Ring~~~~~")


if __name__ == "__main__":
    args = parser.parse_args()
    # print(args)
    if args.due_time:
        clock(args.due_time)
    elif args.seconds:
        countdown(args.seconds)
    # clock(args.due_time)

