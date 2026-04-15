# csp-sudoku-backtracking

> A high-performance Sudoku Solver using Constraint Satisfaction Problem (CSP) techniques including Backtracking, Forward Checking, and AC-3 Algorithm.

---



# 🧩 Sudoku Solver using CSP (AI Project)

> 🚀 A powerful and efficient Sudoku solver built using **Constraint Satisfaction Problem (CSP)** techniques.

---

## 📌 Overview

This project implements an intelligent Sudoku solver using:
- 🔁 Backtracking Search
- ⚡ Forward Checking
- 🔗 AC-3 Algorithm (Arc Consistency)

The solver efficiently handles puzzles of varying difficulty by reducing the search space using constraint propagation.

---

## 🎯 Features

✔ Solves Easy, Medium, Hard, and Very Hard Sudoku puzzles  
✔ Uses advanced AI techniques (CSP)  
✔ Optimized with MRV (Minimum Remaining Values heuristic)  
✔ Tracks:
- Number of Backtracking Calls
- Number of Failures  

---

## 📂 Project Structure

```

Sudoku-CSP-Solver/
│── solver.py
│── easy.txt
│── medium.txt
│── hard.txt
│── veryhard.txt
│── README.md

```

---

## 📥 Input Format

Each Sudoku board is provided as a `.txt` file:

- Exactly **9 lines**
- Each line contains **9 digits (0–9)**
- `0` represents empty cells

### Example:
```

004030050
609400000
005100489
000060930
300807002
026040000
453009600
000004705
090050200

````

---

## ▶️ How to Run

```bash
python solver.py
````

---

## 📊 Output

For each Sudoku board, the program displays:

* ✅ Solved Sudoku Grid
* 🔁 Backtrack Calls
* ❌ Backtrack Failures

---

## 🧠 Algorithms Explained

### 🔁 Backtracking

Systematically tries possible values until a solution is found.

### ⚡ Forward Checking

Eliminates invalid values early to avoid unnecessary computation.

### 🔗 AC-3 Algorithm

Maintains arc consistency across variables to reduce domains before search.

### 📉 MRV Heuristic

Selects the variable with the fewest legal values to improve efficiency.

---

## 📈 Performance Insights

| Difficulty | Behavior                                       |
| ---------- | ---------------------------------------------- |
| Easy       | Minimal backtracking                           |
| Medium     | Moderate search required                       |
| Hard       | Increased backtracking                         |
| Very Hard  | Deep recursion and complex constraint handling |

---

## 💡 Key Insight

> Combining **AC-3 + Forward Checking + MRV** dramatically reduces the search space compared to basic backtracking.

---

## 🛠️ Technologies Used

* Python 🐍
* CSP (Artificial Intelligence)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

