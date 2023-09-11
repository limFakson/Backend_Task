
from flask import Flask, request, jsonify
import datetime
import pytz  # for timezone handling

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Validate query parameters
    if not slack_name or not track:
        return jsonify({"error": "Both slack_name and track query parameters are required."}), 400

    # Get current day of the week and UTC time
    current_day_of_week = datetime.datetime.now().strftime('%A')
    utc_time = datetime.datetime.now(pytz.utc)

    # Calculate the time difference from UTC
    utc_offset_hours = int(utc_time.strftime('%z')) / 100

    # Check if UTC time is within +/- 2 hours
    if abs(utc_offset_hours) > 2:
        return jsonify({"error": "UTC time is not within +/- 2 hours."}), 400

    # Define the rest of the information
    github_file_repo = "https://github.com/limFakson/Backend_Task"
    github_source_code_url = "https://github.com/limFakson/Backend_Task/blob/main/testerapp.py"
    status_code = 200  # You can customize this based on your application logic

    # Create the JSON response
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day_of_week,
        "utc_time": utc_time.strftime('%Y-%m-%d %H:%M:%S'),
        "track": track,
        "github_repo_url": github_file_repo,
        "github_file_url": github_source_code_url,
        "status_code": status_code
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run()
