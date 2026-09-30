

import doctors
import patient_db
import appointments
import billing
import triage_sort
import storage


def show_menu():
    print("\n" + "=" * 48)
    print("HOSPITAL MANAGEMENT AND TRIAGE SYSTEM")
    print("=" * 48)
    print("1. Register New Patient")
    print("2. View Triage Priority Queue (Bubble Sort)")
    print("3. View Doctor Directory (Tuples)")
    print("4. View Patient Medical History")
    print("5. Add Service / Treatment Bill")
    print("6. Print Patient Invoice")
    print("7. Save Records to JSON File")
    print("0. Exit")
    print("=" * 48)


def handle_register():
    print("\n--- REGISTER PATIENT ---")
    p_id = input("Enter Patient ID (e.g. PAT106): ").strip()
    if p_id == "":
        print("[!] Patient ID cannot be empty.")
        return

    if patient_db.patient_exists(p_id):
        print(f"[!] Patient with ID {p_id.upper()} is already registered!")
        return

    name = input("Enter Name: ").strip()
    if name == "":
        print("[!] Name cannot be empty.")
        return

    age_input = input("Enter Age: ").strip()
    if not age_input.isdigit():
        print("[!] Please enter a valid number for age.")
        return
    age = int(age_input)

    gender = input("Enter Gender (Male/Female/Other): ").strip()
    disease = input("Enter Disease / Health Issue: ").strip()

    print("\nTriage Levels: 1 = Emergency | 2 = Urgent | 3 = Normal")
    p_input = input("Enter Priority (1-3): ").strip()
    if p_input not in ["1", "2", "3"]:
        print("[!] Invalid priority. Defaulting to 3 (Normal).")
        priority = 3
    else:
        priority = int(p_input)

    patient_db.register_new_patient(p_id, name, age, gender, disease, priority)


def handle_triage():
    patient_list = []
    for p_id in patient_db.patients:
        info = patient_db.patients[p_id]
        entry = {
            "id": p_id,
            "name": info["name"],
            "age": info["age"],
            "gender": info["gender"],
            "disease": info["disease"],
            "priority": info["priority"]
        }
        patient_list.append(entry)

    if len(patient_list) == 0:
        print("\nNo patients to sort.")
        return

    print("\nSort by:")
    print("1. Urgency (Emergency first, tie-breaker: older patients)")
    print("2. Age (Oldest patients first)")
    sort_choice = input("Enter choice (1/2): ").strip()

    if sort_choice == "1":
        sorted_res = triage_sort.bubble_sort_by_priority(patient_list)
        triage_sort.print_triage_queue(sorted_res)
    elif sort_choice == "2":
        sorted_res = triage_sort.bubble_sort_by_age(patient_list)
        triage_sort.print_triage_queue(sorted_res)
    else:
        print("[!] Invalid choice.")


def handle_appointment():
    print("\n--- BOOK APPOINTMENT ---")
    p_id = input("Enter Patient ID: ").strip()
    if not patient_db.check_patient_exists(p_id):
        print(f"[!] Patient {p_id} not found.")
        return

    doctors.show_doctors()
    doc_id = input("Enter Doctor ID: ").strip()
    date = input("Enter Date (DD-MM-YYYY): ").strip()
    notes = input("Enter Consultation Reason: ").strip()

    appointments.book_appointment(p_id, doc_id, date, notes)


def handle_history():
    print("\n--- VIEW MEDICAL HISTORY ---")
    p_id = input("Enter Patient ID: ").strip()
    appointments.show_patient_history(p_id)


def handle_add_bill():
    print("\n--- ADD MEDICAL BILL ITEM ---")
    p_id = input("Enter Patient ID: ").strip()
    if not patient_db.patient_exists(p_id):
        print(f"[!] Patient {p_id} not found.")
        return

    service = input("Enter Service Name (e.g. Blood Test, X-Ray): ").strip()
    amount_str = input("Enter Charge Amount: ").strip()

    try:
        amount = float(amount_str)
        if amount < 0:
            print("[!] Amount cannot be negative.")
            return
    except ValueError:
        print("[!] Invalid amount entered.")
        return

    billing.add_charge(p_id, service, amount)


def handle_view_invoice():
    print("\n--- VIEW INVOICE ---")
    p_id = input("Enter Patient ID: ").strip()
    billing.print_patient_invoice(p_id)


def main():
    print("=" * 48)
    print("  City General Hospital - CSE1021 Project")
    print("=" * 48)
    has_data = storage.load_records_from_file()
    if not has_data:
        print("[i] Loading demo patient records for first-time use...")
        patient_db.load_demo_patients()

    while True:
        show_menu()
        choice = input("Enter your choice (0-11): ").strip()

        if choice == "1":
            handle_register()
        elif choice == "2":
            handle_triage()
        elif choice == "3":
            doctors.show_doctors()
        elif choice == "4":
            handle_history()
        elif choice == "5":
            handle_add_bill()
        elif choice == "6":
            handle_view_invoice()
        elif choice == "7":
            storage.save_records_to_file()
        elif choice == "0":
            ans = input("\nDo you want to save before leaving? (y/n): ").strip().lower()
            if ans == "y":
                storage.save_records_to_file()
            print("\nProgram finished. Thank you!")
            break
        else:
            print("\n[!] Invalid option. Please choose a number from 0 to 11.")


if __name__ == "__main__":
    main()
