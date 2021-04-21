import numpy as np
from cv2 import cv2


def classify(path):
    img = cv2.imread(path)

    rows = open('model/synset_words.txt').read().strip().split("\n")

    net = cv2.dnn.readNetFromCaffe('model/bvlc_googlenet.prototxt', 'model/bvlc_googlenet.caffemodel')
    blob = cv2.dnn.blobFromImage(img, 1, (224, 224))
    net.setInput(blob)
    output = net.forward()

    index = np.argsort(output[0])[::-1]
    result = rows[index[0]]

    #print('\n\n\nThis is {}. I am {:.0f}% sure.\n\n\n' .format(result[10:], output[0][index[0]]*100))

    return result[10:], output[0][index[0]]*100
