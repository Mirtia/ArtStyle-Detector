import os

# The Crawler class checks if a directory and file exist, and creates them if they don't. 
# It's the base class for the alternative crawlers.
# Eventually, I will put more functionalities in this class, this is just not a class.
class Crawler:

    def __init__(self, output_dir: str, input_file: str, prefix: str):
      self.output_dir = self.dir_exists(output_dir, prefix)
      self.input_file = self.file_exists(input_file)
      self.prefix = prefix

    
    @staticmethod
    def dir_exists(dir: str, prefix: str="") -> str:
        """
        The `dir_exists` function checks if a directory exists and creates it if it doesn't, then returns
        the directory path.
        
        :param dir: The "dir" parameter is a string that represents the directory path where you want to
        check if a directory exists or create a new directory
        :type dir: str
        :param prefix: The "prefix" parameter is a string that is added to the directory path before
        checking if it exists. It is optional and its default value is an empty string
        :type prefix: str
        :return: the directory path.
        """
        dir_path = os.path.join(dir, prefix)
        if not os.path.exists(dir_path):
           os.makedirs(dir_path, exist_ok=True)
        return dir_path
        

    @staticmethod
    def file_exists(file: str) -> str:
        """
        The `file_exists` function checks if a file exists and returns the file name if it does,
        otherwise it raises a `FileNotFoundError` with an error message.
        
        :param file: The `file` parameter is a string that represents the file path or file name
        :type file: str
        :return: The file path is being returned.
        """
        if not os.path.isfile(file):
            raise FileNotFoundError("Error: Input file does not exist. Please provide an existing file.")
        else:
            return file 
