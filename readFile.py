import configparser
from throwExceptions import FileFormatError
from throwExceptions import WrongConfigInput
from throwExceptions import SequenceTooLongException
from config import Config


class ReadFile:

    # read sequence file
    def seq_path(self, filepath, config=Config):
        with open(filepath, "r") as f:
            line = f.readline()
            if not line.startswith(">"):
                raise FileFormatError("it is not in FASTA format")
            seq = f.read().replace("\n","")
            if len(seq) > config.MAX_SEQ_LENGTH:
                raise SequenceTooLongException("The sequence can't be longer than the MAX_SEQ_LENTH")
        f.close()
        return seq

    # read config file
    def get_config(self, filepath):

        # check id config file contains all required arguments
        def check_config(required, config_parameters):
            if required not in config_parameters:
                raise WrongConfigInput('The ' + required + ' is missing from the config file.')

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

        gap_penalty = config["DEFAULT"].getint("GAP_PENALTY")
        same = config["DEFAULT"].getint("SAME")
        diff = config["DEFAULT"].getint("DIFF")
        max_seq_length = config["DEFAULT"].getint("MAX_SEQ_LENGTH")
        max_number_paths = config["DEFAULT"].getint("MAX_NUMBER_PATHS")

        # check value of the config file
        if max_seq_length < 0:
            raise WrongConfigInput("it should be a positive number")

        if max_number_paths < 0:
            raise WrongConfigInput("it should be a positive number")

        return Config(same, diff, gap_penalty, max_seq_length, max_number_paths)
