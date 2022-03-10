import random
from datetime import datetime
import pandas as pd
import os
import urllib.request as req

# path setup

path = os.path.dirname(os.path.realpath(__file__))


def UpdateExcel():
    # update Excel +- every week or more often
    try:
        if pd.Timestamp('2022-02-01 00:00:00') < pd.Timestamp(datetime.now()):
            req.urlretrieve(
                "https://docs.google.com/spreadsheets/d/1hBz8I_eg-kSce2fDTeLi2XDaU9tnBYs-tCW-bfIwk28/export?format=xlsx",
                path + r"\workingexcel.xlsx")
        else:
            req.urlretrieve(
                "https://docs.google.com/spreadsheets/d/1W1vcDHVbj8EBOpxcKXdTp9gyQfPLU79cH_7ZYzRKEIE/export?format=xlsx",
                path + r"\workingexcel.xlsx")
    except Exception as ex:
        print(ex)


def UpdateDailyTxt():
    # updates the txt file for daily changes
    try:
        req.urlretrieve("https://docs.google.com/document/d/1clr3jbOEXrIDjTDpJmHHQKZ4n_lHiATOkTN0I7bqVng/export?format=txt", path + r"\dailychanges.txt")
    except Exception as ex:
        print(ex)


def GetXEvents(number_of_rows=1):
    if number_of_rows > 30:
        number_of_rows = 30
    # gets events for X days, starting today from excel file
    df = pd.read_excel(path + r'\workingexcel.xlsx', usecols=[0, 1, 2, 4, 12], skiprows=2, sheet_name="שכבת יב")
    l = df.values.tolist()
    # gets data
    df = pd.read_excel(path + r'\workingexcel.xlsx', usecols=[0, 1, 2, 4, 12], nrows=2, sheet_name="שכבת יב")
    l2 = df.values.tolist()
    # gets headers
    headers = []
    days = []
    i = 0
    datefound = False
    for row in l2:
        headers = row
    today = datetime.today()
    refdate = today.strftime("%d-%m-%Y")
    for row in l:
        checkdate = row[0].strftime("%d-%m-%Y")
        if checkdate == refdate or datefound:
            number_of_rows -= 1
            datefound = number_of_rows > 0
            counter = 0
            for i, item in enumerate(row):
                if item != item:
                    counter += 1
                    row[i] = 'No events'  # replace nan with "No events" for better readability
            if counter == 3:
                days.append(f"({checkdate}) has no events")
            else:
                days.append(dict(zip(headers, row)))

    return days


def DailyChanges(): 
    # as long as google docs is used, if an update to link is needed - https://sites.google.com/a/haderahigh.org.il/main/news_main/changes
    # -> view source -> search "https://docs.google.com/document/"
    UpdateDailyTxt()
    text = (open(path + r'\dailychanges.txt', "r", encoding="utf8")).readlines()
    first_line = text[0]
    try:
        for line in text[0:(text.index('שכבת יב’ \n') - 1)]:
            text.remove(line)
            
        return first_line + '\n'.join(text)
    except Exception as ex:
        print(ex)
        return "No Special Events Today"


def PostProcrastination():
    # very cool
    random.random()
    cool_videos = ["https://www.youtube.com/watch?v=-Kobdb37Cwc", "https://www.youtube.com/watch?v=3DXyRsOQ9Is"]
    random_string = """{0}
```
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
[=========]```""".format(random.choice(cool_videos))
    return random_string
