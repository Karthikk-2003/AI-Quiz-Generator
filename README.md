# AI Quiz Generator (Offline)

This project is an offline AI-powered quiz generator application that leverages local Large Language Models (LLMs) using Ollama. The user can input a topic and generate multiple-choice quizzes, take the quiz interactively, and download it as a PDF. The application runs fully offline after initial setup.

## Features

- Generate topic-based quizzes using local LLMs (Mistral)
- Interactive quiz-taking interface
- Download quiz content as a structured PDF
- Clean user interface built with Gradio
- Runs entirely offline (once models are downloaded)

## Technologies Used

- Python 3.10+
- Ollama (Local LLM management)
- Mistral model (via Ollama)
- Gradio (Frontend UI)
- ReportLab (PDF export)
- Git and GitHub (Version Control)

## How to Set Up and Run the Project

### 1. Prerequisites

Ensure the following are installed on your system:

- [Python 3.10 or 3.11](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Ollama](https://ollama.com) (for running local LLMs like Mistral)

> **Note:** Avoid Python 3.13 as some packages may have compatibility issues.

---

### 2. Clone the Repository

```bash
git clone https://github.com/Karthikk-2003/AI-Quiz-Generator.git
cd AI-Quiz-Generator
```
### 3. Set Up Virtual Environment
Create a virtual environment:
```bash
python -m venv venv
```
###Activate the environment:

On Windows:
```bash
.\venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```
### 4. Install Python Dependencies
If requirements.txt is available:
```bash
pip install -r requirements.txt
```
Or install manually:
```bash
pip install gradio requests reportlab
```
### 5. Download the Mistral Model with Ollama
Make sure Ollama is installed and running, then run:
```bash
ollama pull mistral
```
This will download the Mistral model locally.

### Run the Mistral Model Manually
open a new terminal and run this command
```bash
ollama run mistral
```
After running the above command, wait for the Ollama model to initialize. Once it's ready, you will see a prompt in the terminal to enter your input.

### 6. Run the Application
Start the application with:
```bash
python app_ui.py
```
Once running, open your browser and go to:

http://127.0.0.1:7860

### 7. Stop the Application
To stop the app:

Press Ctrl + C in the terminal

To stop the Ollama model:
```bash
ollama stop
```
### Notes:
This project is fully offline once the model is downloaded.

No API keys or external calls are used.

Ideal for educational use, demonstrations, or secure offline systems.

