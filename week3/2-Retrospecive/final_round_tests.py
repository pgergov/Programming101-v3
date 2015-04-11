import unittest
import final_round


class FinalRoundTests(unittest.TestCase):

    def test_count_words(self):
        self.assertEqual(final_round.count_words(
            ["apple", "banana", "apple", "pie"]), {'apple': 2, 'pie': 1, 'banana': 1})
        self.assertEqual(final_round.count_words(
            ["python", "python", "python", "ruby"]), {'ruby': 1, 'python': 3})

    def test_unique_words(self):
        self.assertEqual(final_round.unique_words_count(
            ["apple", "banana", "apple", "pie"]), 3)
        self.assertEqual(final_round.unique_words_count(
            ["python", "python", "python", "ruby"]), 2)
        self.assertEqual(final_round.unique_words_count(["HELLO!"] * 10), 1)

    def test_nan_expand(self):
        self.assertEqual(final_round.nan_expand(3), "Not a Not a Not a NaN")
        self.assertEqual(final_round.nan_expand(0), "")

    def test_iterations_of_nan_expand(self):
        self.assertEqual(final_round.iterations_of_nan_expand("Not a NaN"), 1)
        self.assertEqual(final_round.iterations_of_nan_expand("asd"), False)

    def test_integer_prime_factorization(self):
        self.assertEqual(final_round.prime_factorization(10), [(2, 1), (5, 1)])
        self.assertEqual(final_round.prime_factorization(14), [(2, 1), (7, 1)])
        self.assertEqual(final_round.prime_factorization(
            356), [(2, 2), (89, 1)])
        self.assertEqual(final_round.prime_factorization(
            1000), [(2, 3), (5, 3)])

    def test_group_function(self):
        self.assertTrue(final_round.group(
            [1, 1, 1, 2, 3, 1, 1]) == [[1, 1, 1], [2], [3], [1, 1]])
        self.assertTrue(final_round.group(
            [1, 2, 1, 2, 3, 3]) == [[1], [2], [1], [2], [3, 3]])

    def test_longest_subsequence_of_equal_consecutive_elements(self):
        self.assertEqual(final_round.max_consecutive(
            [1, 2, 3, 3, 3, 3, 4, 3, 3]), 4)
        self.assertEqual(final_round.max_consecutive(
            [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]), 3)

    def test_group_by(self):
        result1 = {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]}
        self.assertEqual(final_round.groupby(
            lambda x: x % 2, [0,1,2,3,4,5,6,7]), result1)

        result2 = {'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]}
        self.assertEqual(final_round.groupby(
            lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]), result2)

        result3 = {0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]}
        self.assertEqual(final_round.groupby(
            lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]), result3)

    def test_spam_and_eggs(self):
        self.assertEqual(final_round.prepare_meal(5), "eggs")
        self.assertEqual(final_round.prepare_meal(3), "spam")
        self.assertEqual(final_round.prepare_meal(27), "spam spam spam")
        self.assertEqual(final_round.prepare_meal(15), "spam and eggs")
        self.assertEqual(final_round.prepare_meal(45), "spam spam and eggs")
        self.assertEqual(final_round.prepare_meal(7), "")

    def test_reduce_file_path(self):
        self.assertEqual(final_round.reduce_file_path(
            "/"), "/")
        self.assertEqual(final_round.reduce_file_path(
            "/srv/../"), "/")
        self.assertEqual(final_round.reduce_file_path(
            "/srv/www/htdocs/wtf/"), "/srv/www/htdocs/wtf")
        self.assertEqual(final_round.reduce_file_path(
            "/srv/./././././"), "/srv")
        self.assertEqual(final_round.reduce_file_path(
            "/etc/../etc/../etc/../"), "/")

    def test_word_from_an_bn(self):
        self.assertTrue(final_round.is_an_bn(""))
        self.assertTrue(final_round.is_an_bn("aaabbb"))
        self.assertFalse(final_round.is_an_bn("bbbaaa"))

    def test_credit_card_validation(self):
        self.assertTrue(final_round.is_credit_card_valid(79927398713))
        self.assertFalse(final_round.is_credit_card_valid(79927398715))

    def test_goldbach_conjecture(self):
        self.assertEqual(final_round.goldbach(
            100), [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)])

    def test_magic_square(self):
        self.assertFalse(final_round.magic_square(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        self.assertTrue(final_round.magic_square(
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
        self.assertTrue(final_round.magic_square(
            [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
        self.assertTrue(final_round.magic_square(
            [[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
        self.assertFalse(final_round.magic_square(
            [[16, 23, 17], [78, 32, 21], [17, 16, 15]]))

    def test_friday_years(self):
        self.assertEqual(final_round.friday_years(1000, 2000), 178)
        self.assertEqual(final_round.friday_years(1753, 2000), 44)
        self.assertEqual(final_round.friday_years(1990, 2015), 4)

if __name__ == '__main__':
    unittest.main()
