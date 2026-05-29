from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BaseDexClassLoader"]

class BaseDexClassLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/system/BaseDexClassLoader"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/io/File;Ljava/lang/String;Ljava/lang/ClassLoader;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    findLibrary = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")