# Create a virtual environment and edit the activation script to add
# the following information:
# - ENVIRONMENT="development"
# - SECRET="i ate your sweets"
# Then write the necessary code to access and print the values of these
# two environment variables in this script.
import os
secret1 = os.environ['ENVIRONMENT']
print(secret1)
secret2 = os.environ['SECRET']
print(secret2)
