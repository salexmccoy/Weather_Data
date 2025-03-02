# Extended Icing Forecast ETL Pipeline

##  Project Overview
This project builds an **ETL (Extract, Transform, Load) pipeline** to collect, store, and analyze weather forecasts using the **OpenWeatherMap API**. The goal is to predict and validate **road icing conditions** by analyzing temperature, precipitation, wind speed, and cloud cover data.

##  Project Structure
### **1️. Extract**
- Fetch **5-day weather forecasts** (in 3-hour intervals) from OpenWeatherMap.
- Monitor multiple cities (**Knoxville, Chattanooga**, etc.).
- Store forecasted data at the time of retrieval.

### **2️. Transform**
- Convert timestamps into human-readable format.
- Extract relevant fields:
  - Temperature
  - Precipitation (rain & snow)
  - Wind Speed
  - Cloud Cover
  - Weather Condition
- Identify potential **icing risks** based on weather conditions.

### **3️. Load**
- Store data into a **PostgreSQL database**.
- Maintain separate tables for:
  - **Forecasted conditions**
  - **Actual conditions (for validation)**

## Road Icing Prediction & Validation
The system stores forecasted icing risks and later **compares them to actual weather data** to assess model accuracy. This involves:
1. **Predicting road icing risk** based on forecast data.
2. **Storing predictions** in the database.
3. **Validating accuracy** by comparing forecasted vs. actual weather conditions.
4. **Assessing performance** using SQL queries (confusion matrix, precision/recall, etc.).

##  Setup & Installation
### **1️. Clone the Repository**
```sh
git clone https://github.com/your-repo/weather-etl.git
cd weather-etl
```

### **2️ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️. Configure PostgreSQL**
- Ensure PostgreSQL is installed.
- Update database credentials in `etl_pipeline.py`:
  ```python
  DB_URI = "postgresql+psycopg2://username:password@localhost/weather_db"
  ```

### **4️. Run the ETL Pipeline**
```sh
python etl_pipeline.py
```

### **5️. Query the Database**
Check forecasted weather data:
```sql
SELECT * FROM weather_forecast;
```
Validate icing risk predictions:
```sql
SELECT city, datetime, temperature, precip, cloud_cover, icing_risk FROM road_icing_predictions;
```

##  To-Do List
- [x] Store **forecasted** weather data
- [x] Set up **PostgreSQL** database
- [x] Implement **ETL pipeline**
- [ ] Validate icing risk predictions against actual weather
- [ ] Generate **performance metrics (accuracy, precision, recall)**
- [ ] Clean up and make usr friendly

## Contributing
Feel free to submit issues, feature requests, or improvements via pull requests!

