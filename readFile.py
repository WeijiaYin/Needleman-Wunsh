import configparser
from throwExceptions import FileFormatError
from throwExceptions import WrongConfigInput
from throwExceptions import SequenceTooLongException
from config import Config

class ReadFile:

    def seq_path(self, filepath, config=Config):
        with open(filepath, "r") as f:
            line = f.readline()
            if not line.startswith(">"):
                raise FileFormatError("it is not in FASTA format")
            seq = f.read().replace("\n","")
            if len(seq) > config.MAX_SEQ_LENGTH:
                raise SequenceTooLongException("The sequence can't be longer than the MAX_SEQ_LENTH")
        return seq

    def get_config(self, filepath):

        def check_config(field, required_fileds):
            if field not in required_fileds:
                raise WrongConfigInput("The {filed} is missing from the config file.")

        required_fields = [
            "same",
            "diff",
            "gap_penalty",
            "max_seq_length",
            "max_number_paths"
        ]

        config = configparser.ConfigParser()
        config.read(filepath)

        for field in required_fields:
            check_config(field, dict(config["DEFAULT"]))

        GAP_PENALTY = config["DEFAULT"].getint("GAP_PENALTY")
        SAME = config["DEFAULT"].getint("SAME")
        DIFF = config["DEFAULT"].getint("DIFF")
        MAX_SEQ_LENGTH = config["DEFAULT"].getint("MAX_SEQ_LENGTH")
        MAX_NUMBER_PATHS = config["DEFAULT"].getint("MAX_NUMBER_PATHS")

        if MAX_SEQ_LENGTH < 0:
            raise WrongConfigInput("it should be a positive number")

        if MAX_NUMBER_PATHS < 0:
            raise WrongConfigInput("it should be a positive number")

        return Config(SAME, DIFF, GAP_PENALTY, MAX_SEQ_LENGTH, MAX_NUMBER_PATHS)
