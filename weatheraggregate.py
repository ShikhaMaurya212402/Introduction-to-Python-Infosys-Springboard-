def weather_summary(weather):
    # Find hottest day
    hottest_day = max(weather, key=lambda x: x["temp"])["day"]

    # Calculate average temperature
    total_temp = sum(day["temp"] for day in weather)
    avg_temp = round(total_temp / len(weather), 2)

    # Count rainy days
    rainy_days = sum(1 for day in weather if day["rain"])

    # Summary dictionary
    summary = {
        "hottest_day": hottest_day,
        "average_temperature": avg_temp,
        "rainy_days": rainy_days
    }

    return summary
weather = [
    {"day": "Mon", "temp": 32, "rain": False},
    {"day": "Tue", "temp": 35, "rain": True},
    {"day": "Wed", "temp": 30, "rain": False}
]

result = weather_summary(weather)
print()
print(result)
