import os
from django.test import TestCase
from dotenv import find_dotenv, load_dotenv
# Create your tests here.


dotenv_path = find_dotenv()

load_dotenv(dotenv_path)
test = os.getenv("TEST_ENV_VAR")

print(test)