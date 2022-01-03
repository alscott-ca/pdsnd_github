import time
import pandas as pd


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

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("Enter name of city in lower case:").lower()
        if city not in CITY_DATA:
            print("Error, please enter a valid city!")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter month:").lower()
        if month not in ('all', 'january', 'february', 'march', 'april','may', 'june'):
            print("Error, please enter a valid month!")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter day of week:").lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday','sunday'):
            print("Error, please enter a valid day!")
            continue
        else:
            break

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

    df['month'] = df['Start Time'].dt.month

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january','february','march','april','may','june']
        months=months.index(month)+1

        df = df[df['month'] == months]

    if day != 'all':
        df = df[df['day_of_week']==day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]

    print("The most popular month is:", common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]

    print("The most popular day is:", common_day)

    # display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]

    print("The most popular hour is:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most commonly used start station:",df['Start Station'].mode()[0] )

    # display most commonly used end station
    print("Most commonly used end station:",df['End Station'].mode()[0] )

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " and " + df['End Station']
    print("Most commonly used combination of start and end station:",df['combination'].mode()[0] )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time is:", df['Trip Duration'].sum())

    # display mean travel time
    print("Average travel time is:", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(city, df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Number of users by type:", df['User Type'].value_counts())

    if city != 'washington':
    # Display counts of gender
        print("Number of users by gender:", df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
        print("Earliest year of birth year is:", int(df['Birth Year'].min()))
        print("The most recent birth year is:", int(df['Birth Year'].max()))
        print("The most common birth year is:", int(df['Birth Year'].mode()[0]))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def raw_data(df):
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        start_loc = 0
        while (view_data!='no'):
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(city, df)
        raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
