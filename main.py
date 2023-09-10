from http import HTTPStatus
import datetime
import random
import pytz
from flask import Flask, request, jsonify

# initialize Flask
app = Flask(__name__)

# unsort json data
app.json.sort_keys = False


# Get the current time in UTC
utc_now = datetime.datetime.now(pytz.utc)

# Add a random time delta within +/- 2 minutes

time_delta = datetime.timedelta(minutes=random.randint(-2, 2))
utc_time_with_window = utc_now + time_delta

current_utc_time = utc_time_with_window.strftime('%Y-%m-%dT%H:%M:%SZ')

# Get the day

day = datetime.datetime.now()

@app.route('/get_info', methods=['GET'])

def get_info():
    # Get query parameters from the request
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Check if both parameters are provided
    if slack_name is None or track is None:
        return jsonify({'error': 'Both slack_name and track are required'}), 400

    # Create the response JSON
    response = {
        "slack_name": "Oladapo Cole",
        "current_day": day.strftime("%A"),
        "utc_time": current_utc_time,
        "track": "Backend",
        "github_file_url": "https://github.com/olaco/Hng_endpoint/blob/master/api.py",
        "github_repo_url": "https://github.com/olaco/Hng_endpoint",
        "status_code": HTTPStatus.OK
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
