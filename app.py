import os

import openai
from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        years = request.form["years"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(years),
            temperature=0.9,
            max_tokens=1000,
            n=12,
        )
        return redirect(url_for("index", result=response.choices[0].text,
                                 result1=response.choices[1].text,
                                 result2=response.choices[2].text,
                                 result3=response.choices[3].text,
                                 result4=response.choices[4].text,
                                 result5=response.choices[5].text,
                                 result6=response.choices[6].text,
                                 result7=response.choices[7].text,
                                 result8=response.choices[8].text,
                                 result9=response.choices[9].text,
                                 result10=response.choices[10].text,
                                 result11=response.choices[11].text))

    result = request.args.get("result")
    result1 = request.args.get("result1")
    result2 = request.args.get("result2")
    result3 = request.args.get("result3")
    result4 = request.args.get("result4")
    result5 = request.args.get("result5")
    result6 = request.args.get("result6")
    result7 = request.args.get("result7")
    result8 = request.args.get("result8")
    result9 = request.args.get("result9")
    result10 = request.args.get("result10")
    result11 = request.args.get("result11")
    
    return render_template("index.html", result=result,
                            result1=result1,
                            result2=result2,
                            result3=result3,
                            result4=result4,
                            result5=result5,
                            result6=result6,
                            result7=result7,
                            result8=result8,
                            result9=result9,
                            result10=result10,
                            result11=result11,)


def generate_prompt(years):
    return """Suggest an exam problem for a computer scienctist based on their experience, that will take no longer than 5 minutes to complete.

Years: 1
Question: Write a Program to Find Size of Int Float Double and Char data types.
Years: 2
Question: Explain serialization and deserialization.
Years: 3
Question: Write a program to create a doubly linked list and implement operations like add, remove and search.
Years: {}
Question:""".format(
        years.capitalize()
    )


