import oracledb as ora

## db접속정보 oracle > 사용자 마우스 오른쪽 > 속성에서 사용자정보, 세부정보
def connections():
    conn = ora.connect(user="ora_user", password="1111", dsn="localhost:1521/xe")
    return conn