from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLSessionCache"]

class SSLSessionCache(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/SSLSessionCache"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Ljava/io/File;)V", False)]