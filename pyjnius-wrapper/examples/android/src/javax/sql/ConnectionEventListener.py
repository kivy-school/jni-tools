from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConnectionEventListener"]

class ConnectionEventListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/sql/ConnectionEventListener"
    connectionClosed = JavaMethod("(Ljavax/sql/ConnectionEvent;)V")
    connectionErrorOccurred = JavaMethod("(Ljavax/sql/ConnectionEvent;)V")