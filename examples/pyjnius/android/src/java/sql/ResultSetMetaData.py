from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResultSetMetaData"]

class ResultSetMetaData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/ResultSetMetaData"
    columnNoNulls = JavaStaticField("I")
    columnNullable = JavaStaticField("I")
    columnNullableUnknown = JavaStaticField("I")
    getColumnType = JavaMethod("(I)I")
    getSchemaName = JavaMethod("(I)Ljava/lang/String;")
    isAutoIncrement = JavaMethod("(I)Z")
    isCaseSensitive = JavaMethod("(I)Z")
    isSearchable = JavaMethod("(I)Z")
    isCurrency = JavaMethod("(I)Z")
    isNullable = JavaMethod("(I)I")
    getColumnDisplaySize = JavaMethod("(I)I")
    getColumnLabel = JavaMethod("(I)Ljava/lang/String;")
    getCatalogName = JavaMethod("(I)Ljava/lang/String;")
    getColumnTypeName = JavaMethod("(I)Ljava/lang/String;")
    isDefinitelyWritable = JavaMethod("(I)Z")
    getColumnClassName = JavaMethod("(I)Ljava/lang/String;")
    getTableName = JavaMethod("(I)Ljava/lang/String;")
    getColumnName = JavaMethod("(I)Ljava/lang/String;")
    getScale = JavaMethod("(I)I")
    isWritable = JavaMethod("(I)Z")
    getColumnCount = JavaMethod("()I")
    isSigned = JavaMethod("(I)Z")
    isReadOnly = JavaMethod("(I)Z")
    getPrecision = JavaMethod("(I)I")