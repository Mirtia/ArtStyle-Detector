from imageai.Detection import ObjectDetection

class ObjectDetector:
    
    def __init__(self, input):
      self.input = input
      self.detector = ObjectDetection()
      self.detector.setModelTypeAsYOLOv3()
      self.detector.setModelPath()
      # TODO: ...

    def test(self):
      pass
    

