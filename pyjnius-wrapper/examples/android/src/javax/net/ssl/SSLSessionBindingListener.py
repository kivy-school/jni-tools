from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLSessionBindingListener"]

class SSLSessionBindingListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLSessionBindingListener"
    valueBound = JavaMethod("(Ljavax/net/ssl/SSLSessionBindingEvent;)V")
    valueUnbound = JavaMethod("(Ljavax/net/ssl/SSLSessionBindingEvent;)V")