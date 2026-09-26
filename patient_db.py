
registered_ids = set()


patients = {}


def register_new_patient(p_id, name, age, gender, disease, priority):
    p_id = p_id.strip().upper()

    # Check if patient already exists using set
    if p_id in registered_ids:
        print(f"\n[!] Error: Patient ID {p_id} already exists! Cannot register duplicate.")
        return False

    # Add to set to lock uniqueness
    registered_ids.add(p_id)

    # Add to patient dictionary
    patients[p_id] = {
        "name": name.strip(),
        "age": int(age),
        "gender": gender.strip(),
        "disease": disease.strip(),
        "priority": int(priority),  # 1 = Emergency, 2 = Urgent, 3 = Normal
        "history": [],              # List for appointment history
        "bills": []                 # List for charges
    }

    def check_p_id(p_id):
        print(f"\n[+] Patient {name} (ID: {p_id}) registered successfully!")
        return True

    


def patient_exists(p_id):
    return p_id.strip().upper() in registered_ids


def get_patient_info(p_id):
    return patients.get(p_id.strip().upper(), None)


def show_all_patients():
    if len(patients) == 0:
        print("\nNo patient records found.")
        return

    print("\n--- REGISTERED PATIENTS ---")
    print("ID       | Name             | Age | Gender | Priority   | Problem")
    print("-" * 68)
    for p_id in patients:
        info = patients[p_id]
        p_rank = info["priority"]
        if p_rank == 1:
            p_text = "1 (Emergency)"
        elif p_rank == 2:
            p_text = "2 (Urgent)"
        else:
            p_text = "3 (Normal)"
        print(f"{p_id:<8} | {info['name']:<16} | {info['age']:<3} | {info['gender']:<6} | {p_text:<10} | {info['disease']}")
    print("-" * 68)


def load_demo_patients():
    # Adding sample student testing data
    demo_data = [
        ("PAT101", "Ramesh Kumar", 58, "Male", "Chest Pain", 1),
        ("PAT102", "Ananya Sen", 24, "Female", "Sprained Ankle", 3),
        ("PAT103", "Kavita Nair", 72, "Female", "Severe Breathing Issue", 1),
        ("PAT104", "Rahul Bose", 31, "Male", "High Fever", 2),
        ("PAT105", "Sunita Sharma", 65, "Female", "Wrist Fracture", 2)
    ]
    for item in demo_data:
        if item[0] not in registered_ids:
            register_new_patient(item[0], item[1], item[2], item[3], item[4], item[5])
