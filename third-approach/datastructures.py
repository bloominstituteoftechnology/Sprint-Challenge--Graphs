#!/usr/bin/env python

from typing import TypeVar, Optional
A = TypeVar('A')


class Queue:
    def __init__(self):
        self.queue: List[A] = list()

    def enqueue(self, a: A):
        self.queue.append(a)

    def dequeue(self) -> Optional[A]:
        if self.size > 0:
            rtrn: A = self.queue.pop(0)
            return rtrn
        else:
            return None

    @property
    def size(self):
        return len(self.queue)

class Stack:
    def __init__(self):
        self.stack: List[A] = list()

    def push(self, a: A):
        self.stack.append(a)

    def pop(self) -> A:
        if self.size > 0:
            return self.stack.pop()
        else:
            return None

    @property
    def size(self):
        return len(self.stack)
