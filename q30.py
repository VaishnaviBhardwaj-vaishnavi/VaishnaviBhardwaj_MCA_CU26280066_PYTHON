import csv

with open("merged.csv", "w", newline="") as out:
    writer = csv.writer(out)
    header_written = False

    for filename in ["file1.csv", "file2.csv"]:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            header = next(reader, None)

            if header is None:
                continue

            if not header_written:
                writer.writerow(header)
                header_written = True

            writer.writerows(reader)

print("CSV files merged successfully.")