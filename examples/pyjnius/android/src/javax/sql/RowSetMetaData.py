from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RowSetMetaData"]

class RowSetMetaData(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/RowSetMetaData"
    setColumnCount = JavaMethod("(I)V")
    setAutoIncrement = JavaMethod("(IZ)V")
    setCaseSensitive = JavaMethod("(IZ)V")
    setSearchable = JavaMethod("(IZ)V")
    setCurrency = JavaMethod("(IZ)V")
    setNullable = JavaMethod("(II)V")
    setSigned = JavaMethod("(IZ)V")
    setColumnDisplaySize = JavaMethod("(II)V")
    setColumnLabel = JavaMethod("(ILjava/lang/String;)V")
    setColumnName = JavaMethod("(ILjava/lang/String;)V")
    setSchemaName = JavaMethod("(ILjava/lang/String;)V")
    setPrecision = JavaMethod("(II)V")
    setScale = JavaMethod("(II)V")
    setTableName = JavaMethod("(ILjava/lang/String;)V")
    setCatalogName = JavaMethod("(ILjava/lang/String;)V")
    setColumnType = JavaMethod("(II)V")
    setColumnTypeName = JavaMethod("(ILjava/lang/String;)V")