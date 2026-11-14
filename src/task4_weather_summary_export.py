import json
import csv


def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def summarize_weather_data(data):
    n = len(data)
    return {
        "average_max_temp": sum(d["max_temperature"] for d in data) / n,
        "average_min_temp": sum(d["min_temperature"] for d in data) / n,
        "total_precipitation": sum(d["precipitation"] for d in data),
        "average_wind_speed": sum(d["wind_speed"] for d in data) / n,
        "average_humidity": sum(d["humidity"] for d in data) / n,
        "hot_days": sum(1 for d in data if d["max_temperature"] > 30),
        "windy_days": sum(1 for d in data if d["wind_speed"] > 15),
        "rainy_days": sum(1 for d in data if d["precipitation"] > 0),
    }

def export_to_csv(data, file):
    headers = [
        "Date",
        "Max Temperature",
        "Min Temperature",
        "Precipitation",
        "Wind Speed",
        "Humidity",
        "Weather Description",
        "Is Hot Day",
        "Is Windy Day",
        "Is Rainy Day",
    ]

    def _write_rows(f):
        writer = csv.writer(f)
        writer.writerow(headers)
        for d in data:
            writer.writerow([
                d["date"],
                d["max_temperature"],
                d["min_temperature"],
                d["precipitation"],
                d["wind_speed"],
                d["humidity"],
                d["weather_description"],
                d["max_temperature"] > 30,
                d["wind_speed"] > 15,
                d["precipitation"] > 0,
            ])

    if isinstance(file, str):
        with open(file, "w", newline="", encoding="utf-8") as f:
            _write_rows(f)
    else:
        _write_rows(file)


if __name__ == "__main__":
    # Load the JSON data
    weather_data = load_json("src/tokyo_weather_complex.json")

    # Summarize the weather data
    summary = summarize_weather_data(weather_data['daily'])

    # Print the summary for verification
    print("Weather Data Summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")

    # Export the summarized data to a CSV file
    export_to_csv(weather_data['daily'], "tokyo_weather_summary.csv")

    print("Data successfully exported to tokyo_weather_summary.csv")
