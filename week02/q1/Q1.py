import re
import json
import os


pattern = re.compile(
    r'^\[([A-Za-z]{3} [A-Za-z]{3} \d{2} \d{2}:\d{2}:\d{2} \d{4})\] \[([a-zA-Z]+)\] (.+)'
)

timestamp = []
level = []
message = []
info = {}
count_error = 0
count_notice = 0

os.chdir(os.path.dirname(__file__))
try:
    with open(r"C:\maktab137\week02\q1\server.log", "r") as f:
        for line in f:
            for index, line in enumerate(f):
                sentence = pattern.match(line)
                if sentence:
                    timestamp.append(sentence.group(1))
                    level.append(sentence.group(2))
                    message.append(sentence.group(3))
                    if sentence.group(2) == "error":
                        count_error += 1
                        with open("critical_errors.csv", "a") as error:
                            error.write(f"[{sentence.group(1)}] : [{sentence.group(3)}]\n")
                    if sentence.group(2) == "notice":
                        count_notice += 1

                else:
                    with open("errors.log", "a") as file:
                        file.write(f"{index}\t{line}\n")

        with open("summary.json", "a") as summary:
            info = {
                "error": count_error,
                "notice": count_notice,
            }
            json.dump(info, summary)

    for i in timestamp:
        print(i)
    for i in level:
        print(i)
    for i in message:
        print(i)

except FileNotFoundError:
    print("File not found")


