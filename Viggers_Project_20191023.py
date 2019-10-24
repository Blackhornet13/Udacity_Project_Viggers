import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_list = ["Chicago", "New York City", "Washignton"]
    city =str(input('Which city would you like to search: "Chicago", "New York City", "Washignton" \n'))
    while city not in {"Chicago", "New York City", "Washignton"}:
        city = input("Please enter a valid input (check spacing & Caps): ")

    month_list = ["january", "february", "march", "april", "may", "june", "all"]
    month = str(input('Which month would you like to filter to: "january", "february", "march", "april", "may", "june", "all"\n'))
    while month not in {"january", "february", "march", "april", "may", "june", "all"}:
        month = input("Please enter a valid input (check spacing & Caps): ")

    day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "all"]
    day = str(input('Which day of the week would you like to filter to: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "all" \n'))
    while day not in {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "all"}:
        day = input("Please enter a valid input (check spacing & Caps): ")

    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df ['Start Time'] = pd.to_datetime(df['Start Time'])
    df ['month'] = df['Start Time'].dt.month
    df ['day_of_week'] = df['Start Time'].dt.dayofweek.name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] ==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    most_frequent_month = month.mode()[0]
    print('Most Common Month: {}'.format(most_frequent_month))

    # TO DO: display the most common day of week
    most_frequent_day = day.mode()[0]
    print('Most Common Day: {}'.format(most_frequent_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_frequent_start_hr = df['hour'].mode()[0]
    print('Most Common Start Hour: {}'.format(most_frequent_start_hr))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    def getStarts(freq_start):
        return freq_start.keys()
    freq_start = df['Start Station'].value_counts()
    print('Most Commonly Used Start Station: {}'.format(getStarts(freq_start)[0]))


    # TO DO: display most commonly used end station
    def getEnds(freq_end):
        return freq_end.keys()
    freq_end = df['End Station'].value_counts()
    print('Most Commonly Used End Station: {}'.format(getEnds(freq_end)[0]))


    # TO DO: display most frequent combination of start station and end station trip
    df['StartEnd Station'] = 'START: '+ df['Start Station'] + ' & END: ' + df['End Station']
    def getStartEnd(freq_startend):
            return freq_startend.keys()

    freq_startend = df['StartEnd Station'].value_counts()
    mx_se = max(freq_startend.items(),key = lambda x:x[1])
    max_list = [i[0] for i in freq_startend.items() if i[1]==mx_se[1]]
    for i in range(len(max_list)):
        print("Most Commonly Start-End Combo(s): {}".format(max_list[i],'\n'))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print("Total Travel Time: {} minutes".format(total_travel_time))

    # TO DO: display mean travel time
    average_travel_time = sum(df['Trip Duration'])/len(df['Trip Duration'])
    print("Average Travel Time: {} minutes".format(average_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].fillna("No data given").value_counts()
    print("User Types and Counts: {}".format(user_types))

    # TO DO: Display counts of gender
    user_gender = df['Gender'].fillna("No data given").value_counts()
    print("User Genders and Counts: {}".format(user_gender))


    # TO DO: Display earliest, most recent, and most common year of birth
    birthdays = df['Birth Year']
    print("Earliest Birthyear: {}".format(min(birthdays)))
    print("Most Recent Birthyear: {}".format(max(birthdays)))
    print("Most Common Birthyear: {}".format(birthdays.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
