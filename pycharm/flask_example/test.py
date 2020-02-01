from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/mypage')
def mypage():
   return 'This is My Page!'

## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
   # rank_give로 클라이언트가 준 rank을 가져오기 & 숫자변환
   rank_receive = request.form['rank_give']
   rank_receive = int(rank_receive)
   print(rank_receive)

   # star_give로 클라이언트가 준 star를 가져오기 & 숫자변환
   star_receive = request.form['star_give']
   star_receive = int(star_receive)
   print(star_receive)

   # 해당 순위의 영화를 받은 score로 업데이트 해주기
   db.movies.update_one({'rank': rank_receive}, {'$set': {'star': star_receive}})

@app.route('/test', methods=['GET'])
def test_get():
   # rank_give로 클라이언트가 준 rank을 가져오기
   rank_receive = request.args.get('rank_give')

   rank_receive = int(rank_receive)

   # rank의 값이 받은 rank와 일치하는 document 찾기 & _id 값은 출력에서 제외하기
   movie_info = db.movies.find_one({'rank': rank_receive}, {'_id': 0})

   print(movie_info)

   # info라는 키 값으로 영화정보 내려주기
   return jsonify({'result': 'success', 'info': movie_info})

@app.route('/new', methods=['POST'])
def new_post():
   rank_receive = int(request.form['rank_give'])
   star_receive = request.form['star_give']
   title_receive = request.form['title_give']

   db.movies.insert_one({'rank': rank_receive, 'title':title_receive, 'star': star_receive})

   return jsonify({'result': 'success'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)