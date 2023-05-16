import os, openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def openai_app():
    if request.method == "POST":
        category = request.form["category"]
        number = request.form["number"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(number, category),
            temperature=0.5,
            max_tokens=50,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return redirect(url_for("openai_app", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("openai_app.html", result=result)


def generate_prompt(number, category):
    return """Recommend the best {} {} movies to watch:""".format(number,
        category.capitalize()
    )


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5050, debug=True)
