# Most Active Cookie
When given a cookie log CSV file in the following format:
```
cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00
```
This command line program will return the most active cookie(s) for a specified day, with "active" being defined as the one(s) seen the most times during a given day.

## Prerequisites
This program is written in [Python 3.8](https://www.python.org/downloads/), which will need to be installed onto your system accordingly. Additionally, the test file uses [pytest](https://docs.pytest.org/en/6.2.x/getting-started.html), which will also need to be installed.

Moreover, this program was run and tested in Ubuntu WSL on Windows 11. While there is no guarantee that this program will work on other operating systems, it likely should work on Windows 10, Linux, and Unix as well.

## Instructions
Within terminal, you can run the *most_active_cookie.py* file as so:

`python3 most_active_cookie.py file.csv -d yyyy-mm-dd`

With `file.csv` being the name of the CSV file and `yyyy-mm-dd` being the timestamp date accordingly.

To run the *test_most_active_cookie.py* file, you simply type: `pytest -v`

### Example
To see the most active cookie on 2018-12-09 in the provided *cookie_log.csv* file, type:

`python3 most_active_cookie.py cookie_log.csv -d 2018-12-09`

Which should output: `AtY0laUfhglK3lC7`
