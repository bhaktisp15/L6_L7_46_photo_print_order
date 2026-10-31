# L6_L7_46 : Photo Print Order

## Project Overview

This repository contains the implementation and testing work for the Photo Print Order application as part of Lab 6 and Lab 7.

The application calculates additional photo printing charges based on print size, number of copies, finish type, and membership status. It also validates print orders and determines dispatch status based on delivery requirements.

## Lab 6 : Code and Branch Coverage

### Objectives
- Understand code coverage and branch coverage.
- Design and execute test cases using Python and Pytest.
- Test normal, boundary, and invalid input conditions.
- Achieve high statement and branch coverage.

### Project Structure

```text
L6_L7_46_photo_print_order/
│
└── Lab 6/
    ├── README.md
    ├── photo_print_order.py
    └── test_photo_print_order.py
```

### Features Tested

**1. Extra Print Charge (`extra_print_charge`)**
- Supports 4x6, 5x7, and 8x10 print sizes.
- Calculates charges for additional prints.
- Applies membership benefits.
- Handles matte, glossy, and canvas finishes.
- Validates print size and number of copies.

**2. Order Validation (`order_valid`)**
- Validates regular and rush orders.
- Checks file size restrictions.
- Enforces copy limits.

**3. Dispatch Status (`dispatch_status`)**
- Determines whether an order is on time, tight, or missed.
- Considers framed and international orders.
- Applies different dispatch cutoffs.

## Technologies Used

- Python 3.11
- Pytest
- Pytest-Cov
- Git and GitHub

## Installation and Execution

### 1. Install dependencies

```bash
python -m pip install pytest pytest-cov
```

### 2. Navigate to the Lab 6 directory

```bash
cd "Lab 6"
```

### 3. Execute test cases

```bash
python -m pytest -v
```

### 4. Generate coverage report

```bash
python -m pytest --cov=photo_print_order --cov-branch --cov-report=term-missing
```

## Lab 6  : Test Results

| Metric | Result |
|---|---:|
| Total test cases | 27 |
| Tests passed | 27 |
| Tests failed | 0 |
| Statement coverage | 100% |
| Branch coverage | 100% |

All 27 test cases passed successfully, achieving 100% statement and branch coverage for `photo_print_order.py`.

<img width="940" height="358" alt="image" src="https://github.com/user-attachments/assets/1fc783be-cb76-411f-8bc9-52e7b42be434" />
<img width="940" height="600" alt="image" src="https://github.com/user-attachments/assets/5584b5cd-9d40-40b8-9ab6-a4fc3f748ac4" />
<img width="940" height="317" alt="image" src="https://github.com/user-attachments/assets/c669ee9c-d7df-44ac-8500-a29649c2221d" />

## Repository

**GitHub:** [L6_L7_46_photo_print_order](https://github.com/bhaktisp15/L6_L7_46_photo_print_order)

**Forked from:** [SETAPESU26/L6_L7_46_photo_print_order](https://github.com/SETAPESU26/L6_L7_46_photo_print_order)

---

