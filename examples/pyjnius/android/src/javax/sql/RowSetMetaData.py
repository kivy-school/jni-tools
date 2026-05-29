from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RowSetMetaData"]

class RowSetMetaData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/RowSetMetaData"
    columnNoNulls = JavaStaticField("I")
    columnNullable = JavaStaticField("I")
    columnNullableUnknown = JavaStaticField("I")
    setCurrency = JavaMethod("(IZ)V")
    setAutoIncrement = JavaMethod("(IZ)V")
    setTableName = JavaMethod("(ILjava/lang/String;)V")
    setCatalogName = JavaMethod("(ILjava/lang/String;)V")
    setColumnType = JavaMethod("(II)V")
    setColumnTypeName = JavaMethod("(ILjava/lang/String;)V")
    setSearchable = JavaMethod("(IZ)V")
    setNullable = JavaMethod("(II)V")
    setSigned = JavaMethod("(IZ)V")
    setColumnDisplaySize = JavaMethod("(II)V")
    setColumnLabel = JavaMethod("(ILjava/lang/String;)V")
    setColumnName = JavaMethod("(ILjava/lang/String;)V")
    setSchemaName = JavaMethod("(ILjava/lang/String;)V")
    setScale = JavaMethod("(II)V")
    setCaseSensitive = JavaMethod("(IZ)V")
    setColumnCount = JavaMethod("(I)V")
    setPrecision = JavaMethod("(II)V")