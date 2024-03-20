import org.apache.spark.sql.SparkSession

object WordCount{
  def main(args: Array[String]): Unit = {
    // Create SparkSession
    val spark = SparkSession.builder()
      .appName("WordCountScala")
      .master("local[*]")
      .getOrCreate()

    // Read input text file
    val inputPath = "input.txt"
    val lines = spark.read.textFile(inputPath)

    // Perform Word Count
    val wordCounts = lines
      .flatMap(_.split("\\s+"))
      .map(word => (word.toLowerCase, 1))
      .reduceByKey(_ + _)

    // Display word counts
    wordCounts.collect().foreach(println)

    // Stop SparkSession
    spark.stop()
  }
}
