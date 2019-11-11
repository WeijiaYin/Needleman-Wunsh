# Needleman-Wunsh
python 3.6
### example run command
```
python run.py -a a.txt -b b.txt -c config.txt -o output.txt
```
### example config.txt

```
[DEFAULT]
GAP_PENALTY = -1
SAME = 1
DIFF = -1
MAX_SEQ_LENGTH = 100
MAX_NUMBER_PATHS = 5
```

GAP_PENALTY: score from up or left   
SAME: score from diagonal if the character is the same   
DIFF: score from dignoal if the character is different   
MAX_SEQ_LENGTH: the max length of the input sequence   
MAX_NUMBER_PATHS: the max number of the output aligment pairs   
