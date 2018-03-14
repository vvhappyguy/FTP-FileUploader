from jsoninfo import JsonInfo
import ftplib


def ftp_upload(ftp_obj, in_path, out_path, ftype='TXT'):
    """
    Функция для загрузки файлов на FTP-сервер
    @param ftp_obj: Объект протокола передачи файлов
    @param in_path: Путь к файлу Input
    @param out_path: Путь к файлу Output
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
    parser.files_info()

    ftp = ftplib.FTP(parser.host)
    ftp.login(parser.username, parser.password)

    for _ in range(len(parser.files)):
        ftp_upload(ftp, parser.files[_]['file_input'],parser.files[_]['file_output'],ftype='JSON')

    data = ftp.retrlines('LIST')
    print(data)
    ftp.quit()
