# Test Plan for Project 3
## 1

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
| 001 | test_book_return - Test with book name, author name, and book isbn | "Test Book", "Author Name", 1234567890 | New Book Object Created | AssertionError: assert 'Author Name' == 'Test Book' | Failed | It read the "Text Book" as the first argument |
| 002 | test_book_return - Test with book name, author name, and book isbn | 1234567890, "Test Book", "Author Name" | New Book Object Created | New Book Object Created  | Pass | N/A |


## 2

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
| 001 | test_book_checkout - Test with book name, author name, and book isbn | Test Book", "Author Name", 1234567890 | New Book Object Created | New Book Object Created | Pass | N/A |

## 3

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
| 001 | test_book_return - Test with book name, author name, and book isbn | "Test Book", "Author Name", 1234567890 | New Book Object Created | New Book Object Created | Pass | N/A |

## 4

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
| 001 | test_user_creation - Test with user name and user id | "John Doe", 1 | New User Object Created | New User Object Created | Pass | N/A |

## 5

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
| 001 | test_user_borrow - Test with book name, author name, book isbn, user name, and user id | "Test Book", "Author Name", 1234567890, "John Doe", 1 | New User and Book Object Created | New User and Book Object Created | Pass | N/A |

## 6

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
| 001 | test_library_add_book - Test with book name, author name, and book isbn | "Test Book", "Author Name", 1234567890 | New User and Book Object Created | New User and Book Object Created | Pass | N/A |

## 7

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
| 001 | test_library_add_user - Test with user name and user id | "John Doe", 1 | New Library Object Created | New Library Object Created | Pass | N/A |

## 8

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
| 001 | test_library_find_book - Test with book name, author name, and book isbn | "Test Book", "Author Name", 1234567890 | New Library Object Created | AssertionError - test_library_find_book - assert None == <Project3.Book object at 0x10640d110> | Fail | It read the "Text Book" as the first argument |
| 002 | test_library_find_book - Test with book name, author name, and book isbn | 1234567890, "Test Book", "Author Name" | New Library Object Created | New Library Object Created | Pass | N/A |

## 9

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
| 001 | test_library_find_user |||| Pass | N/A |


