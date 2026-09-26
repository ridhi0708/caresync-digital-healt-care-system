

import json
import os
import patient_db


SAVE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hospital_records.json")


def save_records_to_file():
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(patient_db.patients, f, indent=4)
        print(f"\n[+] Successfully saved {len(patient_db.patients)} records to hospital_records.json.")
        return True
    except Exception as e:
        print(f"\n[!] Error saving file: {e}")
        return False


def load_records_from_file():
    if not os.path.exists(SAVE_FILE):
        return False

    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)

    
        patient_db.patients.clear()
        patient_db.patients.update(data)

        
        patient_db.registered_ids.clear()
        for p_id in patient_db.patients:
            patient_db.registered_ids.add(p_id)

        print(f"\n[+] Loaded {len(patient_db.patients)} patient records from hospital_records.json.")
        return True
    except Exception as e:
        print(f"\n[!] Error reading file: {e}")
        return False
