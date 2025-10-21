"""
Supongamos que queremos procesar un archivo CSV con información de usuarios, 
calcular su edad media y guardar una lista con los nombres en mayúsculas.
"""

import csv
from datetime import datetime
from typing import List


def calculate_average_age(birthdates: List[str]) -> float:
    """
    Calculate the average age given a list of birthdates in YYYY-MM-DD format.

    Args:
        birthdates (List[str]): A list of birthdate strings.

    Returns:
        float: The average age, or 0.0 if the list is empty.
    """
    current_year = datetime.now().year
    ages = []

    for date_str in birthdates:
        try:
            year = int(date_str.split("-")[0])
            ages.append(current_year - year)
        except (ValueError, IndexError):
            # Skip malformed birthdate values
            continue

    return sum(ages) / len(ages) if ages else 0.0


def read_user_data(filepath: str) -> List[tuple[str, str]]:
    """
    Read user data from a CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        List[tuple[str, str]]: A list of (name, birthdate) tuples.
    """
    users = []
    with open(filepath, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append((row.get("name", "").strip(), row.get("birthdate", "").strip()))
    return users


def write_uppercase_names(names: List[str], output_path: str) -> None:
    """
    Write a list of names (converted to uppercase) to a text file.

    Args:
        names (List[str]): The names to write.
        output_path (str): Path to the output text file.
    """
    with open(output_path, mode="w", encoding="utf-8") as file:
        for name in names:
            file.write(f"{name.upper()}\n")


def process_user_data(input_csv: str, output_txt: str) -> None:
    """
    Process user data from a CSV file:
      1. Read users and birthdates.
      2. Compute average age.
      3. Save uppercase names to a text file.

    Args:
        input_csv (str): Path to the input CSV file.
        output_txt (str): Path to the output text file.
    """
    users = read_user_data(input_csv)
    birthdates = [b for _, b in users]
    names = [n for n, _ in users]

    avg_age = calculate_average_age(birthdates)
    print(f"Average age: {avg_age:.2f}")

    write_uppercase_names(names, output_txt)


if __name__ == "__main__":
    process_user_data("users.csv", "names.txt")
