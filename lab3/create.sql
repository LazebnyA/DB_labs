CREATE TABLE IF NOT EXISTS weather_data (
    country VARCHAR(255),
    location_name VARCHAR(255),
    latitude DECIMAL(10, 2),
    longitude DECIMAL(10, 2),
    timezone VARCHAR(255),
    last_updated_epoch BIGINT,
    last_updated DATETIME,
    temperature_celsius DECIMAL(5, 2),
    temperature_fahrenheit DECIMAL(5, 2),
    condition_text VARCHAR(255),
    wind_mph DECIMAL(5, 2),
    wind_kph DECIMAL(5, 2),
    wind_degree INT,
    wind_direction VARCHAR(3) CHECK (wind_direction IN ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')),
    pressure_mb DECIMAL(6, 2),
    pressure_in DECIMAL(6, 2),
    precip_mm DECIMAL(5, 2),
    precip_in DECIMAL(5, 2),
    humidity INT,
    cloud INT,
    feels_like_celsius DECIMAL(5, 2),
    feels_like_fahrenheit DECIMAL(5, 2),
    visibility_km DECIMAL(5, 2),
    visibility_miles DECIMAL(5, 2),
    uv_index DECIMAL(5, 2),
    gust_mph DECIMAL(5, 2),
    gust_kph DECIMAL(5, 2),
    air_quality_Carbon_Monoxide DECIMAL(6, 2),
    air_quality_Ozone DECIMAL(6, 2),
    air_quality_Nitrogen_dioxide DECIMAL(6, 2),
    air_quality_Sulphur_dioxide DECIMAL(6, 2),
    air_quality_PM25 DECIMAL(6, 2),
    air_quality_PM10 DECIMAL(6, 2),
    air_quality_us_epa_index INT,
    air_quality_gb_defra_index INT,
    sunrise TIME,
    sunset TIME,
    moonrise TIME,
    moonset TIME,
    moon_phase VARCHAR(255),
    moon_illumination INT
);