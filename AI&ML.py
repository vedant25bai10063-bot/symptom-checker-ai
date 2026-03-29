##### MEDICAL SYMPTOMS CHECKER #####

# import module #
import pandas as pd
import time

### Dataset ###
data = pd.read_csv("Training.csv")

# Removing the extra column in the dataset #
if "Unnamed: 133" in data.columns:
    data = data.drop("Unnamed: 133", axis=1)

# Disease column #
disease_col = "prognosis"

### Symptoms ###
symptom = [col for col in data.columns if col != disease_col]

print("=========  SYMPTOM CHECKER  =========\n")

## Patient Details ##
name = input("Enter patient's name: ")
age = input("Enter patient's age: ")

print("\nEnter patient's sex:")
print("1. Male")
print("2. Female")
print("3. Other")

choice = input("Enter choice: ")

if choice == "1":
    sex = "Male"
elif choice == "2":
    sex = "Female"
else:
    sex = "Other"

print("\n Select Symptoms from the list below:\n")

# Showing the Symptoms from the list #
for i in range(len(symptom)):
    print(str(i+1) + ". " + symptom[i])

# Patient's Detail #
Input = input("\nEnter symptom according to number given (comma separated): ")

Selected_Symptoms = []
for num in Input.split(","):
    num = num.strip()
    if num.isdigit():
        index = int(num) - 1
        if 0 <= index < len(symptom):
            Selected_Symptoms.append(symptom[index])
results_dict = {}

# Coparing with dataset #
for i in range(len(data)):
    DiseaseName = data.iloc[i][disease_col]
    Count = 0

    for s in Selected_Symptoms:
        if data.iloc[i][s] == 1:
            Count += 1

    if len(Selected_Symptoms) > 0:
        Percent = int((Count / len(Selected_Symptoms)) * 100)

        if DiseaseName not in results_dict:
            results_dict[DiseaseName] = Percent
        else:
            if Percent > results_dict[DiseaseName]:
                results_dict[DiseaseName] = Percent


# Converting to list #
results = []
for d in results_dict:
    results.append((d, results_dict[d]))

# Sorting the Results #
results.sort(key=lambda x: x[1], reverse=True)

## Processing the time ##
print("\nProcessing the Patient's Data", end="")

for i in range(5):
    print(".", end="", flush=True)
    time.sleep(0.5)

print("\n")

print("\n=========  RESULT  =========")
print("Name: " + name)
print("Age: " + age)
print("Sex: " + sex)

if len(results) == 0:
    print("\nNo matching disease found. Please consult a doctor.")
else:
    print("\nPossible Disease affecting the Patient:", results[0][0])

    print("\nOther Possible Diseases:\n")

    for disease_name, percent in results[:5]:
        if percent > 75:
            risk = "High"
        elif percent > 45:
            risk = "Medium"
        else:
            risk = "Low"

        print(disease_name, "-> Match:", str(percent) + "%", "| Risk:", risk)

print("\nNote: This is just a basic program to guess the diseases by symptoms entered, not real medical advice.")