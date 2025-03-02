CREATE TABLE road_icing_predictions (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    prediction_time TIMESTAMP,
    forecast_time TIMESTAMP,
    temperature FLOAT,
    precip FLOAT,
    cloud_cover INT,
    wind_speed FLOAT,
    icing_risk BOOLEAN
);
CREATE TABLE actual_weather (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    recorded_time TIMESTAMP,
    temperature FLOAT,
    precip FLOAT,
    cloud_cover INT,
    wind_speed FLOAT,
    actual_icing BOOLEAN
);