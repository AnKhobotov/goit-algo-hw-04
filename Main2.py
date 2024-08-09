from pathlib import Path

file_name = Path("./Temp")

try:
    with open(file_name / "New_text.txt", "r", encoding='utf-8') as file:
        for line in file:
            print(line, end="")
except Exception as e:
    print(f"{e} with file")

new_dir = Path("ABC")
if not new_dir.exists():
    new_dir.mkdir()
