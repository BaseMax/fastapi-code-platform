import sys
code = sys.stdin.read()

try:
    exec(code, {"__builtins__": {}})
except Exception as e:
    print("Error:", e)
