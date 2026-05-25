from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BaseDexClassLoader"]

class BaseDexClassLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/system/BaseDexClassLoader"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/io/File;Ljava/lang/String;Ljava/lang/ClassLoader;)V", False)]
    findClass = JavaMethod("(Ljava/lang/String;)Ljava/lang/Class;")
    findResource = JavaMethod("(Ljava/lang/String;)Ljava/net/URL;")
    findResources = JavaMethod("(Ljava/lang/String;)Ljava/util/Enumeration;")
    findLibrary = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getPackage = JavaMethod("(Ljava/lang/String;)Ljava/lang/Package;")
    toString = JavaMethod("()Ljava/lang/String;")