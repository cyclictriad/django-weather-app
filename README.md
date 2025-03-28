# Django Weather App

A simple Django web application that fetches and displays weather data for a given city using the OpenWeatherMap API.

---

## Features

- Enter a city name to get current weather information.
- Displays temperature, weather description, humidity, and wind speed.
- Built with Django and the OpenWeatherMap API.

---

## Prerequisites

Before running the app, ensure you have the following installed:

- Python 3.x
- Django
- An API key from [OpenWeatherMap](https://openweathermap.org/api)

---

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/cyclictriad/weather_app.git
   cd weather_app
   ```

2. **Set up a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your OpenWeatherMap API key**:

   - Open `weather_project/settings.py`.
   - Add your API key:
     ```python
     OPENWEATHERMAP_API_KEY = 'your_api_key_here'
     ```

5. **Run migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

7. **Open your browser**:
   Visit `http://127.0.0.1:8000/` to use the app.

---

## Usage

1. Enter the name of a city in the input field.
2. Click "Get Weather" to view the current weather information for that city.

---
