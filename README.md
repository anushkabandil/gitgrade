# GitGrade 🚀  
### Intelligent GitHub Repository Evaluation & Developer Profiling

GitGrade is an intelligent system that analyzes a public GitHub repository and converts it into a **dimension-wise score, recruiter-style evaluation, and a personalized learning roadmap**.

Unlike traditional code analyzers, GitGrade focuses on **engineering quality, clarity, and real-world readiness**.

---

## 📌 Problem Statement

A GitHub repository is a developer’s strongest proof of work — yet:
- Students don’t know how good their repositories really are
- Recruiters struggle to assess repo quality quickly
- There is no clear feedback or improvement roadmap

**GitGrade bridges this gap.**

---

## 💡 Solution Overview

GitGrade takes a **GitHub repository URL** as input and produces:

- 📊 Dimension-wise scores (code quality, testing, docs, etc.)
- 🧠 Recruiter confidence & repo maturity level
- 🧾 Recruiter + student perspective summaries
- 🎯 Resume-ready skill extraction
- 🛣 Personalized improvement roadmap with reasoning

---

## ✨ Key Features (WHAT MAKES IT WIN)

### ⭐ Dimension-wise Score Breakdown
Transparent scoring across:
- Code Quality
- Documentation
- Testing
- Project Structure
- Git Practices

### 🏷 Repository Maturity Tag
Classifies repos as:
- Beginner
- Intermediate
- Industry-Ready

### 🧠 Recruiter Confidence Meter
Indicates how confidently a recruiter would shortlist the repo:
- High / Medium / Low

### 👥 Dual Perspective Summaries
- **Recruiter View:** hiring-focused insights
- **Student View:** growth-oriented feedback

### 📄 Resume-Ready Skill Extraction
Automatically detects skills like:
- Programming languages
- Git usage
- Documentation practices

### 🛣 Explainable Personalized Roadmap
Not just *what* to improve — but *why* those steps matter.

---

## ⚙️ How It Works (System Architecture)
GitHub URL
↓
Data Fetcher (GitHub API)
↓
Repository Analyzer
↓
Scoring Engine
↓
Summaries + Skills + Roadmap Generator
↓
Readable, Recruiter-Ready Output


---

## 🛠 Tech Stack

- Python
- GitHub REST API
- Modular rule-based evaluation
- CLI-based interface

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/anushkabandil/gitgrade.git
cd gitgrade
python main.py

When prompted, paste any public GitHub repository URL, for example:
https://github.com/octocat/Hello-World
```

---

## 🧪 Evaluation Philosophy

GitGrade does not aim to judge developers solely by raw metrics.  
Instead, it focuses on **engineering signals** that recruiters and mentors actually care about — such as structure, clarity, consistency, and growth potential.
