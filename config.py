class Config:
    # store config values
    SAME: int
    DIFF: int
    GAP_PENALTY: int
    MAX_SEQ_LENGTH: int
    MAX_NUMBER_PATH: int

    def __init__(self, same, diff, gap_penalty, max_seq_length, max_number_path):
        self.SAME = same
        self.DIFF = diff
        self.GAP_PENALTY = gap_penalty
        self.MAX_SEQ_LENGTH = max_seq_length
        self.MAX_NUMBER_PATH = max_number_path
