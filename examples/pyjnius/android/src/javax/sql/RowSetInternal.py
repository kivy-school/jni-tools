from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RowSetInternal"]

class RowSetInternal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/RowSetInternal"
    getConnection = JavaMethod("()Ljava/sql/Connection;")
    getOriginalRow = JavaMethod("()Ljava/sql/ResultSet;")
    setMetaData = JavaMethod("(Ljavax/sql/RowSetMetaData;)V")
    getOriginal = JavaMethod("()Ljava/sql/ResultSet;")
    getParams = JavaMethod("()[Ljava/lang/Object;")