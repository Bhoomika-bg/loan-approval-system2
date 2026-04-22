# 🏦 Loan Approval System using AO* Algorithm

## 📌 Overview

This project implements a **Loan Approval System using the AO* (AND-OR Search) algorithm**.
Unlike traditional machine learning approaches, this system uses **AI search techniques** to make decisions based on a structured AND-OR graph and cost evaluation.

---

## 🚀 Key Features

* Implements **AO* search algorithm**
* Uses **AND-OR graph structure**
* Cost-based decision making (risk evaluation)
* Transparent and explainable logic (no black-box ML)
* Interactive UI using Streamlit

---

## 🧠 Algorithm Used: AO*

AO* is an informed search algorithm used for solving problems represented as **AND-OR graphs**.

* **AND nodes** → All conditions must be satisfied
* **OR nodes** → Choose the optimal decision path
* The algorithm selects the **minimum cost solution**

---

## 🏗️ System Design

### AND Conditions:

* Income Check
* Credit Score Check
* DTI (Debt-to-Income Ratio)

### OR Decisions:

* Approve
* Review
* Reject

---

## ⚙️ How It Works

1. User inputs:

   * Income
   * Credit Score
   * DTI Ratio
   * Existing Loans
   * Loan Amount

2. System computes:

   * Cost (risk score)
   * Heuristic (estimated cost)

3. AO* algorithm:

   * Evaluates AND-OR graph
   * Selects optimal decision (minimum cost path)

---

## 📁 Project Structure

```
loan-app/
│
├── app.py          # Streamlit UI
├── ao_star.py      # AO* algorithm logic
├── graph.py        # Node (AND-OR graph structure)
├── utils.py        # Cost + heuristic functions
├── requirements.txt
```

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📊 Output

* Decision: Approve / Review / Reject
* Cost (risk score)
* Explanation of decision process

---

## ❗ Note

This project is implemented using **AO*** for academic purposes.
It demonstrates **AI search techniques instead of machine learning models**.

---

## 👩‍💻 Author

BHOOMIKA BG
JAHNAVI
MADHUSHREE
LIKITHA
