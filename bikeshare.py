import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input("Would you like to see data for Chicago, New York City, or Washington? (Hint: your answer should be either chicago, new york city, or washington)").lower()
    while city.lower() not in ['chicago', 'new york city', 'washington']:
        print('you should enter one of these valid inputs: chicago, new york city, or washington')
        city = input("Would you like to see data for Chicago, New York, or Washington? (Hint: your answer should be either chicago, new york city, or washington)").lower()
    print('The city name is: ', city)
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month - January, February, March, April, May, June, or All? (Hint: your answer should be either all, january, february, march, april, may, or june)").lower()
    while month.lower() not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        print('you should enter one of these valid inputs: all, january, february, march, april, may, or june')
        month = input("Which month - January, February, March, April, May, June, or All? (Hint: your answer should be either all, january, february, march, april, may, or june)").lower()
    print('The month is: ', month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? (Hint: your answer should be either all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday)").lower()
    while day.lower() not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        print('you should enter one of these valid inputs: all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday')
        day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? (Hint: your answer should be either all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday)").lower()
    print('The day is: ', day)

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
    # Loading data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extract month from Start Time to create new column
    df['month'] = df['Start Time'].dt.month
    # Extract day of week from Start Time to create new column
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # Extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour    
    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)
        # Filter by month to create the new dataframe
        df = df[df['month'] == month]
    # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is:', most_common_month)
    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day of week is:', most_common_day)
    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is:', most_common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:', most_common_start_station)
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is:', most_common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    start_and_end_combination = df['Start Station'] + ' to '+ df['End Station']
    most_frequent_combination = start_and_end_combination.mode()[0]
    print('The most common trip from start to end is:', most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is:', total_travel_time, ' seconds.')
    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('The average travel time is:', round(average_travel_time,2), ' seconds.')
                  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_type = df['User Type'].value_counts()
    print('The counts of user types are: ', counts_of_user_type) 
    # Gender and birth year are only available for new york city and Chicago, so we will use a if loop
    if city != 'washington':
        # TO DO: Display counts of gender
        counts_of_gender = df['Gender'].value_counts()
        print('The counts of user gender are: ', counts_of_gender)
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = df['Birth Year'].min()
        most_recent_year_of_birth = df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print('The earliest year of birth is: ', int(earliest_year_of_birth))
        print('The most recent year of birth is: ', int(most_recent_year_of_birth))
        print('The most common year of birth is: ', int(most_common_year_of_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
# Ask  to view five rows of the filtered data 
def view_data(df):
    view_sellected_data = input("Do you want to view five rows of the selected data? (Hint: your answer should be yes or no)").lower()
    start_view = 0
    while (view_sellected_data == 'yes'):
        print(df.iloc[start_view:start_view + 5])
        start_view += 5
        view_sellected_data = input("Do you want to view the next five rows?: ").lower()
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        view_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
