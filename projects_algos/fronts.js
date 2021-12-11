class SLLNode { // Singly-linked list node class
    constructor(val) {
        this.value = val; // Holds value for this node
        this.next = null; // Pointer to next node
    }
}

class SLL { // The singly-linked list class itself
    constructor() { // Will start with no nodes
        this.head = null; // Head points to first node
    }

//ADD FRONT

addFront(value) {
    var newNode = new SLLNode(value); 
    newNode.next = this.head; 
    this.head = newNode; 
    return this.head; 
}

//REMOVE

removeFront() {
    if (this.head == null) {
        return this.head;
    }
    var removedNode = this.head; 
    this.head = removedNode.next; 
    return this.head;
}

// Return the value at the front (head) of the list
front() {
if (this.head == null) {
    return null;
} else {
    return this.head.value;
}