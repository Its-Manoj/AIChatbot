# AI Chatbot Project

This is a web-based AI Chatbot built using Flask and integrated with **Google GenAI API**. The chatbot allows users to interact with an AI model in a simple and responsive web interface.

---

## Project Structure

your_project/
├─ app.py # Main Flask application
├─ templates/
│ └─ index.html # HTML template for the chatbot UI
└─ static/
├─ css/ # CSS files
│ └─ style.css
├─ js/ # JavaScript files
└─ assets/ # Images and other static assets
└─ bot.webp # Chatbot logo



---

## Features

- Interactive chatbot interface.
- Custom chatbot logo.
- Responsive design using CSS.
- Powered by Google GenAI API for generating AI responses.
- Separate folders for CSS, JS, and images for better project organization.

---

## Installation

1. Clone the repository:


git clone https://github.com/yourusername/your_project.git
cd your_project
Create and activate a virtual environment:


python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Install dependencies:


pip install -r requirements.txt
Make sure you have Flask and requests installed. You can add other dependencies if needed.

Setup Google GenAI API
Sign up and get your Google GenAI API key.

Add your API key in the project (usually in app.py or a .env file):


GENAI_API_KEY = "your_google_genai_api_key"
Make sure to keep your API key private.

Running the Project
Run the Flask app:


python app.py
Open your browser and navigate to:


http://127.0.0.1:5000
You should see your chatbot interface and be able to start chatting with the AI.

Customization
Logo: Replace bot.webp in static/assets/ with your own logo.

Styles: Edit style.css in static/css/ to change the UI appearance.

Scripts: Modify js/ files for any frontend interactions or enhancements.

Screenshots

License
This project is licensed under the MIT License.

Acknowledgements
Flask
Google GenAI API

---

If you want, I can also make a **shorter, beginner-friendly version** of this README that’s perfect for GitHub so it’s quick to understand and visually appealing.  

Do you want me to do that?
