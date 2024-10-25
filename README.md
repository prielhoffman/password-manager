# Password Manager

A simple password manager application built with Python and Tkinter, allowing users to generate, store, and retrieve passwords securely.

## Features

* **Password Generator**: Generates strong, random passwords with a mix of letters, numbers, and symbols.
* **Save Password**: Stores website credentials (website name, email/username, and password) in a local JSON file.
* **Search Password**: Allows users to search for saved credentials by website name.
* **Clipboard Copying**: Automatically copies the generated password to the clipboard.

## Requirements

* Python 3.x
* Packages:
  - tkinter (included in Python's standard library)
  - pyperclip (for clipboard functionality)
  - json (for data storage in JSON format, included in Python's standard library)

## How to Use

1. **Clone the repository**:
    ```bash
    git clone https://github.com/username/password-manager.git
    ```
2. **Install the required package**:
    ```bash
    pip install pyperclip
    ```
3. **Run the application**:
    ```bash
    python main.py
    ```

## Application Workflow

1. **Generate Password**: Click the "Generate Password" button to create a strong password, which will be automatically copied to your clipboard.
2. **Save Password**: Enter the website name, email/username, and password. Click "Add" to save this information in `data.json`.
3. **Search Password**: Retrieve saved login details by entering the website name and clicking "Search".

## Project Structure

* `main.py`: Main script for the password manager application.
* `logo.png`: Logo image displayed in the application's UI.
* `data.json`: JSON file where all saved passwords are stored.

## License

This project is open-source and available under the MIT License.

## Acknowledgements

Inspired by Angela Yu’s course on Python development ("100 Days of Code: The Complete Python Pro Bootcamp" on Udemy).
