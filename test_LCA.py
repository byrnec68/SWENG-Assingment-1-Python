import unittest
import LCA

class TestLCA(unittest.TestCase):

    def test_LCA(self):
        root = LCA.formBST(LCA.Node(1))
        empty = LCA.formEmptyBST(LCA.Node(1))
        self.assertEqual(LCA.findLCA(root, 4, 5), 2) #Expected answer == 2
        self.assertEqual(LCA.findLCA(root, 3,2),1)#Expected answer == 1
        self.assertEqual(LCA.findLCA(empty, 2, 3), -1)#Null list, expected answer -1

if __name__ == '__main__':
    unittest.main()
