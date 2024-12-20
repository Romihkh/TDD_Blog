import pytest
from blog.comments import Comment

def test_comment_add_sets_text():
    comment = Comment()
    comment.add_comment("First comment")
    assert comment.text == "First comment"

def test_comment_add_overwrite_existing():
    comment = Comment()
    comment.add_comment("First comment")
    comment.add_comment("Second comment")
    assert comment.text == "Second comment"

def test_comment_edit_changes_text():
    comment = Comment()
    comment.add_comment("Initial comment")
    comment.edit_comment("Edited comment")
    assert comment.text == "Edited comment"

def test_comment_edit_empty():
    comment = Comment()
    comment.add_comment("Comment")
    comment.edit_comment("")
    assert comment.text == ""

def test_comment_delete_sets_deleted():
    comment = Comment()
    comment.add_comment("Something")
    comment.delete_comment()
    assert comment.deleted is True

def test_comment_delete_already_deleted():
    comment = Comment()
    comment.delete_comment()
    assert comment.deleted is True
