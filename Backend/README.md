# Baymax

This project is a chatbot designed to provide information about various drugs. It uses the Mistral API with the open-mistral-7b model, fine-tuned on a dataset containing comprehensive drug-related information. Users can interact with the chatbot to obtain detailed and accurate drug information.

## Table of Contents
        Installation
        Usage
        Project Structure
        Environment Variables
        API Endpoints
        License

### Installation

To run this project locally, follow these steps:
1. Clone the repository:

git clone https://github.com/your-username/drug-information-chatbot.git

2. Navigate to the project directory:

cd drug-information-chatbot

3. Install the required dependencies:

pip install -r requirements.txt
4. Set up the environment variables by creating a .env file in the app directory. Refer to the Environment Variables section for details.



### Usage
To start the application, run the following command in the app directory:

uvicorn main:app --reload

This will start the FastAPI server on http://127.0.0.1:8000, where you can access the chatbot API.

### Project Structure
Backend/
│
└───app/
    │
    ├── .env
    ├── model_inference.py
    ├── schemas.py
    ├── main.py

#### Description of Each File

.env: Contains environment variables needed for the application, such as the Mistral API key.
model_inference.py: Handles the logic for running model inference. This includes loading the model and processing user inputs to generate responses.
schemas.py: Defines the data models used in the application, ensuring that data exchanged between the client and server is validated and structured correctly.
main.py: The main application file that sets up the FastAPI server and defines the endpoints for interacting with the chatbot.

### API Endpoints
The application exposes the following API endpoints:
GET /: A welcome message indicating that the API is running.
POST /chat: Endpoint will send a message to the chatbot and receive a response. Expect a JSON payload with the user message.

Example Request
curl -X POST "http://127.0.0.1:8000/chat" -H "Content-Type: application/json" -d '{"message": "Tell me about Aspirin"}'

License
This project is licensed under the MIT License. See the LICENSE file for details.
