from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PooledConnection"]

class PooledConnection(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/PooledConnection"
    getConnection = JavaMethod("()Ljava/sql/Connection;")
    close = JavaMethod("()V")
    addConnectionEventListener = JavaMethod("(Ljavax/sql/ConnectionEventListener;)V")
    removeConnectionEventListener = JavaMethod("(Ljavax/sql/ConnectionEventListener;)V")
    addStatementEventListener = JavaMethod("(Ljavax/sql/StatementEventListener;)V")
    removeStatementEventListener = JavaMethod("(Ljavax/sql/StatementEventListener;)V")