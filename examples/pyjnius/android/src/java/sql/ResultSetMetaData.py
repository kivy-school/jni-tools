from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResultSetMetaData"]

class ResultSetMetaData(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/ResultSetMetaData"
    columnNoNulls = JavaStaticField("I")
    columnNullable = JavaStaticField("I")
    columnNullableUnknown = JavaStaticField("I")
    getColumnCount = JavaMethod("()I")
    isAutoIncrement = JavaMethod("(I)Z")
    isCaseSensitive = JavaMethod("(I)Z")
    isSearchable = JavaMethod("(I)Z")
    isCurrency = JavaMethod("(I)Z")
    isNullable = JavaMethod("(I)I")
    isSigned = JavaMethod("(I)Z")
    getColumnDisplaySize = JavaMethod("(I)I")
    getColumnLabel = JavaMethod("(I)Ljava/lang/String;")
    getColumnName = JavaMethod("(I)Ljava/lang/String;")
    getSchemaName = JavaMethod("(I)Ljava/lang/String;")
    getPrecision = JavaMethod("(I)I")
    getScale = JavaMethod("(I)I")
    getTableName = JavaMethod("(I)Ljava/lang/String;")
    getCatalogName = JavaMethod("(I)Ljava/lang/String;")
    getColumnType = JavaMethod("(I)I")
    getColumnTypeName = JavaMethod("(I)Ljava/lang/String;")
    isReadOnly = JavaMethod("(I)Z")
    isWritable = JavaMethod("(I)Z")
    isDefinitelyWritable = JavaMethod("(I)Z")
    getColumnClassName = JavaMethod("(I)Ljava/lang/String;")