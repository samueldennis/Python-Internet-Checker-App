import ping3
import time

GOOGLE_SERVER = "google.com"

def check_connection():
    try:
        ping_time = ping3.ping(GOOGLE_SERVER)
        if ping_time is not None:
            return ping_time * 1000  # Convert to milliseconds
        else:
            return None
    except Exception:
        return None

def display_ping_rate(ping_rate):
    if ping_rate > 0.00:
        print(f"Ping Rate: {ping_rate:.2f} ms")
    elif ping_rate == 0.00:
        print("Connection temporarily lost")
    else:
        print("Connection Lost")

def main():
    try:
        while True:
            ping_rate = check_connection()
            display_ping_rate(ping_rate)
            time.sleep(1)

    except KeyboardInterrupt:
        print("App terminated by the user.")

if __name__ == "__main__":
    main()
