import json


class QueueOutOfRangeException(Exception):
    pass


class Queue:
    def __init__(self, size=None):
        self.items = []
        self.front = -1
        self.rear = -1
        self.size = size  # max size (optional)

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return self.size is not None and self.rear - self.front + 1 >= self.size

    def enqueue(self, item):
        if self.is_full():
            raise QueueOutOfRangeException("Queue is full!")

        if self.is_empty():
            self.front = 0

        self.rear += 1
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        item = self.items[self.front]
        self.front += 1

        # reset when queue becomes empty
        if self.front > self.rear:
            self.front = -1
            self.rear = -1
            self.items = []  # clean list

        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.items[i], end=" ")
            print()


class NamedQueue(Queue):
    def __init__(self, name, size):
        super().__init__(size)
        self.name = name

    def track_queue_in_json(self):
        queue_dict = {
            "name": self.name,
            "size": self.size,
            "items": self.items[self.front:self.rear + 1] if not self.is_empty() else []
        }
        return json.dumps(queue_dict, indent=4)

    @staticmethod
    def save_queue_to_json_file(named_queue, filename):
        with open(filename,'a') as file:
            file.write(named_queue.track_queue_in_json())

    @staticmethod
    def load_queue_from_json_file(filename):
        with open(filename, 'r') as file:
            queue_dict = json.load(file)

        named_queue = NamedQueue(queue_dict["name"], queue_dict["size"])

        for item in queue_dict["items"]:
            named_queue.enqueue(item)

        return named_queue


if __name__ == "__main__":
    nq = NamedQueue("MyQueu7", 5)
    nq.enqueue(10)
    nq.enqueue(20)
    nq.enqueue(30)
    nq.enqueue(40)
    nq.enqueue(60)


    print("Queue contents:")
    nq.display()

    json_data = nq.track_queue_in_json()
    print("Queue in JSON format:")
    print(json_data)

    NamedQueue.save_queue_to_json_file(nq, 'queue_data.jsonl')

    loaded_nq = NamedQueue.load_queue_from_json_file('queue_data.jsonl')

    print("Loaded Queue contents from JSON file:")
    loaded_nq.display()
