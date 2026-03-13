import sys

def args_as_text():
    user_input = " ".join(sys.argv[1:])

    if not user_input.strip():
        print("No commandline arguments. Query is expected in commandline arguments.")
        sys.exit()

    return user_input
