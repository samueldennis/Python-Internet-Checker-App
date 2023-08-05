# Internet Speed Monitor Documentation

## Overview

The Internet Speed Monitor is a Python application that allows users to measure and monitor their internet connection's download and upload speeds using the Speedtest.net API. The application repeatedly performs speed tests at specified intervals and displays the results in the console.

## Prerequisites

Before running the Internet Speed Monitor application, ensure that you have the following prerequisites installed on your system:

- Python 3.x
- `speedtest-cli` library (can be installed using `pip install speedtest-cli`)

## Installation

1. Clone or download the repository containing the Internet Speed Monitor application to your local machine.

2. Open a terminal or command prompt and navigate to the directory where you've saved the application files.

## Usage

1. Open a terminal or command prompt and navigate to the directory where you've saved the application files.

2. Run the application by executing the following command:

   ```
   python internet_speed_monitor.py
   ```

3. The application will start performing speed tests at regular intervals (1 second by default) and display the download and upload speeds in kilobits per second (kbps) in the console.

4. To stop the application, press `Ctrl + C`. The application will catch the `KeyboardInterrupt` signal and terminate gracefully.

## Application Structure

The Internet Speed Monitor application consists of a single Python script:

- `internet_speed_monitor.py`: This script contains the main functionality of the application.

## Functions

### `get_internet_speed()`

This function initializes a Speedtest instance, retrieves the best server, performs a download speed test, and an upload speed test. The results are converted from bits per second (bps) to kilobits per second (kbps) and returned as a tuple of download and upload speeds.

### `display_speed(download_speed, upload_speed)`

This function takes the download and upload speeds as arguments and prints them in a formatted manner to the console.

### `main()`

The main function of the application. It runs an infinite loop where it continuously retrieves the internet speed using the `get_internet_speed()` function and displays it using the `display_speed()` function. The loop is interrupted by a `KeyboardInterrupt` exception (triggered by `Ctrl + C`), which gracefully terminates the application and displays a termination message.

## Customization

- You can adjust the interval between speed tests by modifying the `time.sleep()` value within the `main()` function.

## Conclusion

The Internet Speed Monitor application provides a simple way to measure and monitor your internet connection's download and upload speeds using the Speedtest.net API. By following the installation and usage instructions, you can easily run the application and keep track of your network's performance over time.