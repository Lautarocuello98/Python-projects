# World Capitals Quiz Generator

A Python script that automatically generates multiple-choice quizzes about world capitals and their answer keys.  
Quizzes can be exported as **TXT, PDF, or DOCX**, ready to print or distribute.

---

## Features

- Generates multiple quizzes automatically  
- Randomizes both questions and answer options  
- Creates a separate answer key for each quiz  
- User can choose:
  - Output folder
  - Number of quizzes
  - Number of questions
  - File format (TXT, PDF, DOCX)
- Files are timestamped to prevent overwriting  

---

## Requirements

Python 3.9+

Install dependencies:

python -m pip install -r requirements.txt

requirements.txt:

python-docx  
reportlab  

---

## How to Run

From the project folder:

python capitals_quiz_generator.py

Then follow the prompts to choose:
- Output folder  
- File format  
- Number of quizzes  
- Number of questions  

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

Python  
pathlib  
random  
python-docx  
reportlab  

---

## Purpose

This project demonstrates how to:

- Automate document generation
- Work with structured data
- Randomize content programmatically
- Build interactive command-line tools
- Generate formatted documents in multiple formats

