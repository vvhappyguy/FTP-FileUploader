import json


class FTP_Copy():
    def __init__(self):
        filename = 'config.json'
        with open(filename) as f:
            pop_data = json.load(f)
        for pop_dict in pop_data:
            if pop_dict['host'] != '':
                self.host = pop_dict['host']
            if pop_dict['username'] != '':
                self.username = pop_dict['username']
            if pop_dict['password'] != '':
                self.password = pop_dict['password']
            if pop_dict['files'] != '':
                self.files = []
                for f_counter in range(len(pop_dict['files'])):
                    tmp_file_input = pop_dict['files'][f_counter]['input_dest']
                    tmp_file_output = pop_dict['files'][f_counter]['output_dest']
                    tmp_file = {
                        'file_input': tmp_file_input,
                        'file_output': tmp_file_output
                    }
                    self.files.append(tmp_file)

    def connection_info(self):
        print("\nHost: " + self.host
              + "\nUsername: " + self.username
              + "\nPassword: " + self.password)

    def files_info(self):
        print("\nFiles INFO:")
        for _ in range(len(self.files)):
            print(self.files[_])


my_ftp_copy = FTP_Copy()
my_ftp_copy.connection_info()
my_ftp_copy.files_info()
