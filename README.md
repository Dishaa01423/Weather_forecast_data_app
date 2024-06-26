# Streamlit Weather Forecast Application

This Streamlit application provides a weather forecast for multiple days based on user input. It allows users to select a location, specify the number of forecast days, and choose between viewing temperature or sky conditions.

## Features
- Input Controls: Users can input the location, select the number of forecast days via a slider, and choose to view either temperature trends or sky conditions.
- Dynamic Visualization: The application dynamically updates to display the selected weather information using interactive plots and images.
- Error Handling: If the entered place does not exist, the application gracefully handles errors and notifies the user.

## Getting Started
To run this Streamlit application locally, follow these steps:

1. Clone Repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install Dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Application:

```bash
streamlit run app.py
```

## Use the Application:

- Enter the desired location in the text input field.
- Adjust the slider to select the number of forecast days (up to 5 days).
- Select either "Temperature" or "Sky" from the dropdown to view the corresponding weather data.
