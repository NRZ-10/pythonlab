from datetime import datetime, timedelta

# Get today's date
today = datetime.today().date()

# Calculate yesterday and tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

# Print the results
print("Yesterday:", yesterday)
print("Today    :", today)
print("Tomorrow :", tomorrow)
