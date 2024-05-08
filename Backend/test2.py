import os
import configparser
from flask import Flask, jsonify
from influxdb_client import InfluxDBClient

app = Flask(__name__)

# Read configuration from example.cfg
config = configparser.ConfigParser()
config.read("example.cfg")

# InfluxDB connection details
influxdb_url = config.get("InfluxDB", "influxdb_url")
influxdb_token = config.get("InfluxDB", "influxdb_token")
influxdb_org = config.get("InfluxDB", "influxdb_org")
influxdb_bucket = config.get("InfluxDB", "influxdb_bucket")

print(influxdb_token)
