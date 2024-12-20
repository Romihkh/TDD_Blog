import pytest
from blog.authors import Author

def test_create_author_sets_name_and_email():
    author = Author()
    author.create_author("Alice", "alice@example.com")
    assert author.name == "Alice"
    assert author.email == "alice@example.com"
    assert author.active is True

def test_create_author_overwrites_existing_author():
    author = Author()
    author.create_author("Bob", "bob@example.com")
    author.create_author("Charlie", "charlie@example.com")
    assert author.name == "Charlie"
    assert author.email == "charlie@example.com"

def test_update_author_changes_name():
    author = Author()
    author.create_author("Dave", "dave@example.com")
    author.update_author(name="David")
    assert author.name == "David"
    assert author.email == "dave@example.com"

def test_update_author_changes_email():
    author = Author()
    author.create_author("Eve", "eve@example.com")
    author.update_author(email="eve_new@example.com")
    assert author.email == "eve_new@example.com"

def test_delete_author_sets_inactive():
    author = Author()
    author.create_author("Frank", "frank@example.com")
    author.delete_author()
    assert author.active is False

def test_delete_author_already_inactive():
    author = Author()
    author.delete_author()
    assert author.active is False
