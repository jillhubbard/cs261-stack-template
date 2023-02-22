# DO NOT MODIFY THIS FILE
# For credit, uncomment one test at a time and make sure to commit and push after each test passes 
# with a commit message that specifies the test name that passed.
# Run me via: python3 -m unittest test_stack or py -m unittest test_stack


import unittest
import time
from stack import Stack


class TestStack(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        Test 1: A Stack exists.
        """
        try:
            Stack()
        except NameError:
            self.fail("Could not instantiate Stack.")

    # def test_initially_empty(self):
    #     """
    #     Test 2: A stack is initially empty.
    #     """
    #     s = Stack()
    #     self.assertTrue(s.is_empty())

    # def test_initial_pop(self):
    #     """
    #     Test 3: Popping from an empty stack raises IndexError.
    #     """
    #     s = Stack()
    #     self.assertRaises(IndexError, s.pop)

    # def test_initial_peek(self):
    #     """
    #     Test 4: Peeking at an empty stack raises IndexError.
    #     """
    #     s = Stack()
    #     self.assertRaises(IndexError, s.peek)

    # def test_initial_push(self):
    #     """
    #     Test 5: Pushing a value onto the stack means the stack is no longer empty.
    #     """
    #     s = Stack()
    #     s.push('fee')
    #     self.assertFalse(s.is_empty())

    # def test_peek_one(self):
    #     """
    #     Test 6: A value pushed onto the stack can be peeked at.
    #     """
    #     s = Stack()
    #     s.push('fee')
    #     self.assertEqual('fee', s.peek())

    # def test_pop_one(self):
    #     """
    #     Test 7: A value pushed onto the stack can be popped.
    #     """
    #     s = Stack()
    #     s.push('fee')
    #     self.assertEqual('fee', s.pop())

    # def test_peek_two(self):
    #     """
    #     Test 8: Peeking at a stack with two values returns the last pushed value.
    #     """
    #     s = Stack()
    #     s.push('fee')
    #     s.push('fi')
    #     self.assertEqual('fi', s.peek())

    # def test_peek_state(self):
    #     """
    #     Test 9: Peeking doesn't mutate the stack.
    #     """
    #     s = Stack()
    #     s.push('fee')
    #     s.push('fi')
    #     self.assertEqual('fi', s.peek())
    #     self.assertEqual('fi', s.peek())

    # def test_pop_two(self):
    #     """
    #     Test 10: Popping from a stack with two values returns the last pushed value.
    #     """
    #     s = Stack()
    #     first_value = fake_value()
    #     second_value = fake_value()
    #     s.push(first_value)
    #     s.push(second_value)
    #     self.assertEqual(second_value, s.pop())

    # def test_pop_state(self):
    #     """
    #     Test 11: Popping removes the last pushed value from the stack.
    #     """
    #     s = Stack()
    #     first_value = fake_value()
    #     second_value = fake_value()
    #     s.push(first_value)
    #     s.push(second_value)
    #     self.assertEqual(second_value, s.pop())
    #     self.assertEqual(first_value, s.pop())
    #     self.assertTrue(s.is_empty())


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
