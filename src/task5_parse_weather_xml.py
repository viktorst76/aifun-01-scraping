import xml.etree.ElementTree as ET
import csv


def parse_weather_xml(xml_file):
    with open(xml_file, "r", encoding="utf-8") as f:
        tree = ET.parse(f)

    root = tree.getroot()
    weather_data = []

    for day in root.findall("day"):
        weather_data.append({
            "date": day.find("date").text.strip(),
            "temperature": float(day.find("temperature").text.strip()),
            "humidity": int(day.find("humidity").text.strip()),
            "precipitation": float(day.find("precipitation").text.strip()),
        })

    return weather_data


def save_to_csv(data, filename="parsed_weather_data.csv"):
    headers = ["Date", "Temperature", "Humidity", "Precipitation"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for row in data:
            writer.writerow([
                row["date"],
                row["temperature"],
                row["humidity"],
                row["precipitation"],
            ])


if __name__ == "__main__":
    # Parse the XML file
    weather_data = parse_weather_xml("src/weather_data.xml")

    # Save the parsed data to a CSV file
    save_to_csv(weather_data)
    print(
        "Data has been successfully parsed and saved to parsed_weather_data.csv."
    )
