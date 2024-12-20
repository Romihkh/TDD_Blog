import pytest
from blog.posts import Post

def test_post_publish_sets_published_and_date():
    post = Post(title="Draft Title", content="Draft Content")
    post.publish()
    assert post.published is True
    assert post.published_date is not None

def test_post_publish_on_already_published():
    post = Post(title="Old Title", content="Old Content")
    post.publish()
    post.publish()
    assert post.published is True

def test_post_edit_changes_title_and_content():
    post = Post(title="Old Title", content="Old Content")
    post.edit(new_title="New Title", new_content="New Content")
    assert post.title == "New Title"
    assert post.content == "New Content"

def test_post_edit_partial_change():
    post = Post(title="Title", content="Content")
    post.edit(new_title="Only Title Changed", new_content=None)
    assert post.title == "Only Title Changed"
    assert post.content == "Content"

def test_post_delete_sets_deleted():
    post = Post(title="Title", content="Content")
    post.delete()
    assert post.deleted is True

def test_post_delete_already_deleted():
    post = Post(title="Title", content="Content")
    post.delete()
    post.delete()
    assert post.deleted is True
