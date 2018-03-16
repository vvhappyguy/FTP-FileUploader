# -*- coding: utf-8 -*-
import threading
from jsoninfo import JsonInfo
import ftplib
import sys


class myThread(threading.Thread):
    def __init__(self,threadID):
        self.threadID = threadID
        """FTP-connection"""
        try:
            self.ftp = ftplib.FTP(host=parser.host, acct=parser.port)
        except TimeoutError as ftp_error:
            print("[FTP-ERROR][{}]: {}".format(self.threadID,ftp_error))
            sys.exit()
        except ftplib.error_proto as ftp_error:
            print("[FTP-ERROR][{}]: {}".format(self.threadID,ftp_error))
            sys.exit()
        except ftplib.error_reply as ftp_error:
            print("[FTP-ERROR][{}]: {}".format(self.threadID,ftp_error))
            sys.exit()
        except ftplib.error_temp as ftp_error:
            print("[FTP-ERROR][{}]: {}".format(self.threadID,ftp_error))
            sys.exit()
        else:
            print("[LOG][{}]: Good Host-address".format(self.threadID))
        try:
            self.ftp.login(user=parser.username, passwd=parser.password)
        except ftplib.error_perm as ftp_error:
            self.ftp.close()
            print("[FTP-ERROR][{}]: {}".format(self.threadID,ftp_error))
            sys.exit()
        except ftplib.error_proto as ftp_error:
            print("[FTP-ERROR][{}]: {}".format(self.threadID,ftp_error))
            sys.exit()
        except ftplib.error_reply as ftp_error:
            print("[FTP-ERROR][{}]: {}".format(self.threadID,ftp_error))
            sys.exit()
        except ftplib.error_temp as ftp_error:
            print("[FTP-ERROR][{}]: {}".format(self.threadID,ftp_error))
            sys.exit()
        else:
            print("[LOG][{}]: Connected successfully".format(self.threadID))
        
        
        """Thread Data"""
        self.in_dir = parser.files[threadID]['file_input']
        self.out_dir = parser.files[threadID]['file_output']
        self.file_exp = parser.files[threadID]['file_extention']
        threading.Thread.__init__(self)
    def run(self):
        try:
            ftp_upload(self.ftp,self.in_dir, self.out_dir,self.file_exp)
        except ftplib.error_perm as ftp_error:
            print("[FTP-ERROR][{}]: {}".format(self.threadID,ftp_error))
        except FileNotFoundError as in_error:
            print("[LOCAL-ERROR][{}]: {}".format(self.threadID,in_error))
        except ftplib.error_proto as ftp_error:
            print("[FTP-ERROR][{}]: {}".format(self.threadID,ftp_error))
        except ftplib.error_reply as ftp_error:
            print("[FTP-ERROR][{}]: {}".format(self.threadID,ftp_error))
        except ftplib.error_temp as ftp_error:
            print("[FTP-ERROR][{}]: {}".format(self.threadID,ftp_error))
        else:
            print("[LOG][{}]: Has been uploaded.".format(self.threadID))
        finally:
            self.ftp.close()
            print("[LOG][{}]: FTP-Connection closed.".format(self.threadID))

def ftp_upload(ftp_obj, in_path, out_path, ftype):
    """
    Function for uploading files to FTP-server
    @param ftp_obj: FTP-object protocol 
    @param in_path: Destination file (from)
    @param out_path: Destination file (to)
    """
    if ftype == 'txt':
        with open(in_path) as fobj:
            ftp_obj.storlines('STOR ' + out_path, fobj)
    else:
        with open(in_path, 'rb') as fobj:
            ftp_obj.storbinary('STOR ' + out_path, fobj, 1024)

if __name__ == "__main__":
    parser = JsonInfo()
    parser.connection_info()
    parser.unique_list()
    parser.files_info()

    if parser.state:
        threads = []
        for i in range(len(parser.files)):
            thread = myThread(i)
            thread.start()
            threads.append(thread)
        
        for t in threads:
            t.join()
    
    """For checking files on FTP-server"""
   #ftp = ftplib.FTP(host=parser.host, user=parser.username,
    #                     passwd=parser.password, acct=parser.port)
"""
    print("\n")
    data = ftp.retrlines('LIST')
    print("\n" + data)
"""
    