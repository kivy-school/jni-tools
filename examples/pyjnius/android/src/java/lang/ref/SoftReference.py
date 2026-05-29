from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SoftReference"]

class SoftReference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ref/SoftReference"
    __javaconstructor__ = [("(Ljava/lang/Object;)V", False), ("(Ljava/lang/Object;Ljava/lang/ref/ReferenceQueue;)V", False)]
    get = JavaMethod("()Ljava/lang/Object;")