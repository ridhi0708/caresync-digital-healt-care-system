

import patient_db
import doctors


def book_appointment(p_id, doc_id, date, notes):
    p_id = p_id.strip().upper()
    doc_id = doc_id.strip().upper()

    if not patient_db.check_patient_exists(p_id):
        print(f"\n[!] Patient ID {p_id} not found.")
        return False

    doc_name = doctors.get_doctor_name(doc_id)
    patient = patient_db.get_patient_info(p_id)

    new_visit = {
        "doctor_id": doc_id,
        "doctor_name": doc_name,
        "date": date.strip(),
        "notes": notes.strip()
    }

    
    patient["history"].append(new_visit)
    print(f"\n[+] Appointment booked with {doc_name} for patient {patient['name']} on {date}.")
    return True


def show_patient_history(p_id):
    p_id = p_id.strip().upper()
    if not patient_db.patient_exists(p_id):
        print(f"\n[!] Patient ID {p_id} not found.")
        return

    patient = patient_db.get_patient_info(p_id)
    history_list = patient["history"]

    print(f"\n--- APPOINTMENT HISTORY FOR {patient['name']} ({p_id}) ---")
    if len(history_list) == 0:
        print("No previous appointments found.")
        return


    count = 1
    for visit in history_list:
        print(f"Visit #{count}:")
        print(f"  Date       : {visit['date']}")
        print(f"  Doctor     : {visit['doctor_name']} ({visit['doctor_id']})")
        print(f"  Notes      : {visit['notes']}")
        print("-" * 45)
        count = count + 1
