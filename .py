# CSE1021 - Introduction to Problem Solving and Programming
# Project: Hospital Management System
# Module: hospital_data.py
# Description: Handles data structures (dictionaries, sets, tuples, lists) and file storage

import json

# Tuple to store immutable doctor records: (Doctor ID, Doctor Name, Department)
# Doctors are fixed staff members, so tuples are suitable to avoid accidental modifications
DOCTORS = (
    ("DOC101", "Dr. Rajesh Sharma", "General Medicine"),
    ("DOC102", "Dr. Priya Patel", "Cardiology"),
    ("DOC103", "Dr. Amit Verma", "Pediatrics"),
    ("DOC104", "Dr. Sneha Reddy", "Orthopedics"),
    ("DOC105", "Dr. Vikram Rao", "Emergency")
)

# Set to store unique patient IDs and prevent duplicate registrations
patient_id_set = set()

# Main dictionary database for patients
# Key: PAT-ID (e.g., 'PAT101'), Value: dictionary of patient details
patient_dict = {}


def load_data_from_json(filename="hospital_records.json"):
    """
    Loads patient data from a JSON file into patient_dict and patient_id_set.
    """
    global patient_dict, patient_id_set
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            patient_dict = data
            # Clear old set and re-populate with keys from the loaded dictionary
            patient_id_set.clear()
            for pat_id in patient_dict.keys():
                patient_id_set.add(pat_id)
        print(f"\n[SUCCESS] Successfully loaded {len(patient_dict)} patient record(s) from '{filename}'.")
    except FileNotFoundError:
        print(f"\n[INFO] '{filename}' not found. Starting with empty records.")
    except Exception as e:
        print(f"\n[ERROR] An error occurred while loading data: {e}")


def save_data_to_json(filename="hospital_records.json"):
    """
    Saves the current patient_dict to a JSON file.
    """
    try:
        with open(filename, "w") as file:
            json.dump(patient_dict, file, indent=4)
        print(f"\n[SUCCESS] All records successfully saved to '{filename}'.")
    except Exception as e:
        print(f"\n[ERROR] Could not save data: {e}")


def register_patient(pat_id, name, age, gender, disease, priority):
    """
    Registers a new patient. Checks set to ensure no duplicate ID is used.
    """
    # Check if patient ID already exists in the set
    if pat_id in patient_id_set:
        print(f"\n[ERROR] Patient ID '{pat_id}' is already registered! Please use a unique ID.")
        return False

    # Add ID to the set to enforce uniqueness
    patient_id_set.add(pat_id)

    # Store patient data in the dictionary
    # history and bills are initialized as empty lists
    patient_dict[pat_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "disease": disease,
        "priority": priority,  # 1: Emergency, 2: Urgent, 3: Normal
        "history": [],         # List of appointment history strings/entries
        "bills": []            # List of billing items (charges)
    }

    print(f"\n[SUCCESS] Patient '{name}' (ID: {pat_id}) registered successfully!")
    return True


def display_all_patients():
    """
    Displays all registered patients in patient_dict.
    """
    if len(patient_dict) == 0:
        print("\nNo patients registered in the system yet.")
        return

    print("\n" + "=" * 65)
    print(f"{'ID':<10} {'Name':<18} {'Age':<6} {'Gender':<8} {'Priority':<10} {'Disease'}")
    print("=" * 65)
    for pat_id in patient_dict:
        info = patient_dict[pat_id]
        print(f"{pat_id:<10} {info['name']:<18} {info['age']:<6} {info['gender']:<8} {info['priority']:<10} {info['disease']}")
    print("=" * 65)


def display_doctors():
    """
    Displays the list of doctors using the immutable tuple.
    """
    print("\n" + "-" * 55)
    print(f"{'Doctor ID':<12} {'Doctor Name':<25} {'Department'}")
    print("-" * 55)
    # Loop through the DOCTORS tuple
    for doc in DOCTORS:
        doc_id = doc[0]
        doc_name = doc[1]
        doc_dept = doc[2]
        print(f"{doc_id:<12} {doc_name:<25} {doc_dept}")
    print("-" * 55)


def add_appointment(pat_id, doc_id, date, diagnosis):
    """
    Adds an appointment record to the patient's history list.
    """
    # Check if patient exists in our dictionary
    if pat_id not in patient_dict:
        print(f"\n[ERROR] Patient ID '{pat_id}' not found.")
        return False

    # Find doctor name from DOCTORS tuple
    doc_name = "Unknown Doctor"
    found_doc = False
    for doc in DOCTORS:
        if doc[0] == doc_id:
            doc_name = doc[1]
            found_doc = True
            break

    if not found_doc:
        print(f"\n[WARNING] Doctor ID '{doc_id}' not recognized. Proceeding anyway.")

    appointment_entry = {
        "doctor_id": doc_id,
        "doctor_name": doc_name,
        "date": date,
        "notes": diagnosis
    }

    # Append to the history list of this patient
    patient_dict[pat_id]["history"].append(appointment_entry)
    print(f"\n[SUCCESS] Appointment added to {patient_dict[pat_id]['name']}'s history.")
    return True


def view_patient_history(pat_id):
    """
    Displays the appointment history list of a specific patient.
    """
    if pat_id not in patient_dict:
        print(f"\n[ERROR] Patient ID '{pat_id}' not found.")
        return

    patient = patient_dict[pat_id]
    history_list = patient["history"]

    print(f"\n--- Appointment History for {patient['name']} (ID: {pat_id}) ---")
    if len(history_list) == 0:
        print("No prior appointments found.")
        return

    # Loop through the list of appointments
    for i in range(len(history_list)):
        entry = history_list[i]
        print(f"[{i + 1}] Date: {entry['date']}")
        print(f"    Doctor: {entry['doctor_name']} ({entry['doctor_id']})")
        print(f"    Diagnosis / Notes: {entry['notes']}")


def add_bill_item(pat_id, service_name, amount):
    """
    Adds a bill entry (service and amount) to the patient's billing list.
    """
    if pat_id not in patient_dict:
        print(f"\n[ERROR] Patient ID '{pat_id}' not found.")
        return False

    item = {
        "service": service_name,
        "amount": amount
    }
    patient_dict[pat_id]["bills"].append(item)
    print(f"\n[SUCCESS] Added charge of Rs. {amount:.2f} for '{service_name}' to patient {pat_id}.")
    return True


def generate_final_bill(pat_id):
    """
    Calculates total charges by looping through the patient's billing list.
    """
    if pat_id not in patient_dict:
        print(f"\n[ERROR] Patient ID '{pat_id}' not found.")
        return

    patient = patient_dict[pat_id]
    bills_list = patient["bills"]

    print("\n" + "=" * 45)
    print(f"         HOSPITAL INVOICE")
    print("=" * 45)
    print(f"Patient ID   : {pat_id}")
    print(f"Patient Name : {patient['name']}")
    print(f"Age / Gender : {patient['age']} / {patient['gender']}")
    print("-" * 45)

    if len(bills_list) == 0:
        print("No billable services recorded for this patient.")
        print("Total Due    : Rs. 0.00")
        print("=" * 45)
        return

    # Calculate sum using a simple loop (no built-in sum or external lib)
    total_amount = 0.0
    for bill in bills_list:
        service = bill["service"]
        cost = bill["amount"]
        total_amount = total_amount + cost
        print(f"- {service:<26} : Rs. {cost:>8.2f}")

    print("-" * 45)
    print(f"TOTAL AMOUNT PAYABLE        : Rs. {total_amount:>8.2f}")
    print("=" * 45)
