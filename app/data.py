def load_logs():
    with open("logs.txt", "r") as f:
        return f.read().splitlines()
