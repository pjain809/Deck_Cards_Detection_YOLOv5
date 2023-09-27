
import sys


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg = f"Error occurred in {file_name} at line no. {exc_tb.tb_lineno}.\n" \
                f"Error message : {str(error)}"

    return error_msg


class AppException(Exception):
    def __init__(self, error_msg, error_detail):
        super().__init__(error_msg)
        self.error_msg = error_message_detail(error_msg, error_detail)

    def __str__(self):
        return self.error_msg
