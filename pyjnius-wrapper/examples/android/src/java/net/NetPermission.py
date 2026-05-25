from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetPermission"]

class NetPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/NetPermission"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]