lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [a + b + c + d for a in lowercase for b in lowercase for c in digits for d in digits]
correct_answer == answer