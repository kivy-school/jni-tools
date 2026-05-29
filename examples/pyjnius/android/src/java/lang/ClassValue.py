from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClassValue"]

class ClassValue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ClassValue"
    remove = JavaMethod("(Ljava/lang/Class;)V")
    get = JavaMethod("(Ljava/lang/Class;)Ljava/lang/Object;")