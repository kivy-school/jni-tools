from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RowSetInternal"]

class RowSetInternal(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/RowSetInternal"
    getParams = JavaMethod("()[Ljava/lang/Object;")
    getConnection = JavaMethod("()Ljava/sql/Connection;")
    setMetaData = JavaMethod("(Ljavax/sql/RowSetMetaData;)V")
    getOriginal = JavaMethod("()Ljava/sql/ResultSet;")
    getOriginalRow = JavaMethod("()Ljava/sql/ResultSet;")