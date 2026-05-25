from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConnectionPoolDataSource"]

class ConnectionPoolDataSource(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/ConnectionPoolDataSource"
    getPooledConnection = JavaMultipleMethod([("()Ljavax/sql/PooledConnection;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/sql/PooledConnection;", False, False)])