SELECT 
    COUNT(*) AS total_predictions,
    SUM(CASE WHEN icing_risk = TRUE AND actual_icing = TRUE THEN 1 ELSE 0 END) AS true_positives,
    SUM(CASE WHEN icing_risk = TRUE AND actual_icing = FALSE THEN 1 ELSE 0 END) AS false_positives,
    SUM(CASE WHEN icing_risk = FALSE AND actual_icing = FALSE THEN 1 ELSE 0 END) AS true_negatives,
    SUM(CASE WHEN icing_risk = FALSE AND actual_icing = TRUE THEN 1 ELSE 0 END) AS false_negatives
FROM road_icing_predictions
JOIN actual_weather ON road_icing_predictions.forecast_time = actual_weather.recorded_time;
