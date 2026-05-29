from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLData"]

class SQLData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/SQLData"
    getSQLTypeName = JavaMethod("()Ljava/lang/String;")
    readSQL = JavaMethod("(Ljava/sql/SQLInput;Ljava/lang/String;)V")
    writeSQL = JavaMethod("(Ljava/sql/SQLOutput;)V")