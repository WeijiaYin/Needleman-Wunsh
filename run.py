import argparse
from needlemanWunsh import NeedlemanWunsh
from readFile import ReadFile

if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', type=str, help='Path to the a sequence', required=True, dest='seq_a')
    parser.add_argument('-b', type=str, help='Path to the b sequence', required=True, dest='seq_b')
    parser.add_argument('-c', type=str, help='Path to the config file', required=True, dest='config_path')
    parser.add_argument('-o', type=str, help='Path to the output file', required=True, dest='output_path')
    args = parser.parse_args()

    rf = ReadFile()
    config = rf.get_config(args.config_path)
    nw = NeedlemanWunsh()
    mat, directmat = nw.calculate_matrix(rf.seq_path(args.seq_a, config), rf.seq_path(args.seq_b, config), config)
    score, alignments = nw.calculate_result(mat, directmat, rf.seq_path(args.seq_a, config), rf.seq_path(args.seq_b, config), config)
    # write results to file
    f = open(args.output_path, 'w')
    f.write('SCORE=' + str(score) + '\n')
    f.write('\n')
    for i in range(len(alignments)):
        f.write(alignments[i].res_a + '\n')
        f.write(alignments[i].res_b + '\n')
        f.write('\n')
    f.close()

