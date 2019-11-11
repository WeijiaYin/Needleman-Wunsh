class FileFormatError(Exception):
    # if the file is not in FASTA format throws this exception
    pass


class WrongConfigInput(Exception):
    # if the value or arguments of the config file throws this exception
    pass


class SequenceTooLongException(Exception):
    # if the length of the sequence is longer than the max length declared in the config file throw this exception
    pass
