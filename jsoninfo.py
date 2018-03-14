from json import load


class JsonInfo():
    """
    Class for Parsing information from config.json
    """

    def __init__(self):
        self.files = []
        self.host = ""
        self.username = ""
        self.password = ""

        filename = 'config.json'
        with open(filename) as f:
            pop_data = load(f)
        for pop_dict in pop_data:
            if pop_dict['host'] != '':
                self.host = pop_dict['host']
            if pop_dict['username'] != '':
                self.username = pop_dict['username']
            if pop_dict['password'] != '':
                self.password = pop_dict['password']
            if pop_dict['files'] != '':
                for f_counter in range(len(pop_dict['files'])):
                    tmp_file_input = pop_dict['files'][f_counter]['input_dest']
                    tmp_file_output = pop_dict['files'][f_counter]['output_dest']
                    tmp_file_extention = tmp_file_output[tmp_file_output.find(
                        '.'):len(tmp_file_output)]
                    tmp_file = {
                        "file_input": tmp_file_input,
                        "file_output": tmp_file_output,
                        "file_extention": tmp_file_extention
                    }
                    self.files.append(tmp_file)

    def connection_info(self):
        print("\nHost: " + self.host
              + "\nUsername: " + self.username
              + "\nPassword: " + self.password)

    def files_info(self):
        print("\nFiles(" + str(len(self.files)) + ") INFO:")
        for _ in range(len(self.files)):
            print(self.files[_])


t = JsonInfo()
t.connection_info()
t.files_info()
