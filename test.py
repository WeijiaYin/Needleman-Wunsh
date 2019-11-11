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
        rf = ReadFile()
        self.assertRaises(WrongConfigInput, rf.get_config, 'wrongconfig1.txt')
        self.assertRaises(WrongConfigInput, rf.get_config, 'wrongconfig2.txt')
        self.assertRaises(WrongConfigInput, rf.get_config, 'wrongconfig3.txt')

    # test if sequence is longer than the max length throws sequencetoolong exception
    def test_too_long_sequence(self):
        rf = ReadFile()
        config = rf.get_config('config.txt')
        self.assertRaises(SequenceTooLongException, rf.seq_path, 'longsequence.txt', config)

    # test if file is not in fasta format throws fileformaterror exception
    def test_file_format_error(self):
        rf = ReadFile()
        config = rf.get_config('config.txt')
        self.assertRaises(FileFormatError, rf.seq_path, 'wrongformat.txt', config)

    # test read sequence function
    def test_read_sequence(self):
        rf = ReadFile()
        config = rf.get_config('config.txt')
        seq = rf.seq_path('a.txt', config)
        self.assertEqual(seq, 'GATTACA')

    # test read config file function
    def test_read_config(self):
        rf = ReadFile()
        config = rf.get_config('config.txt')
        c = Config(1, -1, -1, 100, 5)
        self.assertEqual(config.SAME, c.SAME)
        self.assertEqual(config.DIFF, c.DIFF)
        self.assertEqual(config.GAP_PENALTY, c.GAP_PENALTY)
        self.assertEqual(config.MAX_SEQ_LENGTH, c.MAX_SEQ_LENGTH)
        self.assertEqual(config.MAX_NUMBER_PATH, c.MAX_NUMBER_PATH)

    # test result
    def test_calculate_result(self):
        c = Config(1, -1, -1, 10, 5)
        nw = NeedlemanWunsh()
        mat, directmat = nw.calculate_matrix('GATTACA', 'GCATGCU', c)
        score, aligments = nw.calculate_result(mat, directmat, 'GATTACA', 'GCATGCU', c)
        self.assertEqual(score, 0)
        self.assertEqual(len(aligments), 3)

    # test result with the constraint of the max path number
    def test_max_path(self):
        c = Config(1, -1, -1, 10, 1)
        nw = NeedlemanWunsh()
        mat, directmat = nw.calculate_matrix('GATTACA', 'GCATGCU', c)
        score, aligments = nw.calculate_result(mat, directmat, 'GATTACA', 'GCATGCU', c)
        self.assertEqual(score, 0)
        self.assertEqual(len(aligments), 1)


if __name__ == '__main__':
    unittest.main()
