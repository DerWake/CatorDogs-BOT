import time
import os
import random
import json

import nn

predictor = nn.Predictor()


def load(img_path):
	item = predictor.get_image_item(img_path)
	return item

