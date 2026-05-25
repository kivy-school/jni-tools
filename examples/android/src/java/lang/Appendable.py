from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Appendable"]

class Appendable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Appendable"
    append = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Ljava/lang/Appendable;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/lang/Appendable;", False, False), ("(C)Ljava/lang/Appendable;", False, False)])