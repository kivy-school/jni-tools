from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LinkPermission"]

class LinkPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/LinkPermission"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]