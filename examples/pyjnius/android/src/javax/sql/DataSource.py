from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataSource"]

class DataSource(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/DataSource"
    getConnection = JavaMultipleMethod([("()Ljava/sql/Connection;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/sql/Connection;", False, False)])