import sys
import random

for f in sys.argv[1:]:
    newf = f.replace(".html", ".txt")
    print(f"extracting words from {f} into {newf}")

    with open(newf, "w") as out:
        out.write("word " * int(random.random() * 5000 + 1000))
