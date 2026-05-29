from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Stack"]

class Stack(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Stack"
    __javaconstructor__ = [("()V", False)]
    empty = JavaMethod("()Z")
    peek = JavaMethod("()Ljava/lang/Object;")
    search = JavaMethod("(Ljava/lang/Object;)I")
    push = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    pop = JavaMethod("()Ljava/lang/Object;")