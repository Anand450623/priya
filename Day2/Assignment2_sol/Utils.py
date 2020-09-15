def read_file_contents(path):

    data = list()
    buffer = str()
    with open(path, "r") as f:
        for line in f:
            if not line.isspace():
                if line.strip()[-1] == ';':
                    data.append(buffer + line.strip())
                else:
                    buffer += line.strip()+"\n"

    return data
