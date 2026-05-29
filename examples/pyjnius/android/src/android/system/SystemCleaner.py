from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SystemCleaner"]

class SystemCleaner(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/system/SystemCleaner"
    cleaner = JavaStaticMethod("()Ljava/lang/ref/Cleaner;")