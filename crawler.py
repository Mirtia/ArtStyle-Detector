import os

# The Crawler class checks if a directory and file exist, and creates them if they don't. 
# It's the base class for the alternative crawlers.
class Crawler:

    def __init__(self, output_dir, input_file, prefix):
      self.output_dir = self.dir_exists(output_dir, prefix)
      self.input_file = self.file_exists(input_file)
      self.prefix = prefix

    @staticmethod
    def dir_exists(dir, prefix=""):
        """
        This is a static method in Python that checks if a directory exists and creates it if it
        doesn't.
        
        :param dir: The directory path where the new directory will be created
        :param prefix: The prefix parameter is an optional string that can be added to the directory
        path. It is used to create a subdirectory within the main directory specified by the dir
        parameter. If no prefix is provided, the function will simply create the directory specified by
        the dir parameter
        :return: the directory path that was created or already existed.
        """
        dir_path = os.path.join(dir, prefix)
        if not os.path.exists(dir_path):
           os.makedirs(dir_path, exist_ok=True)
        return dir_path
        

    @staticmethod
    def file_exists(file):
        """
        This is a static method in Python that checks if a file exists and raises an error if it
        doesn't.
        
        :param file: The parameter "file" is a string representing the file path of the file being
        checked for existence
        :return: the input file if it exists.
        """
        if not os.path.isfile(file):
            raise FileNotFoundError("Error: Input file does not exist. Please provide an existing file.")
        else:
            return file 

    # Crawling time / status