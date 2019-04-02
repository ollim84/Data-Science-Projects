import pandas as pd
from datetime import date
import csv



start_date = date(2018, 1, 1)
end_date = date(2018, 12, 31)

daterange = pd.date_range(start_date, end_date)

minutesList = {}
timesCancelled = 0

for single_date in daterange:
    date_string = single_date.strftime("%Y-%m-%d")
    url_string = 'https://rata.digitraffic.fi/api/v1/trains/{}/45'.format(date_string)

    # Read the json into a pandas dataframe:
    c = pd.read_json(url_string)


    # If there is information available
    if(len(c) != 0):

        # The values that we need are in the time table rows
        temp_list = c.iloc[0]["timeTableRows"]

        for item in range(0, len(temp_list)):
            temp_string = temp_list[item]

            if (temp_string['stationShortCode'] == 'VTR' and temp_string['type'] == 'ARRIVAL'):

                print(date_string)

                # Get the arrival time if the train has not been cancelled
                if(temp_string['cancelled'] == False):

                    difference = temp_string['differenceInMinutes']
                    minutesList[date_string] = difference
                else:
                    timesCancelled += 1

    # Train might not run due to holidays
    else:
        print(url_string)


# Write the 2018 values into a CSV file.
with open('2018_values.csv','wb') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(['Date', 'Delay'])
    w.writerows(minutesList.items())


# TODO: Write the values into a database (mySQL or influxDB)