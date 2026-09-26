
doctors_list = (
    ("DOC101", "Dr. Rajesh Sharma", "Cardiology"),
    ("DOC102", "Dr. Priya Patel", "Pediatrics"),
    ("DOC103", "Dr. Amit Verma", "General Medicine"),
    ("DOC104", "Dr. Sneha Reddy", "Orthopedics"),
    ("DOC105", "Dr. Vikram Rao", "Emergency Care")
)


def show_doctors():
    # Loop through the doctors tuple and display details
    print("\n--- AVAILABLE DOCTORS ---")
    print("ID       | Name                   | Department")
    print("-" * 50)
    for doc in doctors_list:
        print(f"{doc[0]:<8} | {doc[1]:<22} | {doc[2]}")
    print("-" * 50)


def get_doctor_name(doc_id):
    clean_id = doc_id.strip().upper()
    for doc in doctors_list:
        if doc[0] == clean_id:
            return doc[1]
    return "General Physician"
