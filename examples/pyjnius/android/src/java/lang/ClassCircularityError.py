from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClassCircularityError"]

class ClassCircularityError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ClassCircularityError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]