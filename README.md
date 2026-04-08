# 🚀 High Performance Automation Workflow System

A scalable and high-performance automation workflow system built using FastAPI and Python asyncio. This project executes tasks asynchronously, supports parallel workflows, and provides real-time monitoring through a live dashboard.

---

## 🔥 Features

- ⚡ Async & Parallel Task Execution  
- 🧠 Strategy Pattern for flexible task processing  
- 🏭 Factory Pattern for dynamic strategy selection  
- 💾 Caching system to optimize repeated tasks  
- 📊 Real-time Monitoring Dashboard  
- 📈 Metrics tracking (success, failure, execution time)  
- 🗄 SQLite Database integration  
- 🔄 REST API for task management  

---

## 🏗️ System Architecture

The system is designed with modular and scalable components:

- Workflow Engine → Executes tasks asynchronously  
- Task Manager → Handles task creation & status updates  
- Strategy Layer → Defines task execution logic  
- Factory → Selects appropriate strategy dynamically  
- Monitoring Service → Tracks performance metrics  
- Dashboard UI → Displays live system metrics  

---

## 🛠 Tech Stack

- Backend: FastAPI, Python  
- Async Processing: asyncio  
- Database: SQLite  
- Frontend: HTML, CSS, JavaScript  
- Server: Uvicorn  

---

## 📁 Project Structure

```
high_performance_automation/
│
├── src/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── database/
│   └── utils/
│
├── dashboard/
│   └── index.html
│
├── config/
│   └── settings.py
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/automation-workflow-system.git
cd automation-workflow-system
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Start Backend Server

```bash
uvicorn src.api.app:app --reload
```

### 4️⃣ Start Dashboard

```bash
cd dashboard
python -m http.server 5500
```

### 5️⃣ Open in Browser

Dashboard: http://127.0.0.1:5500  
API Docs: http://127.0.0.1:8000/docs  

---

## 📡 API Endpoints

- GET `/` → Health check  
- POST `/create-task` → Create a new task  
- GET `/run-workflow` → Execute pending tasks  
- GET `/tasks` → Get pending tasks  
- GET `/metrics` → Get performance metrics  

---

## 📊 Dashboard Features

- Displays total tasks, successful tasks, failed tasks, and average execution time  
- Shows real-time task execution history  
- Auto-refresh every few seconds  

---

## ⚡ Example Workflow

1. Create task via API  
2. Run workflow  
3. Tasks execute asynchronously  
4. Metrics update in real-time  
5. Dashboard reflects results  

---

## 🚀 Key Highlights

- Designed for high performance and scalability  
- Implements modern backend architecture  
- Uses design patterns (Strategy + Factory)  
- Supports real-time monitoring  
- Demonstrates async programming and parallel execution  

---

## 📌 Future Improvements

- Add authentication & user management  
- Deploy using Docker  
- Add advanced analytics & charts  
- Integrate message queues (RabbitMQ/Kafka)  

---

## 👨‍💻 Author

Likhitha  

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
