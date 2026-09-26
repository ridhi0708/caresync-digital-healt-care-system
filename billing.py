

import patient_db


def add_charge(p_id, service_name, price):
    p_id = p_id.strip().upper()
    if not patient_db.patient_exists(p_id) :
        print(f"\n[!] Patient ID {p_id} not found.")
        return False

    patient = patient_db.get_patient_info(p_id)
    bill_item = {
        "service": service_name.strip(),
        "amount": float(price)
    }

    
    patient["bills"].append(bill_item)
    print(f"\n[+] Added Rs. {float(price):.2f} for '{service_name}' to patient {p_id}.")
    return True


def print_patient_invoice(p_id):
    p_id = p_id.strip().upper()
    if not patient_db.patient_exists(p_id):
        print(f"\n[!] Patient ID {p_id} not found.")
        return

    patient = patient_db.get_patient_info(p_id)
    bill_list = patient["bills"]

    print("\n" + "=" * 45)
    print("            PATIENT BILL / INVOICE")
    print("=" * 45)
    print(f"Patient ID   : {p_id}")
    print(f"Patient Name : {patient['name']}")
    print(f"Age / Gender : {patient['age']} / {patient['gender']}")
    print("-" * 45)

    if len(bill_list) == 0:
        print("No charges recorded yet.")
        print("-" * 45)
        print("Total Amount Due: Rs. 0.00")
        print("=" * 45)
        return

    
    total_bill = 0.0
    for item in bill_list:
        s_name = item["service"]
        cost = item["amount"]
        total_bill = total_bill + cost
        print(f"- {s_name:<25} : Rs. {cost:>8.2f}")

    print("-" * 45)
    print(f"Total Amount Payable        : Rs. {total_bill:>8.2f}")
    print("=" * 45)
