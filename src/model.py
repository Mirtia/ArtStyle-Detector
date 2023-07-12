import os
import shutil
from imageai.Classification.Custom import ClassificationModelTrainer, CustomImageClassification

# The `StyleModel` class is a Python class that provides methods for creating a directory structure
# for training and testing data, training a model using the ResNet50 architecture, and classifying
# images using a pre-trained ResNet50 model.
class StyleModel:

    TRAIN_SET_SIZE = 1000
    TEST_SET_SIZE = 500

    def __init__(self, input_dir: str, output_dir: str, skip: bool=True):
        self.input_dir = input_dir
        self.output_dir = output_dir
        if not skip:
            self.__create_dir_structure()
        self.model_trainer = ClassificationModelTrainer()

    def __create_dir_structure(self):
        """
        The function creates a directory structure for training and testing data, and moves files from
        the input directory to the appropriate train and test directories based on a specified train set
        size and test set size.
        """
        os.makedirs(self.output_dir, exist_ok=True)
        train_dir = os.path.join(self.output_dir, "train")
        test_dir = os.path.join(self.output_dir, "test")
        os.makedirs(train_dir, exist_ok=True)
        os.makedirs(test_dir, exist_ok=True)

        train_dir_category = None
        test_dir_category = None
        for root, dirs, files in os.walk(self.input_dir):
            # If there is a list of directories and not a list of files then its a top level directory
            if dirs and not files and root is not self.input_dir:
                count = 0
                train_dir_category = os.path.join(train_dir, os.path.basename(root))
                test_dir_category = os.path.join(test_dir, os.path.basename(root))
                os.makedirs(train_dir_category, exist_ok=True)
                os.makedirs(test_dir_category, exist_ok=True)
            else:
                for file in files:
                    # If maximum count is reached then continue with next category
                    # TODO: Images may not be enough, proportional splitting?
                    if count <=  self.TRAIN_SET_SIZE:
                        shutil.move(os.path.join(root, file), os.path.join(train_dir_category, file))
                    elif count <= self.TRAIN_SET_SIZE + self.TEST_SET_SIZE:
                        shutil.move(os.path.join(root, file), os.path.join(test_dir_category, file))
                    else:
                        break
                    count += 1

    def train(self):
        """
        The function trains a model using the ResNet50 architecture with a specified number of
        experiments and batch size.
        See https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Classification/CUSTOMTRAINING.md
        """
        self.model_trainer.setModelTypeAsResNet50()
        self.model_trainer.setDataDirectory(self.output_dir)
        self.model_trainer.trainModel(num_experiments=100, batch_size=32)

    def __get_paths(self, path: str) -> tuple:
        """
        The function `__get_paths` takes a directory path as input and returns the paths of a model file
        and a JSON file within that directory.
        
        :param path: The `path` parameter is a string that represents the directory path where the files
        are located
        :type path: str
        :return: a tuple containing the paths of the model file and the JSON file.
        """
        model_path, json_path = None, None
        if os.path.isdir(path):
            files = os.listdir(path)
            for file in files:
                file_path = os.path.join(path, file)
                if os.path.isfile(file_path) and file_path.endswith(".json"):
                    json_path = file_path
                else:
                    model_path = file_path
        return model_path, json_path


    def classify(self, input_img: str):
        """
        The `classify` function uses a pre-trained ResNet50 model to classify an input image and prints
        the top 10 predictions along with their probabilities.
        
        :param input_img: The input_img parameter is the image that you want to classify. It should be
        the path to the image file or a PIL image object
        """
        prediction = CustomImageClassification()
        prediction.setModelTypeAsResNet50()

        model_path, json_path = self.__get_paths(os.path.join(self.output_dir, "models"))
       
        prediction.setModelPath(model_path)
        prediction.setJsonPath(json_path)
        prediction.loadModel()
        predictions, probabilities = prediction.classifyImage(input_img, result_count=10)

        print(f"Predictions for image: {input_img}")
        print("============================================================")
        for eachPrediction, eachProbability in zip(predictions, probabilities):
            print(eachPrediction + " : " + str(eachProbability))
        print("============================================================")