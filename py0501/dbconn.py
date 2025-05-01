# 오라클 db연결 pip install oracledb
import oracledb as ora

## 오라클 접속 - 외부연결이라 에러 났을때 예외처리
def connections():
    try: conn = ora.connect(user='ora_user', password='1111', dsn='localhost:1521/xe')
    except Exception as e: print(e)
    return conn