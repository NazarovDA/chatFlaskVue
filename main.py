#coding: UTF8

from flask import Flask, request
from flask.json import jsonify

app = Flask(__name__)



class Message:
    def __init__(self, text:str, author:str, time:int):
        self.text:str = text
        self.author:str = author
        self.time:int = time
        self.id:int = self.set_id()

    def __str__(self):
        return f"{self.text} {self.author} {self.time}"
        

    def set_id(self)->int:
        return messages.__len__()+1

    def to_json(self):
        return {
            "id": self.id,
            "time": self.time,
            "text": self.text,
            "author": self.author
        }

messages: list[Message] = []    


@app.route("/get_message", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        data = request.get_json()

        message = Message(
                text=data["text"],
                author=data["author"],
                time=data["time"]
            )

        messages.append(
            message
        )

        return jsonify(message.to_json())

    elif request.method == "GET":

        args = request.args
        print(args)
        id:int = int(args.get("from_id")) if args.get("from_id") else 0
        
        return jsonify(
            [message.to_json() for message in messages[id:]] if id > 0 else [message.to_json() for message in messages]
        )


@app.after_request
def after_request(answer):
    answer.headers["Access-Control-Allow-Origin"] = "*"
    answer.headers["Access-Control-Allow-Headers"] = "*"
    answer.headers["Access-Control-Allow-Methods"] = "*"
    return answer

if __name__ == "__main__":
    app.run()