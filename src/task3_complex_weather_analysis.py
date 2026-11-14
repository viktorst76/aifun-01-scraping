import json


def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def analyze_daily_weather(day, temp_threshold=30, wind_threshold=15, humidity_threshold=70):
    max_temp = day["max_temperature"]
    min_temp = day["min_temperature"]
    wind_speed = day["wind_speed"]
    humidity = day["humidity"]
    precipitation = day["precipitation"]

    return {
        "date": day["date"],
        "is_hot_day": max_temp > temp_threshold,
        "temperature_swing": max_temp - min_temp,
        "is_windy_day": wind_speed > wind_threshold,
        "is_uncomfortable_day": humidity > humidity_threshold,
        "is_rainy_day": precipitation > 0,
        "weather_description": day["weather_description"],
        "max_temperature": max_temp,
        "min_temperature": min_temp,
        "wind_speed": wind_speed,
        "humidity": humidity,
        "precipitation": precipitation,
    }

def generate_daily_report(analysis):
    lines = [
        f"Date: {analysis['date']}",
        f"Weather: {analysis['weather_description']}",
    ]

    temp_val = analysis.get("max_temperature", analysis.get("temperature_swing"))
    if temp_val is not None:
        lines.append(f"Temperature: Max {temp_val}°C")

    if analysis.get("is_hot_day"):
        lines.append("It was a hot day.")
    if analysis.get("temperature_swing", 0) > 10:
        lines.append("There was a significant temperature swing.")
    if analysis.get("is_windy_day"):
        lines.append("It was a windy day.")
    if analysis.get("is_uncomfortable_day"):
        lines.append("The humidity made the day uncomfortable.")

    if analysis.get("is_rainy_day"):
        lines.append("It was a rainy day.")
    else:
        lines.append("There was no precipitation.")

    return "\n".join(lines) + "\n"



def summarize_weather_analysis(analyses):
    hottest = max(analyses, key=lambda x: x.get("max_temperature", int(x.get("is_hot_day", False))))
    windiest = max(analyses, key=lambda x: x.get("wind_speed", int(x.get("is_windy_day", False))))
    most_humid = max(analyses, key=lambda x: x.get("humidity", int(x.get("is_uncomfortable_day", False))))
    rainiest = max(analyses, key=lambda x: x.get("precipitation", int(x.get("is_rainy_day", False))))

    hottest_val = hottest.get("max_temperature", hottest.get("is_hot_day"))
    windiest_val = windiest.get("wind_speed", windiest.get("is_windy_day"))
    humid_val = most_humid.get("humidity", most_humid.get("is_uncomfortable_day"))
    rain_val = rainiest.get("precipitation", rainiest.get("is_rainy_day"))

    lines = [
        "Weather Summary:",
        f"Hottest day: {hottest['date']} with a maximum temperature of {hottest_val}°C",
        f"Windiest day: {windiest['date']} with wind speeds of {windiest_val} km/h",
        f"Most humid day: {most_humid['date']} with a humidity level of {humid_val}%",
        f"Rainiest day: {rainiest['date']} with {rain_val} mm of precipitation",
    ]

    return "\n".join(lines)


if __name__ == "__main__":
    # Load the JSON data
    weather_data = load_json("src/tokyo_weather_complex.json")

    # Analyze the weather data for each day
    analyses = [analyze_daily_weather(day) for day in weather_data['daily']]

    # Generate and print daily reports
    for analysis in analyses:
        report = generate_daily_report(analysis)
        print(report)

    # Generate and print a summary report
    summary_report = summarize_weather_analysis(analyses)
    print(summary_report)
