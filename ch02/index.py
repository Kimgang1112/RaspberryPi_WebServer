from flask import Flask, render_template, redirect, url_for, request
import pymysql




app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")








@app.route("/submit", methods=["POST"])

def save_db():
    data = request.get_json()
    print(data.get("value"))
    conn = pymysql.connect(host='localhost', user='root', password='q1w2e3', database='Study')
    cursor = conn.cursor()
    cursor.execute(f"insert into numcount(num) values ({data.get("value")})")
    conn.commit()

    conn.close()
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)


