# Input:
# +----+----+----+
# |col1|col2|col3|
# +----+----+----+
# |   a|  aa|   1|
# |   a|  aa|   2|
# |   b|  bb|   5|
# |   b|  bb|   3|
# |   b|  bb|   4|
# +----+----+----+

# Output:
# +----+----+---------+
# |col1|col2|col2_list|
# +----+----+---------+
# |   a|  aa|   [1, 2]|
# |   b|  bb|[5, 3, 4]|
# +----+----+---------+

from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import Row

data = [("a", "aa", 1),
        ("a", "aa", 2),
        ("b", "bb", 5),
        ("b", "bb", 3),
        ("b", "bb", 4)]

# schema = ["col1", "col2", "col3"]
schema = StructType([ \
    StructField("col1",StringType(),True), \
    StructField("col2",StringType(),True), \
    StructField("col3",IntegerType(),True), \
  ])

# fields = [StructField(field_name, IntegerType() if field_name == "col3" else StringType(), True) for field_name in schema]
# struct = StructType(fields)

# rows = [Row(col1=row[0], col2=row[1], col3=row[2]) for row in data]

df = spark.createDataFrame(data, schema)
df.show()

df.createOrReplaceTempView("my_view")

spark.sql("""SELECT col1, col2, COLLECT_LIST(col3) AS col2_list
FROM my_view
GROUP BY col1, col2;""").show()

