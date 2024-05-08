import influxdb_client, os, time

# from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "yb0Xr3W2YuuUPwqE7SQHijWmXPuHJby-BVfPmp4ZxYw6eYaZGB_Rp0S5D3chZ-gkp9zxe2OR4o9XCkGfSg8zDA=="
org = "sofrecom"
url = "http://192.168.43.50:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket = "sensor_test_pc"

# write_api = client.write_api(write_options=SYNCHRONOUS)

# for value in range(5):
#     point = (
#         influxdb_client.Point("measurement1")
#         .tag("tagname1", "tagvalue1")
#         .field("field1", value)
#     )
#     write_api.write(bucket=bucket, org="sofrecom", record=point)
#     time.sleep(1)  # separate points by 1 second

query_api = client.query_api()

query = """
    from(bucket: "sensor_test_pc")
        |> range(start: -1d)
        |> filter(fn: (r) => r._measurement == "sensor_temp")
        |> filter(fn: (r) => r._field == "humidity" or r._field == "temperature")
        |> last()
"""


while True:
    # Execute the query to fetch the latest data
    tables = query_api.query(query, org=org)

    for table in tables:
        for record in table.records:
            field_value = record.get_value()
            print(record["_field"], "Value:", field_value)

    time.sleep(2)
