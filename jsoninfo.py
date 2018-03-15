from json import load


class JsonInfo():
    """
    Class for Parsing information from config.json

    Variables:
    files -- list for writing all files
    host -- host-address(string)
    username -- username(string) default="anonymous"
    passwrod -- password(string) default="anonumous@"
    port -- port(string) default="21"
    state -- state of connection data default="True"
    """

    def __init__(self):
        self.files = []
        self.host = ""
        self.username = "anonymous"
        self.password = "anonymous@"
        self.port = "21"
        self.state = True

        filename = 'config.json'
        with open(filename) as f:
            pop_data = load(f)
        for pop_dict in pop_data:
            try:
                self.host = pop_dict['host']
            except KeyError:
                print("ERROR - No host-address")
                self.state = False
            try:
                self.username = pop_dict['username']
            except KeyError:
                print("Using default value for username.")
            try:
                self.password = pop_dict['password']
            except KeyError:
                print("Using default value for password.")
            try:
                self.port = pop_dict['port']
                if (self.port == "") or (self.port == " "):
                    self.port = "21"
            except KeyError:
                print("Using default value for port.")
            if self.state:
                for f_counter in range(len(pop_dict['files'])):
                    tmp_file_input = pop_dict['files'][f_counter]['input_dest']
                    tmp_file_output = pop_dict['files'][f_counter]['output_dest']
                    tmp_file_extention = tmp_file_output[tmp_file_output.find(
                        '.')+1:len(tmp_file_output)]
                    tmp_file = {
                        "file_input": tmp_file_input,
                        "file_output": tmp_file_output,
                        "file_extention": tmp_file_extention
                    }
                    self.files.append(tmp_file)

    def unique_list(self):
        """Fucntion for removing repeating elements in file list"""
        if self.state:
            c1, c2 = 0, 0
            for i in self.files:
                c1 += 1
                for j in self.files:
                    c2 += 1
                    if (i == j) and (c2 != c1):
                        self.files.pop()
                c2 = 0

    def connection_info(self):
        """Printing Connection Info function"""
        if self.state:
            print("\nHost: " + self.host
                  + "\nUsername: " + self.username
                  + "\nPassword: " + self.password
                  + "\nPort: " + self.port)

    def files_info(self):
        """Printing Files Info function"""
        if self.state:
            print("\nFiles(" + str(len(self.files)) + ") INFO:")
            for _ in range(len(self.files)):
                print(self.files[_])
            print("\n")
