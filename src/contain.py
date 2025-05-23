import os
import dotenv
import sys
import ast

dotenv.load_dotenv()

print(os.getenv("DOCK"))

print(sys.argv)
#print(input("data:"))