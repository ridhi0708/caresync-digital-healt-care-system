import doctors
import patient_db
import appointments
import billing
import triage_sort
import storage


def show_menu():
    print("\n" + "=" * 48)
    print("        HOSPITAL MANAGEMENT SYSTEM")
    print("=" * 48)
    print("1. Register New Patient")
    print("2. View Triage Priority Queue")
    print("3. View Doctor Directory")
    print("4. View Patient Medical History")
    print("5. Add Service / Treatment Bill")
    print("6. Print Patient Invoice")
    print("7. Save Records")
    print("0. Exit")
    print("=" * 48)


def register_patient():
    print("\n--- REGISTER NEW PATIENT ---")

    patient_id = input("Enter Patient ID (e.g. PAT106): ").strip()

    if not patient_id:
        print("[!] Patient ID cannot be empty.")
        return

    if patient_db.patient_exists(patient_id):
        print(f"[!] Patient {patient_id.upper()} is already registered.")
        return

    name = input("Enter Name: ").strip()

    if not name:
        print("[!] Name cannot be empty.")
        return

    age_text = input("Enter Age: ").strip()

    if not age_text.isdigit():
        print("[!] Please enter a valid age.")
        return

    age = int(age_text)

    gender = input("Enter Gender (Male/Female/Other): ").strip()
    disease = input("Enter Disease / Health Issue: ").strip()

    print("\nTriage Level:")
    print("1 - Emergency")
    print("2 - Urgent")
    print("3 - Normal")

    priority_text = input("Enter Priority (1-3): ").strip()

    if priority_text in ("1", "2", "3"):
        priority = int(priority_text)
    else:
        print("[!] Invalid priority. Setting it to Normal.")
        priority = 3

    patient_db.register_new_patient(
        patient_id,
        name,
        age,
        gender,
        disease,
        priority
    )


def view_triage_queue():
    patients = []

    for patient_id, patient in patient_db.patients.items():
        patients.append({
            "id": patient_id,
            "name": patient["name"],
            "age": patient["age"],
            "gender": patient["gender"],
            "disease": patient["disease"],
            "priority": patient["priority"]
        })

    if not patients:
        print("\nThere are no patients to sort.")
        return

    print("\nSort patients by:")
    print("1. Urgency (Emergency first)")
    print("2. Age (Oldest first)")

    choice = input("Enter your choice (1/2): ").strip()

    if choice == "1":
        sorted_patients = triage_sort.bubble_sort_by_priority(patients)
        triage_sort.print_triage_queue(sorted_patients)

    elif choice == "2":
        sorted_patients = triage_sort.bubble_sort_by_age(patients)
        triage_sort.print_triage_queue(sorted_patients)

    else:
        print("[!] Invalid choice.")


def book_appointment():
    print("\n--- BOOK APPOINTMENT ---")

    patient_id = input("Enter Patient ID: ").strip()

    if not patient_db.check_patient_exists(patient_id):
        print(f"[!] Patient {patient_id} was not found.")
        return

    doctors.show_doctors()

    doctor_id = input("Enter Doctor ID: ").strip()
    date = input("Enter Date (DD-MM-YYYY): ").strip()
    reason = input("Enter Consultation Reason: ").strip()

    appointments.book_appointment(
        patient_id,
        doctor_id,
        date,
        reason
    )


def view_history():
    print("\n--- PATIENT MEDICAL HISTORY ---")

    patient_id = input("Enter Patient ID: ").strip()
    appointments.show_patient_history(patient_id)


def add_bill():
    print("\n--- ADD BILL ITEM ---")

    patient_id = input("Enter Patient ID: ").strip()

    if not patient_db.patient_exists(patient_id):
        print(f"[!] Patient {patient_id} was not found.")
        return

    service = input(
        "Enter Service Name (e.g. Blood Test, X-Ray): "
    ).strip()

    amount_text = input("Enter Charge Amount: ").strip()

    try:
        amount = float(amount_text)

        if amount < 0:
            print("[!] Amount cannot be negative.")
            return

    except ValueError:
        print("[!] Please enter a valid amount.")
        return

    billing.add_charge(patient_id, service, amount)


def view_invoice():
    print("\n--- PATIENT INVOICE ---")

    patient_id = input("Enter Patient ID: ").strip()
    billing.print_patient_invoice(patient_id)


def main():
    print("=" * 48)
    print("       City General Hospital")
    print("          CSE1021 Project")
    print("=" * 48)

    # Load existing records when the program starts.
    records_loaded = storage.load_records_from_file()

    if not records_loaded:
        print("[i] No saved records found.")
        print("[i] Loading demo patient records...")
        patient_db.load_demo_patients()

    while True:
        show_menu()

        choice = input("Enter your choice (0-7): ").strip()

        if choice == "1":
            register_patient()

        elif choice == "2":
            view_triage_queue()

        elif choice == "3":
            doctors.show_doctors()

        elif choice == "4":
            view_history()

        elif choice == "5":
            add_bill()

        elif choice == "6":
            view_invoice()

        elif choice == "7":
            storage.save_records_to_file()

        elif choice == "0":
            save_choice = input(
                "\nDo you want to save your records before exiting? (y/n): "
            ).strip().lower()

            if save_choice == "y":
                storage.save_records_to_file()

            print("\nProgram finished. Thank you!")
            break

        else:
            print("[!] Invalid option. Please choose a number from 0 to 7.")


if __name__ == "__main__":
    main()
```
