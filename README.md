# Smart OS Resource Manager

Smart OS Resource Manager is an OS mini-project that combines core operating-system simulations into one place.

It includes:
- A browser frontend in index.html
- A Python implementation of all algorithms in ResourceManager.py

## Feature Highlights

### 1) CPU Scheduling Simulator
Supports six scheduling strategies with per-process results and timeline output:
- FCFS (First-Come, First-Served)
- SJF (Shortest Job First, Non-Preemptive)
- SRTF (Shortest Remaining Time First, Preemptive)
- Priority Scheduling (Non-Preemptive)
- Priority Scheduling (Preemptive)
- Round Robin (Preemptive)

What you get:
- Completion Time (CT), Turnaround Time (TAT), Waiting Time (WT)
- Average WT and average TAT
- Gantt-style timeline visualization in the HTML frontend

### 2) Memory Management Simulator
Implements page-replacement behavior with step-by-step state tracking:
- FIFO (First-In, First-Out)
- LRU (Least Recently Used)

What you get:
- HIT/MISS for every page reference
- Frame state after each step
- Total page faults summary

### 3) Deadlock Avoidance (Banker's Algorithm)
Performs safe-state analysis using process-resource matrices.

What you get:
- SAFE or DEADLOCK state detection
- Safe sequence (if available)
- Need matrix generation
- Available resource vector after simulation

### 4) Interactive HTML Frontend
The browser UI is designed for direct experimentation and demos.

Frontend capabilities:
- Separate tabs for CPU, Memory, and Deadlock modules
- Input validation with clear error messages
- One-click sample data loading
- Responsive layout for desktop and mobile
- Visual Gantt timeline for CPU scheduling output

## Project Structure

- index.html: Browser-based frontend (HTML + CSS + JavaScript)
- ResourceManager.py: Python logic for scheduling, memory, and deadlock modules

## How To Run

### Option A: Run the browser frontend
1. Open index.html in your browser.
2. Choose a module tab and enter inputs.
3. Click the run button for that module.

### Option B: Run the Python CLI
1. Open a terminal in the project folder.
2. Run:

```bash
python ResourceManager.py
```

3. Follow the menu prompts.

## Why This Project Is Useful

- Demonstrates multiple classic OS topics in one mini-project
- Helps compare algorithms with the same input sets
- Useful for viva, lab demonstrations, and quick concept revision
- Shows both algorithm design (Python) and user-facing interaction (HTML frontend)
