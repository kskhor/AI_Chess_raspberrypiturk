#unused -  Extracts raw pixel features, but we are using square_color_detector instead.
#can be used in training model(Convert images into numerical data using RawPixelsExtracto)
import numpy as np
from raspberryturk.core.data.feature_extractor import FeatureExtractor
from sklearn.preprocessing import normalize

class RawPixelsExtractor(FeatureExtractor):
    def extract_features(self, square):
        return (square.raw_img.flatten() / 127.5) - 1.0
