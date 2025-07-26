# AI Quiz Generator (Offline)

This is an AI-powered quiz generator app built in Python with a clean GUI using Gradio. It allows users to input any topic and generate multiple-choice quizzes using **local large language models (LLMs)** via **Ollama**. Users can take quizzes interactively, get automatic evaluation with scores, and export the quiz as a styled PDF.

> ⚡ Fully offline, no API keys, no internet needed once models are downloaded.

---

## ✨ Features

* ✅ Generate quizzes using local LLMs (e.g., Mistral, Gemma)
* ✅ Choose between multiple supported models via dropdown
* ✅ Fully interactive quiz-taking interface with scoring
* ✅ Export quizzes to PDF (includes selected answers and correct answers)
* ✅ Clean UI built with Gradio
* ✅ Modular Python code structure
* ✅ Works fully offline after initial setup

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Ollama** – For managing and running local LLMs (Mistral, Gemma, etc.)
* **Gradio** – For building the interactive UI
* **ReportLab** – For exporting styled PDF files
* **Git + GitHub** – For version control and collaboration

---

## 🚀 How to Run the Project

### 1. Prerequisites

Install the following tools:

* [Python 3.10+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads)
* [Ollama](https://ollama.com) – required to run local models like Mistral or Gemma

> ⚠️ Do **not** use Python 3.13 – some libraries may not be compatible.

---

### 2. Clone the Repository

```bash
git clone https://github.com/Karthikk-2003/AI-Quiz-Generator.git
cd AI-Quiz-Generator
```

---

### 3. Set Up Virtual Environment

```bash
python -m venv venv
```

Activate it:

* On **Windows**:

  ```bash
  .\venv\Scripts\activate
  ```
* On **macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

---

### 4. Install Python Dependencies

If a `requirements.txt` is provided:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install gradio requests reportlab
```

---

### 5. Download a Local Model with Ollama

Choose any supported model:

```bash
ollama pull mistral
ollama pull gemma:2b-instruct
```

You can run either:

```bash
ollama run mistral
```

or

```bash
ollama run gemma:2b-instruct
```

Wait for the model to initialize and be ready to receive input.

---

### 6. Run the Application

In your project folder, run:

```bash
python app_ui.py
```

Open your browser and visit:

```
http://127.0.0.1:7860
```

You can now:

* Enter a topic
* Choose a model
* Generate and take the quiz
* Export the results as PDF

---

### 7. Stop the Application

To stop the Gradio app:

```
Ctrl + C
```

To stop the LLM:

```bash
ollama stop
```

---

## 📆 Project Structure

```
├── app_ui.py           # Main GUI application
├── quiz_logic.py       # Prompt building and model calling logic
├── quiz_generator.py   # Quiz generation flow (retry, scoring)
├── pdf_exporter.py     # PDF exporting logic
├── assets/             # Images or media files (if needed)
```

---

## ✅ Notes

* No OpenAI or paid API needed.
* No internet required after models are downloaded.
* Perfect for offline, educational, or privacy-focused use cases.

---
