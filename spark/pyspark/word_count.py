from pyspark.sql import SparkSession

if __name__ == "__main__":
    # Create SparkSession
    spark = SparkSession.builder \
        .appName("WordCountPython") \
        .getOrCreate()

    # Read input text file
    input_path = "input.txt"
    lines = spark.read.text(input_path)

    # Perform Word Count
    word_counts = lines \
        .selectExpr("explode(split(value, '\\s+')) as word") \
        .groupBy("word") \
        .count()

    # Display word counts
    word_counts.show()

    # Stop SparkSession
    spark.stop()
