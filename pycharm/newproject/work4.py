from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

movie_info = db.movies.find_one({'title' : '사운드 오브 뮤직'})
print(movie_info['star'])
target_star = movie_info['star']

print(list(db.movies.find({'star' : target_star})))

stars = list(db.movies.find({'star' : target_star}))

for i in stars :
    print(i['title'])

# 생김새
db.movies.update_many({'star' : target_star},{ '$set': {'star' :0}})

# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# user = db.users.find_one({'name':'bobby'})
# print (user)