def save_data(data, section, filename="data.txt"):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    section_data = []
    new_lines = []
    inside_section = False

    for line in lines:
        if line.strip() == f"[{section}]":
            inside_section = True
            section_data = [item.strip() for item in lines[lines.index(line)+1:] if not item.startswith("[")]
        elif inside_section and line.startswith("["):
            inside_section = False
        if not inside_section:
            new_lines.append(line)

    section_data.extend(data)
    new_lines.append(f"[{section}]\n")
    for item in section_data:
        new_lines.append(f"{item}\n")

    with open(filename, "w") as file:
        file.writelines(new_lines)

def load_data(section, filename="data.txt"):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        return []

    data = []
    inside_section = False

    for line in lines:
        if line.strip() == f"[{section}]":
            inside_section = True
        elif line.startswith("[") and inside_section:
            inside_section = False
        elif inside_section:
            data.append(line.strip())

    return data


