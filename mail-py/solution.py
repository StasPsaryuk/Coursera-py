import sys
digit_string = sys.argv[1]

s = sum(map(int, digit_string)) # Sum of digit string
print(s)

""" 
sys.argv[0] - name of the running file, sys.argv[1] - string to be transmitted. 
test - python3 solution.py 873 

"""