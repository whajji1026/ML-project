import sys 
'''sys module contains methods and variables 
for modifying many elements of the Python Runtime 
Environment. It allows us to access parameters and 
functionalities specific to the system.'''


def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Erroor occured in python script name [{0}] line [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message
    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message





