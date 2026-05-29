from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConnectionPoolDataSource"]

class ConnectionPoolDataSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/ConnectionPoolDataSource"
    getLogWriter = JavaMethod("()Ljava/io/PrintWriter;")
    setLogWriter = JavaMethod("(Ljava/io/PrintWriter;)V")
    setLoginTimeout = JavaMethod("(I)V")
    getLoginTimeout = JavaMethod("()I")
    getPooledConnection = JavaMultipleMethod([("()Ljavax/sql/PooledConnection;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/sql/PooledConnection;", False, False)])
    createPooledConnectionBuilder = JavaMethod("()Ljavax/sql/PooledConnectionBuilder;")