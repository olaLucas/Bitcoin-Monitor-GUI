from datetime import datetime


def conv_timestamp_to_date(timestamp):

    # timestamp is number of seconds since 1970-01-01
    # timestamp = 1676073584

    # convert the timestamp to a datetime object in the local timezone
    dt_object = datetime.fromtimestamp(timestamp)

    # print the datetime object and its type
    # print("Date =", dt_object)
    return dt_object

def conv_date_to_timestamp(date):

    # current date and time
    dt_object = datetime.now()

    # convert from datetime to timestamp
    ts = datetime.timestamp(dt_object)

    # print("Timestamp =", ts)
    return dt_object

# conv_date_to_timestamp(1677245791)
# conv_timestamp_to_date(1677245791)