# 🚀 DevMate CLI - AI Coding Assistant

DevMate is a CLI-based AI coding assistant built using multi-agent architecture.
It uses CrewAI to simulate a team of developers (Planner, Coder, Debugger) working together to complete coding tasks.

---

## ✨ Features

* 🧠 Multi-agent system (Planner → Coder → Debugger)
* 💻 CLI-based interaction
* ⚡ Supports multiple LLM providers (Groq / OpenRouter)
* 🔧 Extensible architecture
* 🛠️ Real-world developer workflow simulation

---

## 🏗️ Project Structure

```
devmate-cli/
│
├── devmate/
│   ├── agents/
│   ├── core/
│   ├── config/
│   ├── cli.py
│
├── setup.py
├── .env
├── README.md
```

---

## 🚀 Installation

### 1. Clone repo

```bash
git clone https://github.com/<your-username>/devmate-cli.git
cd devmate-cli
```

---

### 2. Create virtual environment

```bash
py -3.11 -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

## ⚡ Usage

```bash
python -m devmate.cli "build express server"
```

---

## 🧠 How it Works

1. CLI takes user input
2. Executor creates tasks
3. Agents process tasks:

   * Planner → breaks problem
   * Coder → writes code
   * Debugger → fixes issues
4. Final output is returned

---

## 🔮 Future Improvements

* Auto project generation (files & folders)
* Interactive chat mode
* Memory & context awareness
* Web UI dashboard
* Multi-model fallback system

---

## 🤝 Contributing

Feel free to fork and improve DevMate!

---

## 📜 License

MIT License
