import unittest

class TestHackerRankProblems(unittest.TestCase):
    
    def test_funny_string(self):
        self.assertEqual(funnyString("acxz"), "Funny")
        self.assertEqual(funnyString("bcxz"), "Not Funny")

    def test_alternating_characters(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("A"), 0) # Edge case

    def test_caesar_cipher(self):
        self.assertEqual(caesarCipher("a-Z", 2), "c-B")
        self.assertEqual(caesarCipher("abc", 27), "bcd") # k > 26

    def test_two_characters(self):
        self.assertEqual(twoCharacters("beabeefeab"), 5)
        self.assertEqual(twoCharacters("a"), 0) # Edge case

    def test_grid_challenge(self):
        self.assertEqual(gridChallenge(["ebc", "hjk", "mpq"]), "YES")
        self.assertEqual(gridChallenge(["zyx", "abc"]), "NO")

if __name__ == '__main__':
    unittest.main()