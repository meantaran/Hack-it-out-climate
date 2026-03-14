PyClimaExplorer

PyClimaExplorer is a full-stack climate data visualization web application that allows users to explore, analyze, and generate reports from climate datasets interactively.
The application provides a modern dashboard where users can search any location in the world, visualize climate trends, and export climate reports.

This project was built as a rapid-prototype scientific visualization tool to transform raw climate datasets into meaningful visual insights.

🚀 Features
🔐 User Authentication

User registration and login system

Secure password hashing

SQLite database for storing user accounts

🌍 Interactive Climate Dashboard

Search any city or location

Convert location to latitude and longitude

Analyze climate data for that region

📊 Climate Data Visualization

Interactive climate trend graphs

Monthly temperature visualization

Real-time chart rendering using Chart.js

🌎 3D Earth Visualization

Interactive rotating globe

Visual exploration of the planet

📄 Climate Report Generator

Generate downloadable PDF climate reports

Includes:

Location name

Climate variable

Analysis summary

🔎 Location Search

Global location search using Geopy

Automatically fetches coordinates for climate analysis

🧠 Technologies Used
Frontend

HTML

CSS

JavaScript

Chart.js

Globe.gl (3D Earth)

Backend

Python

Flask

Xarray

Pandas

Geopy

ReportLab

Database

SQLite

📂 Project Structure
pyclima-explorer/
│
├── app.py
├── users.db
├── requirements.txt
│
├── templates/
│     └── index.html
│
└── static/
      ├── style.css
      └── script.js
⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/yourusername/pyclimaexplorer.git
cd pyclimaexplorer
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Application
python app.py
4️⃣ Open the App

Go to:

http://127.0.0.1:5000
🖥️ How It Works

User creates an account or logs in.

User enters a location name.

The system converts the location to coordinates.

Climate data is extracted from the dataset.

The dashboard displays climate trend charts.

Users can export a PDF climate analysis report.

📊 Example Use Case

A user wants to analyze the climate of Varanasi.

Login to PyClimaExplorer

Enter Varanasi in the search field

View the temperature trend graph

Download a Climate Report PDF

🔮 Future Improvements

🌍 Interactive global heatmaps

📊 Climate comparison between years

🤖 AI-based climate prediction

🛰 Integration with NASA climate datasets

📈 Animated climate change visualization

🏆 Hackathon Use

PyClimaExplorer is designed for data science, climate research, and hackathon demonstrations, enabling quick insights into complex climate datasets through an intuitive interface.
