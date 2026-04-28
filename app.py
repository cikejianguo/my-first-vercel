import os
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

# 1. 配置数据库路径（关键：用绝对路径，避免部署出错）
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "insurance_account_final.db")

# 2. 测试数据库连接的路由（先验证能不能连上）
@app.route("/test-db")
def test_db():
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        # 读取数据库里的表，验证连接成功
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        conn.close()
        return jsonify({
            "status": "success",
            "message": "数据库连接正常",
            "tables": [table[0] for table in tables]
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"数据库连接失败：{str(e)}"
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
