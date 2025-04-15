# 🧠 Google Form(Single page) Auto Filler Bot using Selenium (Edge Browser)

This Python script automatically fills out and submits a Google Form multiple times using random answers. It supports English and Bangla language forms and handles different question types like **radio buttons** and **checkboxes**.

## 🚀 Features

- Submits the form `n` times (default: 150)
- Handles radio button and checkbox inputs
- Randomly select one or more answers
- Works with multilingual forms (English/Bangla)
- Adds slight delays to simulate human behavior
- Supports Microsoft Edge via `msedgedriver`

## **🧩 Requirements**

You need to have the following installed:

- Python 3.x
- Selenium: You can install it using **Bash**:
  `pip install selenium`
- Edge WebDriver: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver

  
## **🔧 Setup**

Clone this repository or download the script.
Replace the following placeholders in the script:

**EDGE_DRIVER_PATH → Path to your msedgedriver.exe**

**FORM_URL → Full link to your Google Form**


Run the script using **Bash**:
`python google_form_filler_bot.py`
