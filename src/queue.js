class Queue {
    constructor() {
        this.queue = [];
    }

    dequeue() {
        return this.queue.shift();
    }

    enqueue(it) {
        this.queue.push(it);

        return true;
    }

    enqueueArray(arr) {
        for(let i = 0; i < arr.length; i++) {
            this.enqueue(arr[i]);
        }
    }

    isEmpty() {
        return !this.queue[0];
    }

    peek(i) {
        return this.queue[i];
    }

    next() {
        return this.queue[0];
    }
}

module.exports = Queue;
