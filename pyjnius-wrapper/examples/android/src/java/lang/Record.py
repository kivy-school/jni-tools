from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Record"]

class Record(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Record"
    __javaconstructor__ = [("()V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")