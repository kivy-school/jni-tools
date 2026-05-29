from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLData"]

class SQLData(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/SQLData"
    getSQLTypeName = JavaMethod("()Ljava/lang/String;")
    readSQL = JavaMethod("(Ljava/sql/SQLInput;Ljava/lang/String;)V")
    writeSQL = JavaMethod("(Ljava/sql/SQLOutput;)V")