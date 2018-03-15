from jsoninfo import JsonInfo
import ftplib


def ftp_upload(ftp_obj, in_path, out_path, ftype='TXT'):
    """
    Function for uploading files to FTP-server
    @param ftp_obj: FTP-object protocol 
    @param in_path: Destination file (from)
    @param out_path: Destination file (to)
    """

    if ftype == 'TXT':
        with open(in_path) as fobj:
            ftp.storlines('STOR ' + out_path, fobj)
    else:
        with open(in_path, 'rb') as fobj:
            ftp.storbinary('STOR ' + out_path, fobj, 1024)


if __name__ == '__main__':
    parser = JsonInfo()
    parser.connection_info()
    parser.unique_list()
    parser.files_info()
    if parser.state:
        ftp = ftplib.FTP(host=parser.host, user=parser.username,
                         passwd=parser.password, acct=parser.port)

        for _ in range(len(parser.files)):
            ftp_upload(ftp, parser.files[_]['file_input'], parser.files[_]
                       ['file_output'], ftype=parser.files[_]['file_extention'])

        ftp.quit()
