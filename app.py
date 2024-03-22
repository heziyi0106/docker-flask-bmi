from flask import Flask, redirect, request, render_template
import mysql.connector

app = Flask(__name__)

# MySQL 連線設定
mysql_config = {
    # 'host': '127.0.0.1', # 本地端運營時寫這行
    'host': 'mysql',  # MySQL 服務的主機名稱（這是 Docker 容器的名稱）
    'port': 3306,  # MySQL 服務的端口號（預設是 3306）
    'user': 'd_flask',
    'password': '123123',
    'database': 'docker_flask',
    'auth_plugin': 'mysql_native_password'  # 如果需要，根據 MySQL 版本選擇驗證插件
}

@app.route("/bmi", methods=['GET','POST'])
def bmi():
    if request.method == "POST":
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = round(weight / ((height/100) ** 2), 2)
        
        # 創建 MySQL 連線
        db_connection = mysql.connector.connect(**mysql_config)
        cursor = db_connection.cursor()

        # 插入新資料的 SQL 語句
        insert_query = "INSERT INTO user_bmi (weight, height, bmi) VALUES (%s, %s, %s)"
        # 執行 SQL 語句
        cursor.execute(insert_query, (weight, height, bmi))
        # 提交事務
        db_connection.commit()
        # 關閉游標和連線
        cursor.close()
        db_connection.close()

        return redirect("/show")
    else:
        return render_template("index.html")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/show')
def show():
    # 創建 MySQL 連線
    db_connection = mysql.connector.connect(**mysql_config)
    cursor = db_connection.cursor()

    # 執行 SQL 查詢
    cursor.execute("SELECT * FROM user_bmi")
    data = cursor.fetchall()

    # 關閉游標和連線
    cursor.close()
    db_connection.close()

    return render_template('result.html', data=data)

@app.route('/test')
def test():
    # 創建 MySQL 連線
    db_connection = mysql.connector.connect(**mysql_config)
    cursor = db_connection.cursor()

    # 更新访问次数的 SQL 语句
    update_query = "UPDATE site_visits SET visit_count = visit_count + 1 WHERE id = 1"
    cursor.execute(update_query)
    db_connection.commit()

    # 查询最新的访问次数
    select_query = "SELECT visit_count FROM site_visits WHERE id = 1"
    cursor.execute(select_query)
    visit_count = cursor.fetchone()[0]

    # 关闭游标和连接
    cursor.close()
    db_connection.close()

    # return f'The website has been visited {visit_count} times.' 
    return f'本網站已有 {visit_count} 次點擊.' 
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
