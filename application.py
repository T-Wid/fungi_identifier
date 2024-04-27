from Classify import classify, main
from flask import Flask, render_template, request

application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def gfg():
    if request.method == "POST":
        gill_color = int(request.form.get("gill_color"))
        population = int(request.form.get("population"))
        spore_color = int(request.form.get("spore_color"))
        bruises = int(request.form.get("bruises"))
        stalk_root = int(request.form.get("stalkRoot"))

        user_selection = main(gill_color, population, spore_color, bruises, stalk_root)
        message = classify(user_selection)
        return message

    return render_template("gfg.html")


if __name__ == '__main__':
    application.run()
