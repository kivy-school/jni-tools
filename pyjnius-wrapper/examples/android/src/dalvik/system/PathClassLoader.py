from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PathClassLoader"]

class PathClassLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/system/PathClassLoader"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/ClassLoader;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/ClassLoader;)V", False)]