from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MalformedURLException"]

class MalformedURLException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/MalformedURLException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]