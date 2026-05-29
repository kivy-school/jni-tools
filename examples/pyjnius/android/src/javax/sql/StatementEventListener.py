from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StatementEventListener"]

class StatementEventListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/StatementEventListener"
    statementClosed = JavaMethod("(Ljavax/sql/StatementEvent;)V")
    statementErrorOccurred = JavaMethod("(Ljavax/sql/StatementEvent;)V")