from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StatementEventListener"]

class StatementEventListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/StatementEventListener"
    statementClosed = JavaMethod("(Ljavax/sql/StatementEvent;)V")
    statementErrorOccurred = JavaMethod("(Ljavax/sql/StatementEvent;)V")