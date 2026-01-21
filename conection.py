import mysql.connector
from mysql.connector import pooling

mydb = mysql.connector.connect(
  host="srv847.hstgr.io",
  user="u112589075_auto_project",
  password="#Ap949521",
  database='u112589075_db_auto_prod'
)

try:
      # 2. Crie o pool de conexões
  pool_conexoes = pooling.MySQLConnectionPool(
      pool_name="meu_app_pool",
      pool_size=5,  # Comece com 5, ajuste se necessário
      host="srv847.hstgr.io",
      user="u112589075_auto_project",
      password="#Ap949521",
      database='u112589075_db_auto_prod'
  )

except mysql.connector.Error as err:
  print(f"Erro ao criar o pool de conexões: {err}")
  pool_conexoes = None # Garante que o pool não será usado se falhar
  

mycursor = mydb.cursor()