import logging
from datetime import datetime

KEY = "Key TSTFEED0300|7E3E|0400"
LOG_FILE = "hb_test.log"
INPUT_FILE = "hblog.txt"


def setup_logger():
    # configure logger to write WARNING and ERROR to file
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.WARNING,
        format="%(levelname)s - %(message)s",
        filemode="w"
    )


def get_timestamp(line):
    # extract timestamp string from log line and parse it
    ts_index = line.find("Timestamp ") + len("Timestamp ")
    ts_str = line[ts_index:ts_index + 8]
    return datetime.strptime(ts_str, "%H:%M:%S")


def analyze_heartbeats(filtered_lines):
    # compare each pair of lines and log if heartbeat is too large
    for i in range(len(filtered_lines) - 1):
        t1 = get_timestamp(filtered_lines[i])
        t2 = get_timestamp(filtered_lines[i + 1])
        diff = abs((t1 - t2).total_seconds())

        if diff >= 33:
            logging.error(f"Timestamp {t1.strftime('%H:%M:%S')} -> {t2.strftime('%H:%M:%S')} | heartbeat={diff}s")
        elif diff > 31:
            logging.warning(f"Timestamp {t1.strftime('%H:%M:%S')} -> {t2.strftime('%H:%M:%S')} | heartbeat={diff}s")


def analyze():
    setup_logger()

    # read all lines from file
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()

    # filter only lines with our key
    filtered_lines = [line for line in lines if KEY in line]
    print(f"Filtered lines with key: {len(filtered_lines)}")

    analyze_heartbeats(filtered_lines)
    print(f"Analysis done. Check {LOG_FILE}")


analyze()