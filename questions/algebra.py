import matplotlib
import matplotlib.pyplot as plt
from random import randint
from random import randint, shuffle
from io import BytesIO
import base64
import requests
import json

class Q_type():
    multichoice = "multichoice"
    singlechoice = "singlechoice"
    photo = "photo"
    shortreply = "shortreply"

def find_x_angel_in_qualdrilateral():
    # setting matplotlib
    font = {'family': 'normal',
            'weight': 'bold',
            'size': 16}

    matplotlib.rc('font', **font)
    matplotlib.rcParams.update({'text.color': "white",
                                'axes.labelcolor': "blue"})
    # creating the plot
    x = [1, 0.75, 2.5, 3.5]
    y = [0.5, 1.25, 2, 1]
    fig = plt.figure(figsize=(8, 8))
    plt.axis('equal')
    plt.axis('off')

    # generating the question
    question = "The diagram shows a quadrilateral. Find the value of X (NOT TO SCALE)"
    a = []
    while not(200 < sum(a) < 340):
        a = [randint(30, 150), randint(30, 150), randint(30, 150)]

    answer = 360-sum(a)
    wrongs = set()
    while len(wrongs) < 4:
        a_wrong = randint(30, 150)
        if a_wrong != answer:
            wrongs.add(a_wrong)

    options = list(wrongs)+[answer]
    text = "{q}---{a}\n\n".format(q=question, a=answer)
    for i, o in enumerate(options):
        text += "{i}) {o}\n".format(i=chr(i+65), o=o)

    # adding the texts
    plt.fill(x, y)
    plt.text(x[0], y[0]+0.1, a[0])
    plt.text(x[1]+0.1, y[1]-0.1, a[1])
    plt.text(x[2]-0.15, y[2]-0.2, a[2])
    plt.text(x[3]-0.3, y[3]+0.07, 'x')

    ax = fig.add_subplot(111)
    ax.text(0.5, 2, text, fontsize=13, color='black')

    # this is to convert the graph to the text format to send
    image = BytesIO()
    plt.savefig(image, format='png')
    image.seek(0)
    string_image1 = base64.encodebytes(image.getvalue()).decode()

    return {"photo": string_image1,
            "q_type": Q_type.singlechoice,
            "hint": [],
            "solution": []}

