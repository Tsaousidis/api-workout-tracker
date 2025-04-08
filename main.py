
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# User's physical attributes required by Nutritionix API
GENDER = "male"
WEIGHT_KG = 78 
HEIGHT_CM = 178 
AGE = 28 

# API credentials and endpoints (stored securely in .env)
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")

# Nutritionix API endpoint for natural language processing
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"


def get_exercise_data(query):
    """Sends a workout description to Nutritionix and returns structured data."""
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    }

    body = {
        "query": query,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }

    response = requests.post(url=EXERCISE_ENDPOINT, json=body, headers=headers)
    response.raise_for_status()
    return response.json()


def log_exercise_to_sheet(exercises):
    """Logs each exercise to Google Sheets via Sheety API."""
    date = datetime.now().strftime("%d/%m/%Y")
    time = datetime.now().strftime("%H:%M:%S")

    for exercise in exercises:
        sheet_data = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }

        response = requests.post(
            SHEET_ENDPOINT,
            json=sheet_data,
            auth=(SHEETY_USERNAME, SHEETY_PASSWORD)
        )
        response.raise_for_status()
        print(f"Logged: {exercise['name'].title()} - {exercise['duration_min']} min")


def main():
    """Main script flow: input, fetch, log."""    
    try:
        user_input = input("What exercise did you do today? ")
        exercise_result = get_exercise_data(user_input)
        log_exercise_to_sheet(exercise_result["exercises"])
        print("Workout logged successfully!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()