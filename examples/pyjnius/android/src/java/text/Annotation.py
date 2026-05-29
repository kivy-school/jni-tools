from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Annotation"]

class Annotation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/Annotation"
    __javaconstructor__ = [("(Ljava/lang/Object;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    getValue = JavaMethod("()Ljava/lang/Object;")