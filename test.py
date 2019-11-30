from readFile import ReadFile
from throwExceptions import WrongConfigInput
from throwExceptions import SequenceTooLongException
from throwExceptions import FileFormatError
from config import Config
from needlemanWunsh import NeedlemanWunsh
import unittest


class Test(unittest.TestCase):
    # test if the config value or argument is not proper throws wrongconfiginput exception
    def test_wrong_config_error(self):
        # given
        expected = WrongConfigInput
        file_path1 = 'wrongconfig1.txt'
        file_path2 = 'wrongconfig2.txt'
        file_path3 = 'wrongconfig3.txt'
        # when
        rf = ReadFile()
        # then
        self.assertRaises(expected, rf.get_config, file_path1)
        self.assertRaises(expected, rf.get_config, file_path2)
        self.assertRaises(expected, rf.get_config, file_path3)

    # test if sequence is longer than the max length throws sequencetoolong exception
    def test_too_long_sequence(self):
        # given
        expected = SequenceTooLongException
        file_path = 'longsequence.txt'
        config_path = 'config.txt'
        # when
        rf = ReadFile()
        config = rf.get_config(config_path)
        # then
        self.assertRaises(expected, rf.seq_path, file_path, config)

    # test if file is not in fasta format throws fileformaterror exception
    def test_file_format_error(self):
        # given
        expected = FileFormatError
        file_path = 'wrongformat.txt'
        config_path = 'config.txt'
        # when
        rf = ReadFile()
        # then
        config = rf.get_config(config_path)
        self.assertRaises(expected, rf.seq_path, file_path, config)

    # test read sequence function
    def test_read_sequence(self):
        # given
        config_path = 'config.txt'
        seq_path = 'a.txt'
        expected = 'GATTACA'
        # when
        rf = ReadFile()
        config = rf.get_config(config_path)
        seq = rf.seq_path(seq_path, config)
        # then
        self.assertEqual(seq, expected)

    # test read config file function
    def test_read_config(self):
        # given
        config_path = 'config.txt'
        same = 5
        diff = -5
        gap_penalty = -2
        max_seq_length = 100
        max_number_path = 20
        # when
        rf = ReadFile()
        config = rf.get_config(config_path)
        c = Config(same, diff, gap_penalty, max_seq_length, max_number_path)
        # then
        self.assertEqual(config.SAME, c.SAME)
        self.assertEqual(config.DIFF, c.DIFF)
        self.assertEqual(config.GAP_PENALTY, c.GAP_PENALTY)
        self.assertEqual(config.MAX_SEQ_LENGTH, c.MAX_SEQ_LENGTH)
        self.assertEqual(config.MAX_NUMBER_PATH, c.MAX_NUMBER_PATH)

    # test result
    def test_calculate_result(self):
        # given
        same = 1
        diff = -1
        gap_penalty = -1
        max_seq_length = 10
        max_number_path = 5
        seq_a = 'GATTACA'
        seq_b = 'GCATGCU'
        expected_score = 0
        expected_length = 3
        # when
        c = Config(same, diff, gap_penalty, max_seq_length, max_number_path)
        nw = NeedlemanWunsh()
        mat, directmat = nw.calculate_matrix(seq_a, seq_b, c)
        score, aligments = nw.calculate_result(mat, directmat, seq_a, seq_b, c)
        #then
        self.assertEqual(score, expected_score)
        self.assertEqual(len(aligments), expected_length)

    # test result with the constraint of the max path number
    def test_max_path(self):
        # given
        same = 1
        diff = -1
        gap_penalty = -1
        max_seq_length = 10
        max_number_path = 1
        seq_a = 'GATTACA'
        seq_b = 'GCATGCU'
        expected_score = 0
        expected_length = 1
        # when
        c = Config(same, diff, gap_penalty, max_seq_length, max_number_path)
        nw = NeedlemanWunsh()
        mat, directmat = nw.calculate_matrix(seq_a, seq_b, c)
        score, aligments = nw.calculate_result(mat, directmat, seq_a, seq_b, c)
        self.assertEqual(score, expected_score)
        self.assertEqual(len(aligments), expected_length)


if __name__ == '__main__':
    unittest.main()
