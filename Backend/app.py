import os
from flask import Flask, jsonify, render_template
from flask_socketio import SocketIO, emit
from influxdb_client import InfluxDBClient
import time
from threading import Thread

app = Flask(__name__)
# app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)

# InfluxDB connection details
influxdb_url = "http://192.168.43.50:8086"
influxdb_token = "yb0Xr3W2YuuUPwqE7SQHijWmXPuHJby-BVfPmp4ZxYw6eYaZGB_Rp0S5D3chZ-gkp9zxe2OR4o9XCkGfSg8zDA=="
influxdb_org = "sofrecom"
influxdb_bucket = "sensor_test_pc"

client = InfluxDBClient(url=influxdb_url, token=influxdb_token)


def fetch_latest_data():
    while True:
        query = f"""
            from(bucket: "{influxdb_bucket}")
                |> range(start: -1d)
                |> filter(fn: (r) => r._measurement == "sensor_temp")
                |> filter(fn: (r) => r._field == "humidity" or r._field == "temperature")
                |> last()
        """

        tables = client.query_api().query(query, org=influxdb_org)
        results = {}
        for table in tables:
            for record in table.records:
                results[record["_field"]] = record.get_value()

        # Emit the latest data through WebSocket
        socketio.emit("update_data", results)

        # Sleep for 1 seconds before fetching data again
        time.sleep(1)


# Start a separate thread to fetch data periodically
fetch_thread = Thread(target=fetch_latest_data)
fetch_thread.daemon = True
fetch_thread.start()


@app.route("/get", methods=["GET"])
def get_latest_data():
    query = f"""
        from(bucket: "{influxdb_bucket}")
            |> range(start: -1d)
            |> filter(fn: (r) => r._measurement == "sensor_temp")
            |> filter(fn: (r) => r._field == "humidity" or r._field == "temperature")
            |> last()
    """

    tables = client.query_api().query(query, org=influxdb_org)
    results = {}
    for table in tables:
        for record in table.records:
            results[record["_field"]] = record.get_value()

    return jsonify(results)


@socketio.on("connect")
def handle_connect():
    print("Client connected")
    # Emit event to notify the client to fetch data from /get
    emit("fetch_data")


@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=3003, debug=True)
