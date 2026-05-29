from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HandshakeCompletedListener"]

class HandshakeCompletedListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/HandshakeCompletedListener"
    handshakeCompleted = JavaMethod("(Ljavax/net/ssl/HandshakeCompletedEvent;)V")