# LRU Cache in Python

A simple implementation of LRU cache in Python for learning purposes.

## Data Structures

In this implementation, we use the classic version of the LRU cache which is implemented using a 
Doubly Linked List and a Hash Map.

We have a custom implementation of Double Linked List.

### Doubly Linked List

The API of the Doubly Linked List is as follows:

| Name | Description |
| --- | --- |
| `insert_left` | Insert the element in the doubly linked list from the left side. |
| `insert_right` | Insert the element in the doubly linked list from the right side. |
| `pop_left` | Remove and return the leftmost node in the doubly linked list. |
| `pop_right` | Remove and return the rightmost node in the doubly linked list. |
| `delete_node` | Delete the node in the doubly linked list. |
| `delete` | Delete the first occurrence of the value in the doubly linked list. |

### LRU Cache

The API of the LRU cache is as follows:

| Name | Description |
| --- | --- |
| `__setitem__` | Set the provided value against the provided key in the cache. |
| `__getitem__` | Get the value mapped against the provided key if it exists. |

> Note: `__setitem__` and `__getitem__` are python data methods for better semantics. Consider them as equal to the `set` and `get` methods of any cache.

The working of `set` and `get` for this cache is as follows:

#### 1. Set Item

- Takes two arguments -- `key` and `value`.
- If cache size is less than maximum cache size allowed
	- Add the value in the doubly linked list from the right side.
    - Map the reference of the doubly linked list node in the hash map against the provided key.
- If cache size is more than maximum cache size allowed
	- Remove the leftmost element from the leftmost element from the doubly linked list.
	- Remove the mapping of that node's value from the hash map.
	- Add the new value in the double linked list from the right side.
	- Map the reference of the doubly linked list node in the hash map against the provided key.


#### 2. Get Item

- Take a single argument -- `key`.
- If the `key` does not exist in the hash map, then return `None`.
- If the `key` exists
	- Get the doubly linked list node from the hash map for the provided `key`
	- Delete the node from the doubly linked list.
	- Insert a new node (with same value) into doubly linked list from the right side.
	- Update the hash map for the `key` with the reference of the new node.
