from flask import Flask, jsonify, request
import mariadb
import os

app = Flask(__name__)


@app.route("/", methods=["GET"])
def return_info():
    try:
        conn = mariadb.connect(
            user=os.environ.get("USER"),
            password=os.environ.get("PSWD"),  # сменить
            host=os.environ.get("DB_HOST"),
            port=3306,
            database=os.environ.get("DATABASE")
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        exit(1)

    cursor = conn.cursor()
    get_all_data = "SELECT * FROM Users;"
    cursor.execute(get_all_data)
    data = cursor.fetchall()
    # print(data)
    return jsonify(data, 200)


@app.route("/health", methods=["GET"])
def get_status():
    return jsonify({"status": "OK"}, 200)


if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0")
