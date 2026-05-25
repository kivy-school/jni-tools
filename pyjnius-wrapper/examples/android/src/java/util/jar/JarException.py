from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JarException"]

class JarException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/jar/JarException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]