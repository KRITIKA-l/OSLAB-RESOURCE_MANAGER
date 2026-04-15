# Smart OS Resource Manager

Smart OS Resource Manager turns classic Operating System concepts into an interactive simulation playground.

Instead of reading formulas in isolation, you can run the algorithms, watch behavior change with inputs, and compare outcomes instantly.

It includes:
- A browser frontend in index.html
- A Python implementation of all algorithms in ResourceManager.py

## What Makes It Interesting

- Three core OS domains in one project: CPU scheduling, memory management, and deadlock avoidance
- Side-by-side learning style: theory + immediate visual/step output
- Quick experimentation with custom inputs and one-click sample datasets
- Great for demos, viva explanations, and concept revision

## Feature Highlights

### 1) CPU Scheduling Simulator
Run six scheduling strategies and inspect process-level metrics:
- FCFS (First-Come, First-Served)
- SJF (Shortest Job First, Non-Preemptive)
- SRTF (Shortest Remaining Time First, Preemptive)
- Priority Scheduling (Non-Preemptive)
- Priority Scheduling (Preemptive)
- Round Robin (Preemptive)

Outputs include:
- Completion Time (CT), Turnaround Time (TAT), Waiting Time (WT)
- Average WT and average TAT
- Gantt-style timeline visualization in the HTML frontend

### 2) Memory Management Simulator
Simulate page replacement and observe frame behavior at each step:
- FIFO (First-In, First-Out)
- LRU (Least Recently Used)

Outputs include:
- HIT or MISS for each page request
- Frame content after every step
- Total page faults

### 3) Deadlock Avoidance (Banker's Algorithm)
Evaluate whether the system is safe for a given allocation state.

Outputs include:
- SAFE or DEADLOCK status
- Safe sequence (if one exists)
- Need matrix
- Available resources at the end of simulation

### 4) Interactive HTML Frontend
Modern browser-based interface built for simulation-first usage.

Frontend capabilities:
- Dedicated tabs for CPU, Memory, and Deadlock modules
- Input validation with clear error feedback
- Sample input buttons for quick testing
- Responsive design for desktop and mobile
- Visual timeline for scheduling results

## Project Structure

- index.html: Browser frontend (HTML + CSS + JavaScript)
- ResourceManager.py: Core algorithm logic and CLI-based interaction

## Quick Start

### Option A: Use the browser frontend (recommended)
1. Open index.html in your browser.
2. Select a module tab.
3. Enter input values or load sample data.
4. Run and analyze the output.

### Option B: Use the Python CLI
1. Open a terminal in the project folder.
2. Run:

```bash
python ResourceManager.py
```

3. Follow the interactive menu.

## Ideal Use Cases

- OS lab mini-project submissions
- Classroom demonstrations
- Viva and interview preparation
- Fast comparison of algorithm behavior under different workloads
