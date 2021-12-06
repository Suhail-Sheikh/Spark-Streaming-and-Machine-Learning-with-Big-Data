

from pyspark.ml import Pipeline
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql.types import StructType

# Create a local StreamingContext with two working thread and batch interval of 1 second
sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 1)

# Define schema of the csv
userSchema = StructType().add("Subject", "string").add("Message","string").add("Spam/Ham","string")

# Read CSV files from set path
dfCSV = spark.readStream.option("sep", ";").option("header", "true").schema(userSchema).csv("/home/pes1ug19cs192/Desktop/train.csv")


to_print = spark.sql("select * from dfCSV where Spam/Ham is spam")
query = totalSalary.writeStream.outputMode("complete").format("console").start()

query.awaitTermination()


