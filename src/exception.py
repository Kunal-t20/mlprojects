import sys #sys module in Python is a built-in module that provides access to system-specific parameters and functions. It allows interaction with the Python interpreter and its runtime environment.

def error_message_detail(error,error_detail:sys):
    file_name=exc_tb.tb_frame.f_code.co_filename
    _,_,exc_tb=error_detail.exc_info()
    error_message='error occured in python script name[{0}] line number[{1}] error message[{2}]'.format(
    file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_deatil=error_detail)
    
    def __str__(self):
        return self.error_message
    
