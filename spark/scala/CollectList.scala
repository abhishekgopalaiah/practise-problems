/*
Input:
+----+----+----+
|col1|col2|col3|
+----+----+----+
|   a|  aa|   1|
|   a|  aa|   2|
|   b|  bb|   5|
|   b|  bb|   3|
|   b|  bb|   4|
+----+----+----+

Output:
+----+----+---------+
|col1|col2|col2_list|
+----+----+---------+
|   a|  aa|   [1, 2]|
|   b|  bb|[5, 3, 4]|
*/

import org.apache.spark.sql.{SparkSession, Row}
import org.apache.spark.sql.types.{StructType, StructField, StringType, IntegerType}
import org.apache.spark.sql.functions.{collect_list}

val data = Seq(("a","aa",1),
        ("a","aa", 2),
        ("b","bb", 5),
        ("b","bb", 3),
        ("b","bb", 4))
val schema = Seq("col1", "col2", "col3")

val fields = schema.map(fieldName => StructField(fieldName, if (fieldName == "col3") IntegerType else StringType, nullable = true))
val struct = StructType(fields)

val rows = data.map { case (col1, col2, col3) => Row(col1, col2, col3) }

val df = spark.createDataFrame(spark.sparkContext.parallelize(rows), struct)
df.show()

df.createOrReplaceTempView("my_view")

spark.sql("""SELECT col1, col2, COLLECT_LIST(col3) AS col2_list
FROM my_view
GROUP BY col1, col2;""").show()
// df.groupBy("col1","col2").agg(collect_list("col3")).alias("col3").show()
