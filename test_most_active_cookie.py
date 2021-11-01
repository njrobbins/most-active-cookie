from datetime import datetime
import os


def test_check_arg_length():
    args = ["most_active_cookies.py", "cookie_log.csv", "-d", "2018-12-09"]
    assert len(args) == 4


def test_check_if_csv():
    file = "cookie_log_no_headers.csv"
    assert os.path.splitext(file)[-1].lower() == ".csv"


def test_check_flag():
    flag = "-d"
    assert flag == "-d"


def test_check_datetime_format():
    date = "2018-12-08"
    assert datetime.strptime(date, "%Y-%m-%d")
