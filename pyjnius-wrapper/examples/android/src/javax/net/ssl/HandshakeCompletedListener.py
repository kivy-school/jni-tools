from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HandshakeCompletedListener"]

class HandshakeCompletedListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/HandshakeCompletedListener"
    handshakeCompleted = JavaMethod("(Ljavax/net/ssl/HandshakeCompletedEvent;)V")