from Elo import Elo
from itertools import combinations
from random import shuffle, choice
from MatchOutcomes import MatchOutcomes
import os
import cv2
import numpy as np
import sys
import random
from Ranker import Ranker

image_folder = "D:/Pictures/stanford-car-dataset-by-classes-folder/car_data/car_data/train/"


def getImage(directory, image_folder):
    if os.path.isdir(directory):
        images = [i for i in os.listdir(directory) if i.endswith(".jpg")]
        if not images:
            raise Exception("no images in directory")
        return os.path.join(image_folder, directory, random.choice(images))
    return os.path.join(image_folder, directory)

def showMatchImages(a,b):
    image1 = cv2.imread(getImage(a, image_folder))
    image2 = cv2.imread(getImage(b, image_folder))
    
    height1 = image1.shape[0]
    height2 = image2.shape[0]
    if (height1 > height2):
        image2 = cv2.resize(image2, (0,0), None, height1/height2, height1/height2)
    elif (height2 > height1):
        image1 = cv2.resize(image1, (0,0), None, height2/height1, height2/height1)

    height = image1.shape[0]
    if (height != 600):
        scale_factor = 600/height
        image1 = cv2.resize(image1, (0,0), None, scale_factor, scale_factor)
        image2 = cv2.resize(image2, (0,0), None, scale_factor, scale_factor)
    # image = cv2.resize(image, (0, 0), None, .25, .25)

    numpy_horizontal = np.hstack((image1, image2))
    while True:
        cv2.imshow('Numpy Horizontal', numpy_horizontal)
        res = cv2.waitKey()
        if (res == -1): sys.exit()
        if (res in [48,49,50]):
            outcomes = {
                48: (MatchOutcomes.draw,MatchOutcomes.draw),
                49: (MatchOutcomes.win, MatchOutcomes.lose),
                50: (MatchOutcomes.lose, MatchOutcomes.win)
            }
            return outcomes.get(res)


def get_match_input(match_id, a, b):
    # os.system('cls')
    while True:
        print(f"MATCH #{match_id}: {a} VS. {b}")
        result = input(f'Who won match #{match_id}? \nEnter 1 for {a} \nEnter 2 for {b} \nEnter 0 for draw\n')
        if result in ["0","1","2"]:
            break
        # os.system('cls')
        print("Please only enter 0, 1, or 2 as input.")
    # os.system('cls')
    outcomes = {
        "0": (MatchOutcomes.draw,MatchOutcomes.draw),
        "1": (MatchOutcomes.win, MatchOutcomes.lose),
        "2": (MatchOutcomes.lose, MatchOutcomes.win)
    }
    return outcomes.get(result)

ranker = Elo
assert(issubclass(Elo, Ranker))
ranker.init()

os.chdir(image_folder)
files = [i for i in os.listdir() if i.endswith(".jpg") or os.path.isdir(i)]
players = []
ratings = {}
if (os.path.exists("ratings.csv")):
    with open("ratings.csv", "r") as f:
        while True:
            line =f.readline().strip()
            if not line:
                break
            key, val = line.split(",")
            ratings[key] = val

for i in files:
    player = ranker.add_player(i, float(ratings.get(i,1000)))
    players.append(player)

prev = None
while True:
    a = choice(players)
    b = a
    while (b == a or prev == b):
        b = choice(players)
    match_id = ranker.add_match(a, b)
    res = showMatchImages(a.get_id(), b.get_id())
    ranker.end_match(match_id, *res)
    ratings[a.get_id()] = a.get_rating()
    ratings[b.get_id()] = b.get_rating()
    with open("ratings.csv", "w") as f:
        text = "\n".join((str(i) + "," + str(ratings[i])) for i in sorted(ratings, key=lambda x: int(ratings[x])))
        f.write(text)


ranker.disp_players()