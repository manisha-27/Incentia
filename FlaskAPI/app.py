from flask import Flask, render_template, Response, request
import cv2
import os, sys

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def combine():
    if request.method == 'POST':
        if request.form.get('doCombine') == "Do Combine":
            pass
            ronaldo_img = cv2.imread("static/Ronaldo.png")  # Images to be added manually
            my_img = cv2.imread("static/MyImg.JPG")  # Images to be added manually
            ronaldo_img = cv2.resize(ronaldo_img, (512, 512))
            my_img = cv2.resize(my_img, (512, 512))
            final_img = cv2.add(ronaldo_img, my_img)
            cv2.imshow("FinalImage", final_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    return render_template("index.html")


if __name__ == '__main__':
    app.run()
