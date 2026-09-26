# README.md

## Project Title
Hospital Management System[span_0](start_span)[span_0](end_span)[span_1](start_span)[span_1](end_span)

## Overview of the Project
The Hospital Management System is a terminal-based Python application built to streamline daily administrative operations within a clinic or hospital[span_2](start_span)[span_2](end_span). It provides a complete workflow for registering patients, managing a roster of doctors, scheduling appointments, calculating bills, and prioritizing patient care using a custom triage algorithm. All patient data is persistently stored in a local JSON database[span_3](start_span)[span_3](end_span)[span_4](start_span)[span_4](end_span).

## Features
*   **Patient Database**: Register new patients with unique IDs, name, age, gender, disease, and priority level (Emergency, Urgent, Normal)[span_5](start_span)[span_5](end_span)[span_6](start_span)[span_6](end_span). Prevents duplicate registrations using Python sets[span_7](start_span)[span_7](end_span).
*   **Doctor Roster**: View an immutable list of available doctors and their respective departments[span_8](start_span)[span_8](end_span)[span_9](start_span)[span_9](end_span)[span_10](start_span)[span_10](end_span).
*   **Appointment Management**: Book appointments for registered patients with specific doctors and record diagnostic notes[span_11](start_span)[span_11](end_span)[span_12](start_span)[span_12](end_span)[span_13](start_span)[span_13](end_span). View the complete appointment history for any patient[span_14](start_span)[span_14](end_span)[span_15](start_span)[span_15](end_span).
*   **Billing & Invoicing**: Add itemized charges for hospital services and generate a formatted final bill displaying the total amount due[span_16](start_span)[span_16](end_span)[span_17](start_span)[span_17](end_span)[span_18](start_span)[span_18](end_span).
*   **Triage Queue Sorting**: Sort the patient queue based on medical priority (Emergency first) or age (oldest first) utilizing a custom Bubble Sort algorithm[span_19](start_span)[span_19](end_span)[span_20](start_span)[span_20](end_span)[span_21](start_span)[span_21](end_span).
*   **Data Persistence**: Automatically saves and loads all records to `hospital_records.json` so data is not lost between sessions[span_22](start_span)[span_22](end_span)[span_23](start_span)[span_23](end_span).

## Technologies/Tools Used
*   **Language**: Python 3[span_24](start_span)[span_24](end_span)
*   **Standard Libraries**: `json` (for data storage), `os` (for file path handling)[span_25](start_span)[span_25](end_span)[span_26](start_span)[span_26](end_span)
*   **Data Structures**: Dictionaries (main database), Sets (duplicate prevention), Tuples (immutable staff records), Lists (queues and histories)[span_27](start_span)[span_27](end_span)

## Steps to Install & Run the Project
1.  Ensure you have Python 3.x installed on your system.
2.  Clone or download the project repository to your local machine.
3.  Open a terminal or command prompt and navigate to the project directory.
4.  Run the main application file using the command: `python main.py`[span_28](start_span)[span_28](end_span)[span_29](start_span)[span_29](end_span).

## Instructions for Testing
1.  Launch the application and select the option to load demo data. The system includes a `load_demo_patients()` function that automatically registers sample patients (e.g., "Ramesh Kumar" with Chest Pain, "Ananya Sen" with a Sprained Ankle) for quick testing[span_30](start_span)[span_30](end_span).
2.  Register a new custom patient to verify duplicate ID handling.
3.  Book an appointment and add billing items to the newly created patient.
4.  Run the final bill generation to ensure calculations are accurate.
5.  Access the triage sorting menu and test both sorting by priority and sorting by age to observe the Bubble Sort implementation[span_31](start_span)[span_31](end_span)[span_32](start_span)[span_32](end_span).
6.  Close and restart the application to verify that `hospital_records.json` successfully loads previous data[span_33](start_span)[span_33](end_span)[span_34](start_span)[span_34](end_span).

