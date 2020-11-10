from collections import defaultdict

for file_name in [
    "instructor-training.txt",
    "shorter-workshops-events.txt",
    "full-workshops.txt",
]:
    d = defaultdict(int)
    with open(file_name, "r") as f:
        for line in f:
            if line.startswith("  "):
                key = line.split()[0]
                how_many = line.split()[1]
                if how_many != "unknown":
                    d[key] += int(how_many)
    print(file_name, sorted(d.items(), key=lambda x: x[1], reverse=True))
