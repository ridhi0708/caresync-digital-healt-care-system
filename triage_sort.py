


def bubble_sort_by_priority(patient_records):

    records_copy = []
    for p in patient_records:
        records_copy.append(p)

    n = len(records_copy)


    for i in range(n):
        swapped = False
    
        for j in range(0, n - i - 1):
            p1 = records_copy[j]
            p2 = records_copy[j + 1]


            swap_needed = False
            if p1["priority"] > p2["priority"]:
                swap_needed = True
            elif p1["priority"] == p2["priority"] and p1["age"] < p2["age"]:
                swap_needed = True

            if swap_needed:
                # Classic swap using temporary variable
                temp = records_copy[j]
                records_copy[j] = records_copy[j + 1]
                records_copy[j + 1] = temp
                swapped = True

        if not swapped:
            break

    return records_copy


def bubble_sort_by_age(patient_records):
    #
    records_copy = []
    for p in patient_records:
        records_copy.append(p)

    n = len(records_copy)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if records_copy[j]["age"] < records_copy[j + 1]["age"]:
                temp = records_copy[j]
                records_copy[j] = records_copy[j + 1]
                records_copy[j + 1] = temp
                swapped = True
        if not swapped:
            break

    return records_copy


def print_triage_queue(sorted_list):
    if len(sorted_list) == 0:
        print("\nNo patients to show in triage queue.")
        return

    print("\n" + "=" * 68)
    print("              EMERGENCY TRIAGE QUEUE (SORTED)")
    print("=" * 68)
    print("Rank | ID       | Name             | Age | Priority   | Condition")
    print("-" * 68)

    rank = 1
    for p in sorted_list:
        p_val = p["priority"]
        if p_val == 1:
            p_str = "1 (Emergency)"
        elif p_val == 2:
            p_str = "2 (Urgent)"
        else:
            p_str = "3 (Normal)"

        print(f"#{rank:<3} | {p['id']:<8} | {p['name']:<16} | {p['age']:<3} | {p_str:<10} | {p['disease']}")
        rank = rank + 1

    print("=" * 68)
