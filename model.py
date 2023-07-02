import os
import shutil
from imageai.Classification.Custom import ClassificationModelTrainer

class StyleModel:

    TRAIN_SET_SIZE = 1000
    TEST_SET_SIZE = 500

    def __init__(self, input_dir, output_dir, skip=True):
        self.input_dir = input_dir
        self.output_dir = output_dir
        if not skip:
            self.__create_dir_structure()
        self.model_trainer = ClassificationModelTrainer()

    def __create_dir_structure(self):
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

    def train_model(self):
        # https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Classification/CUSTOMTRAINING.md
        self.model_trainer.setModelTypeAsResNet50()
        self.model_trainer.setDataDirectory(self.output_dir)
        self.model_trainer.trainModel(num_experiments=100, batch_size=32)
