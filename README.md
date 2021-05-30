
# flaskAPI

### This is an API developed using Python's Flask framework.

#### It makes use of advanced data structures like linked list, hash table, binary search tree

``dummy data.py`` is used to populate the database

``linked_list.py`` contains the Linked List structure

``hash_table.py`` contains the Hash Table structure

``binary_search_tree.py`` contains the Binary Tree structue

``custom_queue.py`` contains the Queue structure

``stack.py`` contains the Stack structure

Create all the tables defined in the classes(``User, BlogPost``)

```python
from server import db
db.create_all()
```



### To run;

```shell script
python dummy_data.py
python server.py
```

#### Routes

#### `` /user ``   
- method = POST
- This is used to create a user. It requires parameter; name, email, phone number.

#### `` /user/descending_id ``
- method = GET
- This route is used to get all users in descending order(i.e from the highest id to the lowest id). It makes use of linked list

#### `` /user/ascending_id ``
- method = GET
- This route is used to get all users in ascending order(i.e from the lowest id to the highest id)

#### `` /user/'{USER_ID}' ``
- method = GET
- This route is used to get user with id equal to 'USER_ID'. It makes use of linked list

#### `` /user/'{USER_ID}' ``
- method = DELETE
- This route is used to delete a user with id=USER_ID. 

#### `` /blog/'{USER_ID}' ``
- method = POST
- This is used to create a blog post. The created post is by user with id equal to USER_ID. It requires parameter; title, body
- It makes use of hash table data structure

#### `` /blog/'{BLOG_ID}' ``
- method = GET
- This is used to get a blog post. The BLOG_ID is the id of the blog to be retrieved.
- It makes use of binary search tree data structure.

#### `` /blog/numeric_body``
- method = GET
- This is used to get a blog post.
- It makes use of queue data structure(append to the end and remove from the top)
    e.g people buying coffee from a coffee stand; New folks join the line from the end and those that have been attended to(in front) leave the line.

#### `` /blog/delete_last_five_post``
- method = DELETE
- This is used to delete the last five blog posts that were posted.
- It makes use of Stack data structure(append to the top and remove from the top).
    The newest post is always on top.

