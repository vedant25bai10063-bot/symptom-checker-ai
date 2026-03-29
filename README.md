### Symptom Checker AI ###

## Overview ##
Symptom Checker AI is a Python-based project that predicts possible diseases based on symptoms selected by the Patient(User).  
It uses a dataset-driven approach to compare symptoms and provide the relevant disease predictions with risk levels.

## Features ##
-  Takes patient details (Name, Age, Sex)
-  Interactive symptom selection system
-  Calculates match percentage for diseases
-  Classifies risk level (Low / Medium / High)
-  Uses real dataset (`Training.csv`)
-  Intelligent matching logic

## Tech Stack ##
- *Python*
- *Pandas*
- *Dataset-based logic*

## Project Structure ##
- AI&ML.py → Main program
- Training.csv → Dataset
- README.md → Project documentation
- Requirements → Project Report 

## How It Works ##
1. User enters personal details  
2. System displays a list of symptoms  
3. User selects symptoms by number  
4. Program compares input with dataset  
5. Outputs:
   - Most likely disease  
   - Other possible diseases  
   - Match percentage  
   - Risk level

## How to Run the Project ##
 1. Install Dependencies - python AI&ML.py,Training.csv
    pip install pandas

## Sample Output ## 
    ========= RESULT =========
Name: XYZ
Age: 19
Sex: Male

Most Likely Disease: Flu

Other Possible Diseases:
Flu -> Match: 80% | Risk: High
Common Cold -> Match: 60% | Risk: Medium
Allergy -> Match: 40% | Risk: Low

## Disclaimer ##
This project is for educational purposes only.
It is not a medical diagnosis tool. Always consult a doctor for real medical advice.

## Author ##
Vedant Tomar
B-Tech Student (AI & ML)
