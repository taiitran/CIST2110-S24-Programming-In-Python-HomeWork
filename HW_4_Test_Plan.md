# Test Plan for HW4
## 1. 'add' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
| 001 | test_add - Test with positive numbers | 3, 2 | 5 | 5 | PASS | N/A
| 002 | test_add - Test with positive numbers | 0, 5 | 5 | 5 | PASS | N/A

## 2. 'subtract' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
| 001 | test_subtract - Test with positive numbers | 5, 3 | 2 | 2 | PASS | N/A
| 002 | test_subtract - Test with positive numbers | 3, 5 | -2 | -2 | PASS | N/A

## 3. 'divide' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
| 001 | test_divide - Test with positive numbers | 6, 2 | 3 | 3 | PASS | N/A
| 002 | test_divide - Test with 0 and error | 1, 0 | Error | Error | PASS | N/A


## 4. 'multiply' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
| 001 | test_multiply - Test with positive numbers | 4, 3 | 12 | 12 | PASS | N/A
| 002 | test_multiply - Test with positive numbers | 4, 0 | 0 | 0 | PASS | N/A

## 5. 'greet' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
| 001 | test_greet - Test with name | John | John | John | PASS | N/A
| 002 | test_greet - Test with name | Doe | Doe | Doe | PASS | N/A

## 6. 'grade_calc' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
| 001 | grade_calculator - Test with positive numbers | 95 | A | A | PASS | N/A
| 002 | grade_calculator - Test with positive numbers | 85 | B | B | PASS | N/A
| 003 | grade_calculator - Test with positive numbers | 75 | C | C | PASS | N/A
| 004 | grade_calculator - Test with positive numbers | 79 | C | C | PASS | N/A
| 005 | grade_calculator - Test with positive numbers | 65 | D | D | PASS | N/A
| 006 | grade_calculator - Test with positive numbers | 50 | F | F | PASS | N/A
| 007 | grade_calculator - Test with positive numbers | 105 | Invalid Score | Invalid Score | PASS | N/A
| 008 | grade_calculator - Test with positive numbers | -5 | Invalid Score | Invalid Score | PASS | N/A


## 7. 'speed_check' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
| 001 | speed_check - Test with positive numbers | 10 | Too slow | Too slow | PASS | N/A
| 002 | speed_check - Test with positive numbers | 50 | Within limit | Within limit | PASS | N/A
| 001 | speed_check - Test with positive numbers | 80 | Over speed limit | Over speed limit | PASS | N/A
| 002 | speed_check - Test with positive numbers | 65 | Within limit | Within limit | PASS | N/A
    


## 8. 'is_leap_year' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
| 001 | test_is_leap_year - Test with years | 2020 | True | True | PASS | N/A
| 002 | test_is_leap_year - Test with years | 2021 | False | False | PASS | N/A
| 003 | test_is_leap_year - Test with years | 2000 | True | True | PASS | N/A
| 004 | test_is_leap_year - Test with years | 1900 | False | False | PASS | N/A


