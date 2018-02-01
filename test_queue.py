import unittest
from queue import Queue


class QueueTest(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_initialize_queue_buffer(self):
        self.assertTrue(len(self.q.array) == 100)
        self.assertTrue(self.q.max_buffer == 100)
        self.assertTrue(self.q.get_size() == 0)

    def test_initialize_queue_change_buffer_size(self):
        q = Queue(10)
        self.assertTrue(len(q.array) == 10)
        self.assertTrue(q.max_buffer == 10)
        self.assertTrue(q.get_size() == 0)

    def test_is_full(self):
        for i in range(100):
            self.q.enqueue(i)
        self.assertTrue(self.q.get_size() == 100)
        self.assertTrue(len(self.q.array) == 100)
        self.assertFalse(self.q.enqueue("test"))
        self.assertTrue(self.q.get_size() == 100)

    def test_is_full_case2(self):
        q3 = Queue(3)
        for i in range(3):
            q3.enqueue(i)
        self.assertTrue(q3.get_size() == 3)
        self.assertFalse(q3.enqueue("test"))
        self.assertTrue(q3.dequeue() == 0)
        self.assertTrue(q3.get_size() == 2)

    def test_is_empty(self):
        self.assertFalse(self.q.dequeue())

    def test_enqueue(self):
        self.q.enqueue("test1")
        self.q.enqueue("test2")
        self.q.enqueue("test3")
        queue_list = self.q.get_queue_all_list()
        self.assertTrue(queue_list[0] == "test1")
        self.assertTrue(queue_list[1] == "test2")
        self.assertTrue(queue_list[2] == "test3")
        self.assertTrue(len(queue_list) == 3)
        self.assertTrue(self.q.tail == 3)

    def test_dequeue(self):
        self.q.enqueue("test1")
        self.q.enqueue("test2")
        self.q.enqueue("test3")
        self.assertTrue(self.q.dequeue() == "test1")
        print(self.q.get_queue_all_list())
        self.assertTrue(len(self.q.get_queue_all_list()) == 2)
        self.assertTrue(self.q.head == 1)
        self.assertTrue(self.q.tail == 3)

    def test_en_and_dequeu(self):
        self.q.enqueue("test1")
        self.q.enqueue("test2")
        self.assertTrue(self.q.dequeue() == "test1")
        self.q.enqueue("test3")
        self.assertTrue(self.q.get_size() == 2)
        self.assertTrue(self.q.head == 1)
        self.assertTrue(self.q.tail == 3)
        self.assertTrue(self.q.dequeue() == "test2")
        self.q.enqueue("test4")
        self.assertTrue(self.q.get_size() == 2)
        self.assertTrue(self.q.head == 2)
        self.assertTrue(self.q.tail == 4)

    def test_get_stack_all_list(self):
        self.q.enqueue("test1")
        self.q.enqueue("test2")
        self.q.enqueue("test3")
        check_list = ["test1", "test2", "test3"]
        self.assertTrue(len(self.q.get_queue_all_list()) == 3)
        self.assertTrue(self.q.get_queue_all_list() == check_list)

        self.assertTrue(self.q.dequeue() == check_list.pop(0))
        self.assertTrue(len(self.q.get_queue_all_list()) == 2)
        self.assertTrue(self.q.get_queue_all_list() == check_list)
