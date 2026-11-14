import csv
import re


def clean_text(line):
    line = line.replace("\xa0", " ")
    line = line.encode("ascii", "ignore").decode("ascii")
    return line


def extract_weather_data(text_file):
    extracted_data = []
    pattern = re.compile(
        r"Date:\s*(\d{4}-\d{2}-\d{2}),\s*"
        r"Max Temp:\s*([-+]?\d*\.?\d+)C?,\s*"
        r"Min Temp:\s*([-+]?\d*\.?\d+)C?,\s*"
        r"Humidity:\s*(\d+)%,\s*"
        r"Precipitation:\s*([-+]?\d*\.?\d+)mm"
    )

    with open(text_file, "r", encoding="utf-8") as f:
        for line in f:
            cleaned = clean_text(line).strip()
            if not cleaned:
                continue
            match = pattern.search(cleaned)
            if match:
                extracted_data.append({
                    "date": match.group(1),
                    "max_temperature": float(match.group(2)),
                    "min_temperature": float(match.group(3)),
                    "humidity": int(match.group(4)),
                    "precipitation": float(match.group(5)),
                })

    return extracted_data

def save_to_csv(data, filename="extracted_weather_data.csv"):
    headers = [
        "Date",
        "Max Temperature",
        "Min Temperature",
        "Humidity",
        "Precipitation",
    ]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for row in data:
            writer.writerow([
                row["date"],
                row["max_temperature"],
                row["min_temperature"],
                row["humidity"],
                row["precipitation"],
            ])


if __name__ == "__main__":
    # Extract data from the text file
    weather_data = extract_weather_data("src/weather_report.txt")

    # Save the extracted data to a CSV file
    save_to_csv(weather_data)
    print(
        "Data has been successfully extracted and saved to extracted_weather_data.csv."
    )
