# statement.md

## Problem Statement
Small clinics and medical facilities often rely on manual, paper-based workflows to manage patient registration, queue prioritization, and billing[span_36](start_span)[span_36](end_span). This approach is prone to data loss, calculation errors in billing, and inefficient triage processes where critical patients might experience delayed care. There is a need for a lightweight, digital system to reliably store records and automate queue sorting based on medical urgency.

## Scope of the Project
This project focuses on the core administrative and operational tasks of a hospital reception and triage desk[span_37](start_span)[span_37](end_span). It handles complete CRUD (Create, Read, Update, Delete) operations for patient records within a terminal interface, manages an immutable staff roster, tracks visit histories, and computes financial totals. Crucially, it includes an algorithmic triage component that actively sorts patients by priority or age[span_38](start_span)[span_38](end_span)[span_39](start_span)[span_39](end_span), ensuring efficient queue management. The scope does not include advanced features like graphical user interfaces (GUI), online payment processing, or external database server integration.

## Target Users
*   **Hospital Receptionists**: To quickly register patients, book appointments, and generate itemized invoices[span_40](start_span)[span_40](end_span).
*   **Triage Nurses/Administrators**: To generate sorted patient queues based on emergency levels to allocate care effectively[span_41](start_span)[span_41](end_span).
*   **Clinic Managers**: To maintain an accurate, persistent local database of patient histories and hospital operations[span_42](start_span)[span_42](end_span).

## High-Level Features
*   **Demographic Data Management**: Secure patient registration with automatic duplicate prevention[span_43](start_span)[span_43](end_span).
*   **Clinical History Tracking**: Automated logging of doctor appointments and diagnostic notes linked to specific patient IDs[span_44](start_span)[span_44](end_span).
*   **Financial Processing**: Dynamic invoice generation capable of aggregating multiple service charges into a final bill[span_45](start_span)[span_45](end_span).
*   **Algorithmic Prioritization**: Automated patient sorting queues using bubble sort logic for emergency triage[span_46](start_span)[span_46](end_span)[span_47](start_span)[span_47](end_span).
*   **Local File Storage**: Persistent saving and loading of all system state data using JSON format[span_48](start_span)[span_48](end_span).
*