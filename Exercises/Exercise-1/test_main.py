import unittest
import os

class TestUser(unittest.TestCase):
    
    def test_downloadmechanism(self):
        target_path = os.getcwd() + '\\downloads'
        for a, b, files in os.walk(target_path):
            assert files
    
    def test_unzipping(self):
        pass
    
if __name__=='__main__':
    unittest.main()
    test_downloadmechanism()
    print("everything passed")