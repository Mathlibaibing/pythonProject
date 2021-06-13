import redis

pool = redis.ConnectionPool(host="192.168.124.129",password="",decode_response = True) #实现一个连接池
conn = redis.StrictRedis(connection_pool=pool)
conn.lpush("key3",23,446,67567,3242)
print(conn.lpop("key3"))
