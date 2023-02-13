# Test task for tutor in Python

## Python
**What are the key differences between Python2 and Python3?**

The main differences are:
- print sentence
- iteration through dictionaries
- division sign truncation

Another key difference is that Python2 is already deprecated, that is, there is no support or updates after 2.7 version.

**What happens if you import the same library into the code twice?**

Nothing. Libraries and modules are imported once.

**What is circular (cyclic) import and how can you avoid it?**

A circular import happens when two or more modules import each other, causing one of these modules to be incomplete.

This is mostly a design issue. Sometimes the implementation is too convoluted, creating extra modules where one or two would suffice.

Another simple solution is to use deferred imports. This way, the module is used only in a limited scope.

**What is a context manager?**

These are tools that let us allocate resources at will, simplifying the task of reserving and freeing said resources. An example is the reserved word, `with`, which is commonly used to work with files and iterators.

**Describe how a list data structure works.**

A list is an indexed, mutable data structure. The notation to declare a list is by enclosing its elements in square brackets and separating them with commas, that is: `l = [1,2,3]`. One can access its data via individual indexing, e.g. `l[0], l[3], l[-1]`, or using slices, e.g. `l[1:], l[:-1]`. Since it is mutable, one can change its contents on-the-fly, unlike tuples. Python lists are able to store any data type, and several different types at the same time, including any other data structures.

## Algorithms

**Which data type in Python should I choose for the items container so that the operation of searching for an item is asymptotically the most efficient?**

The set. Given that is structure resembles a map, makes sense that is the most efficient in the long-run.

**Estimate the difficulty of quick sorting in the worst-case scenario.**

Quick sort performs the sorting in two phases, i.e. it needs two recursions. Of course, the complexity depends on the phases' depth, which in turn depends on the pivot's location. If the pivot is set at a extreme, the  worst complexity falls to $O(n^2$), being $n$ the number of elements to sort.

**Estimate the complexity of the operation of searching for an element in the search tree in the worst-case scenario.**

Assuming an unbalanced, unsorted binary search tree, the worst scenario is the one where the number of searches is equal to the number of nodes, $n$, in the tree. This results in a time complexity of $O(n)$.

**What is a “heap data structure”?**

A heap structure is a tree that complies with a specific set of conditions. For example, a binary heap is a binary tree that is balanced and its root can be either the maximum or minimum value of the data. Such structures are useful to perform priority queues.

**What features should a binary tree have in order to be a search tree?**

They must met the following conditons:
- The left-side of the tree must have lesser values than its root.
- The right-side of the tree must have greater values than its root.
- All sub-trees must comply with the above conditions.

## Django

**How can I get the value of the username variable in the controller if it is passed from the page by the POST method?**

`request.POST.get('username')`

**Which command runs the development web server in Django?**

`python manage.py runserver`

**What arguments in this code are passed to the view function?**

*`path('/example/<int:id>/', example_view)`*

Positioned `id` argument that has an `int` type

**You need to write a controller that returns data from the database in the form of an object. On the basis of which class would you create it?**

`ListView`

**You have changed the models in a project. What commands do you need to run to commit changes and start migrations?**

```shell
# start migrations
python manage.py makemigrations 'app_name'
pythom manage.py migrate
```

**What is middleware?**

Middleware is a framework that feeds the request/response processes in Django. Put simply, middleware adds blocks of code (*hooks*) for each server request. These can be use for security and/or debugging purposes.

## SQL

**What types of JOIN queries in SQL do you know? Describe them and specify the differences between them.**

- *Inner join*: intersects datasets matching a common key; unmatched data is ignored.
- *Left outer join*: intersects datasets matching a common key; unmatched data on the right side of the join is ignored.
- *Right outer join*: intersects datasets matching a common key; unmatched data on the left side of the join is ignored.
- *Full outer join*: intersects datasets matching a common key; unmatched data on both sides is included in result.
- *Self join*: intersects a dataset with itself matching a common key.

**There are two tables: A and B. The first table has 4 columns and 10 records, and the second one has 5 columns and 8 records. How many rows and columns will be output with the `select * from A,B` query, and why?**

