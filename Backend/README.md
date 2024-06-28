
---

# Baymax

This project is a chatbot designed to provide information about various drugs. It uses the Mistral API with the open-mistral-7b model, fine-tuned on a dataset containing comprehensive drug-related information. Users can interact with the chatbot to obtain detailed and accurate drug information.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/drug-information-chatbot.git
   ```

2. Navigate to the project directory:
   ```bash
   cd drug-information-chatbot
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables by creating a `.env` file in the `app` directory. Refer to the [Environment Variables](#environment-variables) section for details.

## Usage

To start the application, run the following command in the `app` directory:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server on [http://127.0.0.1:8000](http://127.0.0.1:8000), where you can access the chatbot API.

## Project Structure

```
Backend/
└───app/
    ├── .env
    ├── model_inference.py
    ├── schemas.py
    ├── main.py
```

### Description of Each File

- **.env**: Contains environment variables needed for the application, such as the Mistral API key.
- **model_inference.py**: Handles the logic for running model inference. This includes loading the model and processing user inputs to generate responses.
- **schemas.py**: Defines the data models used in the application, ensuring that data exchanged between the client and server is validated and structured correctly.
- **main.py**: The main application file that sets up the FastAPI server and defines the endpoints for interacting with the chatbot.

## Environment Variables

Create a `.env` file in the `app` directory and add the following variables:

```
MISTRAL_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Mistral API key.

## API Endpoints

The application exposes the following API endpoints:

- `GET /`: A welcome message indicating that the API is running.
- `POST /chat`: Endpoint to send a message to the chatbot and receive a response. Expects a JSON payload with the user message.

### Example Request

```bash
curl -X POST "http://127.0.0.1:8000/chat" -H "Content-Type: application/json" -d '{"message": "Tell me about Aspirin"}'
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This format provides a clear and organized structure for your README file, making it easy for users to understand and follow the instructions.
