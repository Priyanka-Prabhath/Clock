# Simple Clock Interface

This project is a Python-based analog clock application built using the `tkinter` library. The clock displays the current time in an analog format and allows users to select different timezones.

## Features

- **Analog Clock**: Displays the current time with hour, minute, and second hands.
- **Timezone Selection**: Choose from a list of common timezones to update the clock's time.
- **Digital AM/PM Indicator**: Displays whether the current time is AM or PM.
- **Dynamic Updates**: The clock updates every second.

## Requirements

- Python 3.x
- The following Python libraries:
  - `tkinter` (comes pre-installed with Python)
  - `tzlocal` (installable via pip)

## Installation

1. Clone the repository or download the source code.
2. Ensure you have Python 3.9 or later installed.
3. Install the required dependencies:
   ```
   pip install tzdata
   pip install tzlocal
   ```

## Usage

1. Run the Python script to launch the clock interface:
    ```
    python main.py
    ```
2. The application window will open, displaying the analog clock.
3. Use the dropdown menu to select a timezone. The clock will update to reflect the selected timezone.

## Project Structure

- `clock.py`: The main script that contains the code for the clock interface.
- `README.md`: This file, providing an overview of the project.

## Future Enhancements

- Add support for different time zones.
- Customize the clock's appearance (e.g., colors, fonts).
- Add an alarm or timer functionality.
