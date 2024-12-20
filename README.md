# Blog Project (TDD Example)

This is a simple Python-based project designed to demonstrate Test-Driven Development (TDD) principles, testing practices using `pytest`, and measuring code coverage using `coverage`. The project simulates a basic blog scenario with three main classes: `Post`, `Comment`, and `Author`. Each class contains three methods, and for each method, we have two test cases.

## Project Structure

```
TDD_blog/
    blog/
        __init__.py
        posts.py
        comments.py
        authors.py
    tests/
        __init__.py
        test_posts.py
        test_comments.py
        test_authors.py
    requirements.txt
    pyproject.toml (or setup.cfg)
    README.md
```

### Components

- **blog/posts.py**: Contains the `Post` class and its methods:
  - `publish()`: Publishes a post, setting `published` and `published_date`.
  - `edit(new_title, new_content)`: Edits the title and/or content of a post.
  - `delete()`: Marks a post as deleted.

- **blog/comments.py**: Contains the `Comment` class and its methods:
  - `add_comment(text)`: Sets the comment text.
  - `edit_comment(new_text)`: Edits the existing comment text.
  - `delete_comment()`: Marks the comment as deleted.

- **blog/authors.py**: Contains the `Author` class and its methods:
  - `create_author(name, email)`: Creates or overwrites the author’s info.
  - `update_author(name=None, email=None)`: Updates author’s name and/or email.
  - `delete_author()`: Marks the author as inactive (deleted).

### Tests

All tests are located in the `tests/` directory. We have three test files corresponding to each class:

- `tests/test_posts.py`
- `tests/test_comments.py`
- `tests/test_authors.py`

Each test file contains 6 tests (2 tests per method), ensuring that each method is thoroughly validated:

- For `Post`:
  - Testing `publish()` to ensure it sets the published flag and date, and behaves correctly if called again.
  - Testing `edit()` to verify it updates title and/or content, even if partial updates are given.
  - Testing `delete()` to confirm it correctly marks the post as deleted, and remains deleted if called multiple times.

- For `Comment`:
  - Testing `add_comment()` to ensure it sets the text and can overwrite it if called again.
  - Testing `edit_comment()` to verify comment text updates correctly, including empty strings.
  - Testing `delete_comment()` to confirm that comments are marked as deleted, and the status remains consistent if called again.

- For `Author`:
  - Testing `create_author()` to ensure correct initialization of author details, and overwriting if called again.
  - Testing `update_author()` to ensure selective updates to name or email without affecting the other fields.
  - Testing `delete_author()` to confirm that authors can be marked inactive, and remain inactive if called multiple times.

### TDD Approach

This project follows a Test-Driven Development approach:

1. **Write tests first**: All the tests in the `tests/` directory are written before implementing the classes and methods.
2. **Run tests to see them fail**: Initially, running `pytest` on the project should yield failures since the classes and methods do not yet exist or are incomplete.
3. **Implement just enough code to pass the tests**: Create the `Post`, `Comment`, and `Author` classes with their respective methods in the `blog/` directory so that all tests pass.
4. **Refactor if needed**: Once tests are passing, you can clean up or optimize the code while ensuring tests still pass.

### Installation & Requirements

**Prerequisites**:  
- Python 3.7+  
- `pip` (Python package manager)

**Dependencies** are listed in `requirements.txt`, which may include `pytest` and `coverage`:

```bash
pip install -r requirements.txt
```

If not listed, you can manually install them:
```bash
pip install pytest coverage
```

### Running Tests

To run tests:
```bash
pytest --maxfail=1 --disable-warnings -v
```

All tests should pass, indicating that the code is functioning as intended.

### Code Coverage

To measure code coverage:
```bash
coverage run -m pytest
coverage report
```

To generate an HTML coverage report:
```bash
coverage html
```

Open `htmlcov/index.html` in your browser to view a detailed coverage report.

### Example of TDD Workflow

1. **Initial test run (failing)**: Before implementing `Post`, run `pytest`. It will fail because `Post` does not exist.
2. **Implement `Post` class**: Create `Post` with the `publish`, `edit`, and `delete` methods.
3. **Re-run tests**: Now tests related to `Post` should pass if implemented correctly.
4. **Move to `Comment` and `Author`**: Repeat the process—write tests first (already done), implement classes to pass them, and verify by running tests.
5. **Refactor code**: If there’s any cleanup or optimization, do it now. Re-run tests to ensure no regressions.

### Project Goals

- **Demonstrate TDD**: Write tests first, then implement code to make tests pass.
- **Ensure High Test Coverage**: By writing thorough tests for each method, we aim for close to 100% coverage.
- **Maintain Code Quality**: The tests serve as a safety net to prevent regression and encourage clean, maintainable code.

