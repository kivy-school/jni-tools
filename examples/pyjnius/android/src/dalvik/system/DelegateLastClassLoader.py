from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DelegateLastClassLoader"]

class DelegateLastClassLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/system/DelegateLastClassLoader"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/ClassLoader;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/ClassLoader;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/ClassLoader;Z)V", False)]
    loadClass = JavaMethod("(Ljava/lang/String;Z)Ljava/lang/Class;")
    getResource = JavaMethod("(Ljava/lang/String;)Ljava/net/URL;")
    getResources = JavaMethod("(Ljava/lang/String;)Ljava/util/Enumeration;")