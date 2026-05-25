from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClassValue"]

class ClassValue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ClassValue"
    __javaconstructor__ = [("()V", False)]
    computeValue = JavaMethod("(Ljava/lang/Class;)Ljava/lang/Object;")
    get = JavaMethod("(Ljava/lang/Class;)Ljava/lang/Object;")
    remove = JavaMethod("(Ljava/lang/Class;)V")