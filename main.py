# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("2:00 PM", "5:10"))


# Run unit tests automatically
main(module='test_module', exit=False)
