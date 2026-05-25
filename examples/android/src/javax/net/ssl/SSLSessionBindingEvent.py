from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLSessionBindingEvent"]

class SSLSessionBindingEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLSessionBindingEvent"
    __javaconstructor__ = [("(Ljavax/net/ssl/SSLSession;Ljava/lang/String;)V", False)]
    getName = JavaMethod("()Ljava/lang/String;")
    getSession = JavaMethod("()Ljavax/net/ssl/SSLSession;")