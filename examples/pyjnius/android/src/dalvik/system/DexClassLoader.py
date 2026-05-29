from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DexClassLoader"]

class DexClassLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/system/DexClassLoader"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/ClassLoader;)V", False)]