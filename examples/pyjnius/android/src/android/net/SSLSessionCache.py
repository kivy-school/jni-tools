from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLSessionCache"]

class SSLSessionCache(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/SSLSessionCache"
    __javaconstructor__ = [("(Ljava/io/File;)V", False), ("(Landroid/content/Context;)V", False)]