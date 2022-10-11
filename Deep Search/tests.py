import unittest
import main

# print(main.biggestPath({'dir1': {}, 'dir2': ['file1'], 'dir3': {'dir4': ['file2'], 'dir5': {'dir6': {'dir7': {}}}}}))

class TestSearch(unittest.TestCase):
  def test_ex1(self):
    d1 = {'dir1': {}, 'dir2': ['file1'], 'dir3': {'dir4': ['file2'], 'dir5': {'dir6': {'dir7': {}}}}}
    self.assertEqual(main.biggestPath(d1), '/dir3/dir5/dir6/dir7')

  def test_ex2(self):
    d2 = {'dir1': ['file1', 'file1']}
    self.assertEqual(main.biggestPath(d2), '/')

  def test_ex3(self):
    d3 = {'dir1': ['file1', 'file2', 'file2']}
    self.assertEqual(main.biggestPath(d3), '/dir1/file1')

  def test_ex4(self):
    d4 = {'dir1': {}, 'dir2': ['file1'], 'dir3': {'dir4': ['file2'], 'dir5': {'dir6': {'dir7': ['file2']}}}}
    self.assertEqual(main.biggestPath(d4), '/dir3/dir5/dir6/dir7/file2')

  def test_ex5(self):
    d5 = {'dir1': {}, 'dir2': ['file1'], 'dir3': {'dir4': ['file2'], 'dir5': {'dir6': {'dir7': ['file2', 'file2']}}}}
    self.assertEqual(main.biggestPath(d5), '/dir3/dir4/file2')

if __name__ == "__main__":
  unittest.main()
