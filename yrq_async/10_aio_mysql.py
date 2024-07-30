import asyncio
import aiomysql
async def execute():
#网络IO操作：连接MySQL
conn=await aiomysql.connect(host='127.0.0.1',port=3306,user='root',password='123',
db='mysq1',)
#网络IO操作：创建CURSOR
cur=await conn.cursor()
#网络IO操作：执行SQL
await cur . execute ( " SELECT Host , User FROM user " )
#网络IO操作：获取SQL结果
result=await cur.fetchall()
print(result)
#网络IO操作：关闭链接
await cur.close()
conn.close()
asyncio.run(execute())