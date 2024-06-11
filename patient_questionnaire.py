import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox

# Create a class for the Patient Questionnaire application
class PatientQuestionnaireApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Questionnaire")
        # Create labels and entry widgets for the questionnaire fields
        self.create_widgets()
        # Data storage
        self.data = []
    def create_widgets(self):
        
        # # Personal Information
        # personal_label = tk.Label(self.root, text="Personal Information", font=("Arial", 12, "bold"))
        # personal_label.grid(row=0, columnspan=2, sticky=tk.W)
        # self.create_label_entry("Case ID", 1)
        # self.create_label_entry("Year of Discharge", 2)
        # self.create_label_entry("Age at Admission", 3, self.age_options())
        # self.create_label_entry("Gender", 4, self.gender_options())
        # self.create_label_entry("Race", 5, self.race_options())
        # self.create_label_entry("Ethnicity", 6, self.ethnicity_options())
        # self.create_label_entry("Marital Status", 7, self.marital_status_options())
        # self.create_label_entry("Education Level", 8, self.education_options())
        # self.create_label_entry("Employment Status at Admission", 9, self.employment_options())
        # self.create_label_entry("Pregnant at Admission", 10, self.yes_no_options())
        # self.create_label_entry("Veteran Status", 11, self.yes_no_options())
        # self.create_label_entry("Living Arrangements at Admission", 12, self.living_arrangements_options())
        # self.create_label_entry("Source of Income/Support", 13, self.income_support_options())
        # self.create_label_entry("Number of Arrests in Past 30 Days", 14, self.arrests_options())

        # # Treatment Information
        # treatment_label = tk.Label(self.root, text="Treatment Information", font=("Arial", 12, "bold"))
        # treatment_label.grid(row=15, columnspan=2, sticky=tk.W)
        # self.create_label_entry("Type of Treatment/Service Setting at Admission", 16, self.treatment_setting_options())
        # self.create_label_entry("Medication-assisted Opioid Therapy", 17, self.yes_no_options())
        # self.create_label_entry("Days Waiting to Enter Substance Use Treatment", 18, self.days_waiting_options())
        # self.create_label_entry("Reason for Discharge", 19, self.discharge_reason_options())
        # self.create_label_entry("Length of Stay in Treatment (days)", 20, self.length_of_stay_options())

        # # Substance Use Information
        # substance_label = tk.Label(self.root, text="Substance Use Information", font=("Arial", 12, "bold"))
        # substance_label.grid(row=21, columnspan=2, sticky=tk.W)
        # self.create_label_entry("Primary Substance Use at Admission", 22, self.substance_use_options())
        # self.create_label_entry("Route of Administration (Primary)", 23, self.route_of_admin_options())
        # self.create_label_entry("Frequency of Use at Admission (Primary)", 24, self.frequency_options())
        # self.create_label_entry("Age at First Use (Primary)", 25, self.age_first_use_options())

        # # Secondary Substance Use Information
        # secondary_label = tk.Label(self.root, text="Secondary Substance Use Information", font=("Arial", 12, "bold"))
        # secondary_label.grid(row=26, columnspan=2, sticky=tk.W)
        # self.create_label_entry("Secondary Substance Use at Admission", 27, self.substance_use_options())
        # self.create_label_entry("Route of Administration (Secondary)", 28, self.route_of_admin_options())

        # # Save button
        # save_button = tk.Button(self.root, text="Save", command=self.save_data)
        # save_button.grid(row=29, columnspan=2)

        # Personal Information
        self.create_label_entry("Case ID", 0)
        self.create_label_entry("Year of Discharge", 1)
        self.create_label_entry("Age at Admission", 2, self.age_options())
        self.create_label_entry("Gender", 3, self.gender_options())
        self.create_label_entry("Race", 4, self.race_options())
        self.create_label_entry("Ethnicity", 5, self.ethnicity_options())
        self.create_label_entry("Marital Status", 6, self.marital_status_options())
        self.create_label_entry("Education Level", 7, self.education_options())
        self.create_label_entry("Employment Status at Admission", 8, self.employment_options())
        self.create_label_entry("Pregnant at Admission", 9, self.yes_no_options())
        self.create_label_entry("Veteran Status", 10, self.yes_no_options())
        self.create_label_entry("Living Arrangements at Admission", 11, self.living_arrangements_options())
        self.create_label_entry("Primary Scource of Payment", 12, self.prime_pay_options())
        self.create_label_entry("Census Division", 13, self.Census_Division())
        # Treatment Information
        self.create_label_entry("Type of Treatment/Service Setting at Admission", 14, self.treatment_setting_options())
        self.create_label_entry("Meth Use?", 15, self.yes_no_options())
        self.create_label_entry("Days Waiting to Enter Substance Use Treatment", 16, self.days_waiting_options())
        self.create_label_entry("How often will you use Self-Help Programs after?", 17, self.FREQ_ATND_SELF_HELP_D())
        self.create_label_entry("Length of Stay in Treatment (days)", 18, self.length_of_stay_options())
        # Substance Use Information
        self.create_label_entry("Primary Substance Use at Admission", 19, self.substance_use_options())
        self.create_label_entry("Route of Administration (Primary)", 20, self.route_of_admin_options())
        self.create_label_entry("Frequency of Use at Admission (Primary)", 21, self.frequency_options())
        self.create_label_entry("Age at First Use (Primary)", 22, self.age_first_use_options())
        # Secondary Substance Use Information
        self.create_label_entry("Secondary Substance Use at Admission", 23, self.substance_use_options())
        self.create_label_entry("Route of Administration (Secondary)", 24, self.route_of_admin_options())
        # Save button
        save_button = tk.Button(self.root, text="Save", command=self.save_data)
        save_button.grid(row=25, columnspan=2)

        

    def create_label_entry(self, text, row, options=None):
        label = tk.Label(self.root, text=text)
        label.grid(row=row, column=0, sticky=tk.W)
        if options:
            entry = ttk.Combobox(self.root, values=options)
        else:
            entry = tk.Entry(self.root)
        entry.grid(row=row, column=1)
        setattr(self, f"entry_{row}", entry)
    def save_data(self):
        # Collect the data
        row_data = []
        for i in range(25): 
            entry = getattr(self, f"entry_{i}")
            row_data.append(entry.get())
        # Append to data list
        self.data.append(row_data)
        # Convert to DataFrame and save to CSV
        columns = [
            "CASEID", "DISYR", "AGE", "GENDER", "RACE", "ETHNIC",
            "MARSTAT", "EDUC", "EMPLOY", "PREG",
            "VET", "LIVARAG", "PRIMPAY",
            "DIVISION", "SERVICES",
            "METHUSE", "DAYWAIT",
            "FREQ_ATND_SELF_HELP_D", " LOS", "SUB1",
            "ROUTE1", "FREQ1", "FRSTUSE1",
            "SUB2", "ROUTE2"
        ]

        # columns = [
        #     "Case ID", "Year of Discharge", "Age at Admission", "Gender", "Race", "Ethnicity",
        #     "Marital Status", "Education Level", "Employment Status at Admission", "Pregnant at Admission",
        #     "Veteran Status", "Living Arrangements at Admission", "Source of Income/Support",
        #     "Number of Arrests in Past 30 Days", "Type of Treatment/Service Setting at Admission",
        #     "Medication-assisted Opioid Therapy", "Days Waiting to Enter Substance Use Treatment",
        #     "Reason for Discharge", "Length of Stay in Treatment (days)", "Primary Substance Use at Admission",
        #     "Route of Administration (Primary)", "Frequency of Use at Admission (Primary)", "Age at First Use (Primary)",
        #     "Secondary Substance Use at Admission", "Route of Administration (Secondary)"
        # ]

        df = pd.DataFrame(self.data, columns=columns)
        #df.to_csv("patient_questionnaire_data.csv", index=False)
        # Save by Case ID
        grouped_data = df.groupby("CASEID")
        for case_id, group_df in grouped_data:
            group_df.to_csv(f"./Patient_Questionnaire_Data/patient_questionnaire_data_{case_id}.csv", index=False)
        # Confirmation message
        messagebox.showinfo("Saved", "Data saved successfully")
    def age_options(self):
        return [
            "12–14 years", "15–17 years", "18–20 years", "21–24 years", "25–29 years", "30–34 years", "35–39 years",
            "40–44 years", "45–49 years", "50–54 years", "55–64 years", "65 years and older"
        ]
    def gender_options(self):
        return ["Male", "Female", "Other", "Prefer not to say"]
    def race_options(self):
        return [
            "Alaska Native (Aleut, Eskimo, Indian)", "American Indian (other than Alaska Native)", "Asian or Pacific Islander",
            "Black or African American", "White", "Asian", "Other single race", "Two or more races", "Native Hawaiian or Other Pacific Islander"
        ]
    def ethnicity_options(self):
        return [
            "Puerto Rican", "Mexican", "Cuban or other specific Hispanic", "Not of Hispanic or Latino origin", "Hispanic or Latino, specific origin not specified"
        ]
    def marital_status_options(self):
        return ["Never married", "Now married", "Separated", "Divorced, Widowed"]
    def education_options(self):
        return [
            "Less than one school grade, no schooling, nursery school, or kindergarten to Grade 8", "Grades 9 to 11", "Grade 12 (or GED)",
            "1-3 years of college, university, or vocational school", "4 years of college, university, BA/BS, some postgraduate study, or more"
        ]
    def employment_options(self):
        return ["Full-time", "Part-time", "Unemployed", "Not in labor force"]
    def yes_no_options(self):
        return ["Yes", "No"]
    def living_arrangements_options(self):
        return ["Homeless", "Dependent living", "Independent living"]
    def prime_pay_options(self):
        return ["Self-pay", "Private insurance", "Medicare", " Medicaid", "Other government payments", " No charge", "Other"]
    def Census_Division(self):
        return ["U.S. territories", "New England", "Middle Atlantic", "East North Central", "West North Central", "South Atlantic", "East South Central", "West South Central", "Mountain", "Pacific"]
    def treatment_setting_options(self):
        return [
            "Detox, 24-hour, hospital inpatient", "Detox, 24-hour, free-standing residential", "Rehab/residential, hospital (non-detox)",
            "Rehab/residential, short term (30 days or fewer)", "Rehab/residential, long term (more than 30 days)",
            "Ambulatory, intensive outpatient", "Ambulatory, non-intensive outpatient", "Ambulatory, detoxification"
        ]
    def days_waiting_options(self):
        return ["0", "1–7", "8–14", "15–30", "31 or more"]
    def FREQ_ATND_SELF_HELP_D(self):
        return [
            "No attendance", "1–3 times per month", "4–7 times per month", "8–30 times per month",
            "Some attendance, frequency is unknown"
        ]
    def length_of_stay_options(self):
        return [
            "1 to 30", "31 to 45 days", "46 to 60 days", "61 to 90 days", "91 to 120 days", "121 to 180 days", "181 to 365 days", "More than a year"
        ]
    def substance_use_options(self):
        return [
            "None", "Alcohol", "Cocaine/crack", "Marijuana/hashish", "Heroin", "Non-prescription methadone", "Other opiates and synthetics",
            "PCP", "Hallucinogens", "Methamphetamine/speed", "Other amphetamines", "Other stimulants", "Benzodiazepines", "Other tranquilizers",
            "Barbiturates", "Other sedatives or hypnotics", "Inhalants", "Over-the-counter medications", "Other drugs"
        ]
    def route_of_admin_options(self):
        return ["Oral", "Smoking", "Inhalation", "Injection", "Other"]
    def frequency_options(self):
        return ["No use in the past month", "Some use", "Daily use"]
    def age_first_use_options(self):
        return [
            "11 years and under", "12–14 years", "15–17 years", "18–20 years", "21–24 years", "25–29 years", "30 years and over"
        ]
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PatientQuestionnaireApp(root)
#     root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = PatientQuestionnaireApp(root)
    root.mainloop()
