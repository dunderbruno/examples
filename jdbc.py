import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

# Configuração do Glue Context
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Configuração JDBC
jdbc_url = "jdbc:teradata://<host>:<port>/database=<db>"
jdbc_properties = {
    "user": "<seu_usuario>",
    "password": "<sua_senha>",
    "driver": "com.teradata.jdbc.TeraDriver"
}

# Query para selecionar os dados
query = "(SELECT * FROM sua_tabela WHERE condicao) AS subquery"

# Lendo os dados do Teradata
df = spark.read.format("jdbc").option("url", jdbc_url) \
    .option("dbtable", query) \
    .option("user", jdbc_properties["user"]) \
    .option("password", jdbc_properties["password"]) \
    .option("driver", jdbc_properties["driver"]) \
    .load()

# Convertendo para DynamicFrame (opcional)
dynamic_frame = DynamicFrame.fromDF(df, glueContext, "dynamic_frame")

# Mostrando os dados (para teste)
dynamic_frame.toDF().show()

job.commit()
