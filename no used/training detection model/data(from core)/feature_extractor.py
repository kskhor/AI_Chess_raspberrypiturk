# unused - Defines an abstract FeatureExtractor class, which other feature extractors (like RawPixelsExtractor) inherit from.Used for converting chessboard images into numerical features for ML models.
#can be used in training model(If you are training a new model and need a structured way to extract features.)
class FeatureExtractor(object):
    def extract_features(self, square):
        raise NotImplementedError
