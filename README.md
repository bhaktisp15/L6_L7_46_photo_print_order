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

## Lab 7: Fuzz Testing and Input Validation

### Objective

Use Hypothesis to discover input validation bugs in the Photo Print Order
application and fix them through defensive programming.

### Files

| File | Description |
|---|---|
| `Lab 7/photo_print_order.py` | Application with input validation fixes |
| `Lab 7/test_photo_print_order.py` | Hypothesis fuzz tests for all three functions |

### Functions Tested

- `parse_order`: Parses the print size and number of copies.
- `file_size_average`: Calculates the integer average of file sizes.
- `payable_amount`: Applies 18% tax, subtracts the discount, and prevents a negative payable amount.

### Testing Approach

Each function was tested using `@given(st.text() | st.none())`.
Hypothesis generated arbitrary Unicode strings and `None` to uncover
inputs that caused crashes.

### Bugs Discovered

| Function | Failing Inputs Found | Error |
|---|---|---|
| `parse_order` | Empty string, `None` | `ValueError`, `AttributeError` |
| `file_size_average` | Empty string, `None` | `ValueError`, `AttributeError` |
| `payable_amount` | Empty string, `"|"`, `None` | `ValueError`, `AttributeError` |

### Fixes Implemented

- Validate input types before calling string methods.
- Check the number of fields separated by `:` or `|`.
- Handle invalid numeric conversions.
- Reject empty print sizes and nonpositive copy counts.
- Reject negative file sizes, amounts, and discounts.
- Reject nonfinite payment values and calculation results.
- Return `None` for invalid inputs instead of raising an unhandled exception.

### Installation and Execution

Install the dependencies:

```bash
python -m pip install hypothesis pytest
```

From the repository root, run:

```bash
cd "Lab 7"
python photo_print_order.py
python -m pytest test_photo_print_order.py -v
```

### Valid Input Example

| Input | Output |
|---|---|
| `4x6:25` | `('4X6', 25)` |
| `4,8,12` | `8` |
| `450|50` | `481.0` |

### Test Results

| Stage | Passed | Failed |
|---|---:|---:|
| Original application | 0 | 3 |
| Fixed application | 3 | 0 |

All three fuzz tests passed after the fixes. The valid-input examples
continued to produce the expected results. Passing fuzz tests demonstrate
that the generated inputs caused no crashes during the run; they do not
prove correctness for every possible input.

## Repository

**GitHub:** [L6_L7_46_photo_print_order](https://github.com/bhaktisp15/L6_L7_46_photo_print_order)

**Forked from:** [SETAPESU26/L6_L7_46_photo_print_order](https://github.com/SETAPESU26/L6_L7_46_photo_print_order)

---

