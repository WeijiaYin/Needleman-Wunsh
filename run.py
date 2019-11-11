from needlemanWunsh import NeedlemanWunsh
from readFile import ReadFile

if __name__ == '__main__':
    rf = ReadFile()
    config = rf.get_config('config.ini')
    nw = NeedlemanWunsh()
    mat, directmat = nw.calculate_matrix(rf.seq_path('a.txt', config), rf.seq_path('b.txt', config), config)
    nw.calculate_result(mat, directmat, rf.seq_path('a.txt', config), rf.seq_path('b.txt', config), "output.txt")