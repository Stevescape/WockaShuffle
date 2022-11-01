def get_id(id_to_get):
    file = open("config.txt", "r")
    lines = file.readlines()
    for line in lines:
        line = line.strip("\n").split()
        if line[0].strip(":") == id_to_get:
            return " ".join(line[1:])
    # Will only reach here if the id cannot be found
    return "Error: ID could not be found"

    
