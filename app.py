# 这是Vercel能识别的标准Flask入口文件
from flask import Flask
import os
import sqlite3

# 核心：必须在文件最顶层定义 app，不能缩进！
app = Flask(__name__)

# 数据库路径配置
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "insurance_account_final.db")

# 首页测试路由
@app.route('/')
def home():
    return "✅ 项目部署成功！数据库已就绪"

# 数据库测试路由
@app.route('/test-db')
def test_db():
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        conn.close()
        return {
            "状态": "连接成功",
            "数据库表": [t[0] for t in tables]
        }
    except Exception as e:
        return {"错误": str(e)}

# 本地运行用，Vercel自动识别上面的 app
if __name__ == '__main__':
    app.run()
