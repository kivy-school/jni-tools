from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StatementEvent"]

class StatementEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/StatementEvent"
    __javaconstructor__ = [("(Ljavax/sql/PooledConnection;Ljava/sql/PreparedStatement;)V", False), ("(Ljavax/sql/PooledConnection;Ljava/sql/PreparedStatement;Ljava/sql/SQLException;)V", False)]
    getSQLException = JavaMethod("()Ljava/sql/SQLException;")
    getStatement = JavaMethod("()Ljava/sql/PreparedStatement;")