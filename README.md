# weather-monitoring
# Title
     Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates.
## Description
    The Real-Time Weather Monitoring System is designed to continuously retrieve and analyze weather data from the [OpenWeatherMap API](https://openweathermap.org/). It aggregates this data to provide daily summaries,
    alerts for specific weather conditions, and visualizations for easy interpretation of weather trends.
### Features
    Real-Time Data Retrieval: Fetches weather data for major metros in India (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad) at configurable intervals.
       Daily Weather Summary: Computes daily aggregates, including:
          - Average temperature
          - Maximum temperature
          - Minimum temperature
          - Dominant weather condition (determined by the frequency of occurrences)
     Alerting System: User-defined thresholds for weather parameters, with alerts triggered when conditions exceed specified limits.
     Visualizations: Graphical representations of daily summaries, historical data, and alerts.
#### Data Source
      Weather parameters retrieved from the OpenWeatherMap API:
         - `main`: Main weather condition (e.g., Rain, Snow, Clear)
         - `temp`: Current temperature in Kelvin (converted to Celsius)
         - `feels_like`: Perceived temperature in Kelvin (converted to Celsius)
         - `dt`: Time of the data update (Unix timestamp)
#### Prerequisites
      - Python 3.12.0
      - [OpenWeatherMap API key](https://openweathermap.org/appid) (sign up for a free account)
##### Installation
      Step 1: Clone the Repository
             git clone https://github.com/saipoojitha77/weather-monitoring
             cd weather-monitoring
      Step 2: Set Up a Virtual Environment 
             python -m venv venv
             source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
      Step 3: Install Required Packages
            Create a requirements.txt file with the following content:
              requests
              sqlalchemy
              matplotlib
              schedule     
       Install the dependencies:
              pip install -r requirements.txt       
      Step 4: Configure the Application
              Create a configuration file (e.g., config.py) to store your API key and other settings:
               # config.py
                OPENWEATHERMAP_API_KEY = 'your_api_key_here'
                INTERVAL_MINUTES = 5  # Set your desired interval for data retrieval
###### Implementation Steps
        Data Retrieval:
                 Set up a function to call the OpenWeatherMap API at intervals defined in INTERVAL_MINUTES.
                 Parse the API response to extract relevant weather data for each specified metro.
        Store Raw Data:
                 Implement a storage mechanism (e.g., database or CSV) to keep track of raw weather data for each retrieval.
        Daily Rollup Calculation:
                 At the end of each day, retrieve all weather data collected for that day.
        Calculate daily aggregates:
                 Average temperature
                 Maximum temperature
                 Minimum temperature
                 Dominant weather condition based on occurrences.
        Alert Logic:
                 Continuously monitor current weather conditions against user-defined thresholds.
                 Trigger alerts if conditions exceed specified limits (e.g., temperature exceeds 35°C).
         Visualizations:
                 Utilize libraries like Matplotlib or Plotly to create visual representations of daily summaries, historical data, and alerts.
###### Running the Application
        Start the Weather Monitoring System by executing the main application script:
            python main.py          
###### Test Cases
          1. System Setup
                 Ensure the application starts successfully and connects to the OpenWeatherMap API using a valid API key.
          2. Data Retrieval
                 Simulate API calls at the specified intervals and confirm accurate retrieval and parsing of weather data.
          3. Temperature Conversion
                  Test the conversion of temperature values from Kelvin to Celsius (or Fahrenheit) based on user preferences.
          4. Daily Weather Summary
                  Simulate a sequence of weather updates for multiple days and verify that daily summaries are computed correctly.
          5. Alerting Thresholds
                  Set user-defined thresholds for weather parameters. Simulate conditions exceeding these thresholds to verify that alerts are correctly triggered.
###### Bonus Features
          Extend support for additional weather parameters (e.g., humidity, wind speed).
          Implement functionalities to retrieve weather forecasts and generate summaries based on predicted conditions.
###### License
          This project is licensed under the MIT License. 
###### Acknowledgement          
          OpenWeatherMap API for providing weather data.
          The Python community for contributing tools and libraries utilized in this project.   
