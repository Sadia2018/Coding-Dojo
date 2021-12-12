// Create display() that returns a string containing all list values. 
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


// Display the values of all the nodes in the list
display() {
    var listStr = ""; 
    if (this.head == null) {
        return ""; 
    }
    listStr += this.head.value; 
    
    var runner = this.head.next;
    while (runner != null) {
        listStr += ", " + runner.value; 
        runner = runner.next; 
    }
    return listStr;
}
