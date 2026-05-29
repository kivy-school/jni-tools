from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataSource"]

class DataSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/DataSource"
    getConnection = JavaMultipleMethod([("()Ljava/sql/Connection;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/sql/Connection;", False, False)])
    getLogWriter = JavaMethod("()Ljava/io/PrintWriter;")
    setLogWriter = JavaMethod("(Ljava/io/PrintWriter;)V")
    setLoginTimeout = JavaMethod("(I)V")
    getLoginTimeout = JavaMethod("()I")
    createConnectionBuilder = JavaMethod("()Ljava/sql/ConnectionBuilder;")