import pandas as pd


GOOGLE_CONTACT_COLUMNS = [
    "First Name",
    "Middle Name",
    "Last Name",
    "Phonetic First Name",
    "Phonetic Middle Name",
    "Phonetic Last Name",
    "Name Prefix",
    "Name Suffix",
    "Nickname",
    "File As",
    "Organization Name",
    "Organization Title",
    "Organization Department",
    "Birthday",
    "Notes",
    "Photo",
    "Labels",
    "Phone 1 - Label",
    "Phone 1 - Value"
]


def generate_contacts(
    input_csv: str,
    output_csv: str,
    suffix: str,
    country_code: str = "+91",
    label: str = "school"
):
    df = pd.read_csv(input_csv)

    required_columns = ["name", "phone number"]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(
                f"Missing required column: {column}"
            )

    contacts = pd.DataFrame(
        columns=GOOGLE_CONTACT_COLUMNS
    )

    contacts["First Name"] = (
        df["name"]
        .astype(str)
        .str.strip()
        + "-"
        + suffix
    )

    contacts["Middle Name"] = ""
    contacts["Last Name"] = ""
    contacts["Phonetic First Name"] = ""
    contacts["Phonetic Middle Name"] = ""
    contacts["Phonetic Last Name"] = ""
    contacts["Name Prefix"] = ""
    contacts["Name Suffix"] = ""
    contacts["Nickname"] = ""
    contacts["File As"] = ""
    contacts["Organization Name"] = ""
    contacts["Organization Title"] = ""
    contacts["Organization Department"] = ""
    contacts["Birthday"] = ""
    contacts["Notes"] = ""
    contacts["Photo"] = ""

    contacts["Labels"] = label

    contacts["Phone 1 - Label"] = "Mobile"

    contacts["Phone 1 - Value"] = (
        country_code
        + df["phone number"]
        .astype(str)
        .str.strip()
    )

    contacts.to_csv(
        output_csv,
        index=False
    )

    print(
        f"Successfully created {output_csv}"
    )


if __name__ == "__main__":

    generate_contacts(
        input_csv="students.csv",
        output_csv="google_contacts.csv",
        suffix="1A-26-27"
    )
