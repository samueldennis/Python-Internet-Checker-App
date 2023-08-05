# Network Connection Monitor Documentation

## Overview

The Network Connection Monitor is a Python application that allows users to monitor the quality of their network connection by periodically sending ping requests to a specified server (in this case, "google.com"). The application calculates and displays the ping rate in milliseconds, indicating the responsiveness of the network. Additionally, it identifies and reports connection losses or temporary disruptions.

## Prerequisites

Before running the Network Connection Monitor application, ensure that you have the following prerequisites installed on your system:

- Python 3.x
- `ping3` library (can be installed using `pip install ping3`)

## Installation

1. Clone or download the repository containing the Network Connection Monitor application to your local machine.

2. Open a terminal or command prompt and navigate to the directory where you've saved the application files.

## Usage

1. Open a terminal or command prompt and navigate to the directory where you've saved the application files.

2. Run the application by executing the following command:

   ```
   python network_connection_monitor.py
   ```

3. The application will start sending ping requests to the specified server ("google.com") at regular intervals (1 second by default). It will calculate the ping rate in milliseconds and display the result in the console.

4. If the connection is temporarily lost, the application will display the message "Connection temporarily lost."

5. If the connection is completely lost, the application will display the message "Connection Lost."

6. To stop the application, press `Ctrl + C`. The application will catch the `KeyboardInterrupt` signal and terminate gracefully.

## Application Structure

The Network Connection Monitor application consists of a single Python script:

- `network_connection_monitor.py`: This script contains the main functionality of the application.

## Functions

### `check_connection()`

This function attempts to send a ping request to the specified server ("google.com") using the `ping3` library. If the ping is successful, the function returns the ping time in seconds, which is then converted to milliseconds. If the ping is not successful (due to an exception), the function returns `None`.

### `display_ping_rate(ping_rate)`

This function takes the calculated ping rate as an argument and displays it in the console. It provides different messages based on the ping rate value: if the ping rate is greater than 0.00, it displays the ping rate in milliseconds; if the ping rate is exactly 0.00, it displays "Connection temporarily lost"; if the ping rate is less than 0.00 (indicating a connection loss), it displays "Connection Lost."

### `main()`

The main function of the application. It runs an infinite loop where it continuously checks the network connection using the `check_connection()` function and displays the ping rate using the `display_ping_rate()` function. The loop is interrupted by a `KeyboardInterrupt` exception (triggered by `Ctrl + C`), which gracefully terminates the application and displays a termination message.

## Customization

- You can modify the `GOOGLE_SERVER` variable to use a different server for ping testing.
- Adjust the interval between ping tests by modifying the `time.sleep()` value within the `main()` function.

## Conclusion

The Network Connection Monitor application provides a straightforward way to monitor network connectivity and responsiveness by sending ping requests to a specified server. By following the installation and usage instructions, you can easily run the application and keep an eye on your network's stability.