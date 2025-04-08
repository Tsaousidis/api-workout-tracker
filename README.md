# 🏋️ Workout Tracker with Nutritionix & Sheety

A simple Python script that logs your daily workouts using the Nutritionix API to extract exercise data from plain English and saves it to a Google Sheet via Sheety. Just describe your workout (e.g., "ran 3 km and did 20 push-ups") and your activity is logged automatically.

---

## ✨ Features

- Natural language input for exercises ("I cycled for 20 minutes")
- Nutritionix API integration to calculate duration & calories
- Logging workouts with date & time to a Google Sheet
- Uses environment variables for secure API keys

---

## 🚀 How to Use

1. **Clone the repo**
   ```bash
   git clone https://github.com/Tsaousidis/api-workout-tracker.git
   cd api-workout-tracker
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** with the following:
   ```env
   APP_ID=your_nutritionix_app_id
   API_KEY=your_nutritionix_api_key
   SHEETY_USERNAME=your_sheety_username
   SHEETY_PASSWORD=your_sheety_password
   SHEET_ENDPOINT=https://api.sheety.co/your_project/workouts
   ```

4. **Run the script**
   ```bash
   python main.py
   ```

5. **Input your workout** in natural language:
   > What exercise did you do today?
   > `Jogged 4km and did 15 push-ups`

---

## 🛠️ Built With

- [Python](https://www.python.org/)
- [Nutritionix API](https://www.nutritionix.com/business/api)
- [Sheety](https://sheety.co)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://pypi.org/project/requests/)

---

## 🔮 Future Improvements

- Add logging to file instead of only terminal
- Schedule daily reminders
- Export to CSV or other formats
- Add support for voice input (using SpeechRecognition)

---

## 👨‍💻 Created by [Tsaousidis](https://github.com/Tsaousidis)
🎉 Have fun playing! Let me know your thoughts and suggestions! 🎉