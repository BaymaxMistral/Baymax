
---

# Baymax

This project is a chatbot designed to provide information about various drugs. It uses the Mistral API with the open-mistral-7b model, fine-tuned on a dataset containing comprehensive drug-related information. Users can interact with the chatbot to obtain detailed and accurate drug information.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Sample Quesiton](#sample-questions)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/BaymaxMistral/Baymax.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Backend/app
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables by creating a `.env` file in the `app` directory.

## Usage

To start the application, run the following command in the `app` directory:

```bash
python main.py
```

This will start the FastAPI server on [http://localhost:8000/docs](http://localhost:8000/docs), where you can access the chatbot API.

## Project Structure

```
Backend/
└───app/
    ├── .env
    ├── model_inference.py
    ├── schemas.py
    ├── main.py
    ├── requirements.txt

```

### Description of Each File

- **.env**: Contains environment variables needed for the application, such as the Mistral API key.
- **model_inference.py**: Handles the logic for running model inference. This includes loading the model and processing user inputs to generate responses.
- **schemas.py**: Defines the data models used in the application, ensuring that data exchanged between the client and server is validated and structured correctly.
- **main.py**: The main application file that sets up the FastAPI server and defines the endpoints for interacting with the chatbot.


## Environment Variables

The application requires specific environment variables to function correctly. Create a `.env` file in the app directory and add the following:

```bash
MISTRAL_API_KEY=your_api_key_here
```

## API Endpoints

The application exposes the following API endpoints:

- `GET /`: A welcome message indicating that the API is running.
- `POST /get_response`: Endpoint to send a message to the chatbot and receive a response. Expects a JSON payload with the user message.

## Sample Questions

- `Question 1`: 
- `Question 2`:
- `Question 3`: 
- `Question 4`:
- `Question 5`: 


---