$Col_{tot} = 4+5 = 9$; 
$Row_{tot} = 10*8 = 80$

SQL takes this query as a join, since there is no key to filter the data, this results in a map where each register from the second table is matched with each register of the first table (like a cartesian product), hence the final 80 registers.

**Indicate the main differences between SQL and NoSQL databases. Give examples of how both of them can be used and explain your choice.**

SQL databases focus on the structure of data (rows an columns) and the relations among these data. NoSQL databases aim to store non-relational data, facilitating its access and scalability.

SQL databases can be used for data analisys, since its structured nature allows one to find close relations between the data.

NoSQL databases are widly use in the blockchain, since they allow to track millions and millions of transactions and its storage without knowing its structure or relations with other data.

## General questions

**1. You need to write Python code that will send users' comments to a certain forum. Which request method would you choose for this — GET, POST, or PUT? Explain your choice.**

POST requests allow APIs to broadcast data on a running server. GET requests only obtain data. PUT requests can update a server.

I choose POST requests.

**2. Explain which is better: inheritance or composition. Why?**

Given the complexity of current systems, I lean toward composition. It allows for the expansion or completion of a working system in a simple manner, since the alteration only broadens it. Inheritance has a drawback: all child classes are based on a parent class. If a system based on inheritance needs to change, it is harder when this alteration must be implemented in the parent class, because all the remaining child classes would have to be adapted. In short, composition is more flexible and adapts better to complex systems. 

**3. Explain how authentication differs from authorization.**

Authentication is a process aimed to verify the identity of a user. Authorization establishes a user's level of access, once one determines the user's identity.

**4. What is versioning used for when creating REST API services?**

Versioning is used when a service has been altered in a significant manner (*breaking change*); small changes do not require versioning.

**5. What HTTP methods do you know?**

GET, HEAD, POST and PUT.

**6. Suggest several options for scaling your service.**

I was no able to answer this one.

**7. What ways do you know for changing file access rights in Linux?**

- Using `chown` (change owner)
- Using `chgrp` (change group)
- Using `chmod` (change level of access)

**8. List the key differences between processes and threads.**

Threads share memory access, processes use separate memory access.

**9. What ways of interaction between processes do you know?**

Communication, Synchronization

**10. You typed a 6-character command in the terminal and received the name of the current directory in response. Is this possible?**

Yes, if one counts the blank space as a character.
`pwd -L`

**11. What types of DNS records do you know?**

- A record (IPv4 address)
- AAAA record (IPv6 address)
- MX record (email server)

**12. 0 STDIN, 1 STDOUT, 2 STDERR — what does it mean?**

The types of standard input/output to terminal and their respective code for redirection.

**13. What is the name of the DNS record for IPv6?**

AAAA record.

## Writing code

**Task 1.**

*There are two lists: you need to return the elements that are in the first list but are missing in the second. Describe the complexity of your solution using Big O Notation.*

**Task 2.**

*There is an array of integers. You need to remove the zeros from it. Only O(1) of additional memory can be used. Example:*
```python
array = [0,1,0,0,4,5,6,7,0,8,-4,0] # input
[1,4,5,6,8,-4] # output
```
*You can leave your answer as a link to your repository in GitHub.*

**Code**: [https://github.com/alopgomez/test_task](https://github.com/alopgomez/test_task)

The code is in the `tasks.py`script and I offer some explanations in the `README.md` file.

---

**Why do you want to become a Tutor in Practicum?**

I simply enjoy teaching these subjects. I have had some experience mentoring Jr programmers and I have to say that those are my fondest memories working in IT.

**What competencies do you think a good tutor in your profession should have? Explain your opinion. Give examples from your own experience.**

Patience and assertiveness. From personal experience, most people learn by error and repetition, lots of it. So, one has to be patient and understand the pace of each student. But one also has to be stern, firm, so that the purpose of the class is served, not wasted.

**Where did you study back-end development and how did you get into this profession?**

I have been studying software engineering since high school, back- and front-end. I did well in my high school programming courses, and I remember the excitement of finishing a coding challenge (proposed or imposed), so I decided to study electronic engineering since it encompassed both subjects of physics and programming.
