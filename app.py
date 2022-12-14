from flask import Flask, redirect, request, render_template
import chat
from time import gmtime, strftime

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def home():
    return render_template('index.html')

@app.route(f'/jarvis', methods =["GET", "POST"])
def search():
    query = request.args.get("question")
    query = query.lower()
    print(query)
    reply = chat.RISHABH(query=query)
    data_save_q = []
    data_save_q.append(query)
    data_save_r = []
    data_save_r.append(reply)
    data_save_t = []
    data_saved = {
        "Hi": "Hey"
    }

    data_saved[query] = reply
    data_save_t.append(strftime("%H:%M"))

    data = {
        "query": query,
        "reply": reply,
        "chat_time": strftime("%H:%M"),
        "data_save_q": data_save_q,
        "data_save_r": data_save_r,
        "data_save_t": data_save_t,
        "data_saved": data_saved
    }
    return render_template('test.html',data=data)

if __name__ == '__main__':
   app.run(debug=True)