import speedtest
import time

def get_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 1000  # Convert to kbps
    upload_speed = st.upload() / 1000  # Convert to kbps

    return download_speed, upload_speed

def display_speed(download_speed, upload_speed):
    print(f"Download Speed: {download_speed:.2f} kbps")
    print(f"Upload Speed: {upload_speed:.2f} kbps")

def main():
    try:
        while True:
            download_speed, upload_speed = get_internet_speed()
            display_speed(download_speed, upload_speed)
            time.sleep(1)

    except KeyboardInterrupt:
        print("App terminated by the user.")

if __name__ == "__main__":
    main()

