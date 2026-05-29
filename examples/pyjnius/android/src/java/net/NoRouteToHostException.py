from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NoRouteToHostException"]

class NoRouteToHostException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/NoRouteToHostException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("()V", False)]