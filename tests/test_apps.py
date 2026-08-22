import unittest

class TestLLMApps(unittest.TestCase):
    def test_prompt_format(self):
        prompt = f'Summarize: Artificial Intelligence'
        self.assertEqual(prompt, 'Summarize: Artificial Intelligence')

if __name__ == '__main__':
    unittest.main()
