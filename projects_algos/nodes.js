// NODE Class -> to build out the individual nodes which consist of two things.. data and a pointer to the next node

class Node {
    constructor(data){
        this.data = data
        this.next = null
    }
}

// SINGLY LINKED LIST (SSL) Class. 
// This will consist of the head node. SSL does not know where every other node is. It only knows where head node is.
// All the other nodes keep track of each other. 

class linkedList {
    constructor(){
        this.head = null
    }
}

// SLL METHODS. 

addFront(val){
    // 1. create a new node
    new_node = new Node(val)
    // 2. check to see if the list is empty or not. if empty place -> new val as head.
    // if list is not empty -> new val is the next node. 
    if(!self.head){
        self.head = new_node
        return self
    }
    new_node.next = this.head
    this.head = new_node
    return self
}


//  Add the value to the end
addToEnd(value) {
// loop through the list until current node.next is null to get to the end
    var currNode = this.head
    while(currNode.next !== null) {
        currNode = currNode.next
    }
    currNode.next = new SLLNode(value)
}