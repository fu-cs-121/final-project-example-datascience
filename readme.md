# Student Lifestyle Analysis

A program to analyze relationships between student activities and academic performance using a dataset of 2,000 student records.

## Folder Structure

## Project Structure

```
project_folder/
    ├── core.py          # Core business logic
    ├── test.py          # Tests for core functionality
    ├── main.py          # Command-line interface
    └── readme.md        # This file
```

## Program Design

The program follows a simple design with separated business logic and interface:

- `core.py`: Contains `StudentAnalyzer` class that handles:

  - Loading and validating data
  - Basic statistics (averages, totals)
  - Study hours impact analysis
  - Stress level impact analysis
  - Top performer analysis

- `test.py`: Tests core functionality

  - Creates test data
  - Verifies all analyzer methods
  - Checks data types and value ranges

- `main.py`: Command-line interface for viewing analysis results

## Dataset

The program uses [`student_lifestyle_dataset.csv`](./student_lifestyle_dataset.csv) which contains:

- 2,000 student records
- 7 columns
- Source: [Kaggle Student Lifestyle Dataset](https://www.kaggle.com/datasets/steve1215rogg/student-lifestyle-dataset)

## Setup

No external packages required - uses only Python standard library

## Running the Program

Run tests:

```bash
python test.py
```

Run analysis interface:

```bash
python main.py
```
