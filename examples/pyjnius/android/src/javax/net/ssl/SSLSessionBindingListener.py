from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLSessionBindingListener"]

class SSLSessionBindingListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLSessionBindingListener"
    valueBound = JavaMethod("(Ljavax/net/ssl/SSLSessionBindingEvent;)V")
    valueUnbound = JavaMethod("(Ljavax/net/ssl/SSLSessionBindingEvent;)V")