def read_url_file(filename):
    links = []
    with open(filename) as file:
        line = file.readline()
        while line:
            links.append(line.replace('\n', ''))
            line = file.readline()

    return links


