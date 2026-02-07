# World Capitals Quiz Generator

A Python script that generates multiple-choice quizzes about world capitals.  
The program can export quizzes and answer keys in TXT, PDF, or DOCX format.

---

## Features

- Generates multiple quizzes automatically  
- Randomized questions and answer options  
- Creates a separate answer key for each quiz  
- User can choose:
  - Output folder  
  - Number of quizzes  
  - Number of questions  
  - File format (TXT, PDF, DOCX)  
- Files are timestamped to avoid overwriting  

---

## Requirements

Python 3.9+

Install dependencies:

    python -m pip install -r requirements.txt

Create a file named requirements.txt with:

    python-docx
    reportlab

---

## How to Run

From the project folder:

    python capitals_quiz_generator.py

Then follow the prompts:
- Choose output folder (or press Enter for default)
- Choose file format
- Enter number of quizzes
- Enter number of questions

---

## Output Example

The script generates files like:

    capital_quiz_20260207_101530_1.pdf
    capital_quiz_20260207_101530_1_answers.pdf

---

## Project Structure

    capitals_quiz_generator.py
    requirements.txt
    README.md

---

## Technologies Used

- Python
- pathlib
- random
- python-docx
- reportlab

---

## Purpose

This project was built to practice:
- File handling
- Data structures
- Randomization
- Generating formatted documents
- Building interactive command-line tools
