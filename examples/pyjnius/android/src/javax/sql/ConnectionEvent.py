from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConnectionEvent"]

class ConnectionEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/ConnectionEvent"
    __javaconstructor__ = [("(Ljavax/sql/PooledConnection;Ljava/sql/SQLException;)V", False), ("(Ljavax/sql/PooledConnection;)V", False)]
    getSQLException = JavaMethod("()Ljava/sql/SQLException;")