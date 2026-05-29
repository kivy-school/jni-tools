from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Stack"]

class Stack(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Stack"
    __javaconstructor__ = [("()V", False)]
    push = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    pop = JavaMethod("()Ljava/lang/Object;")
    peek = JavaMethod("()Ljava/lang/Object;")
    empty = JavaMethod("()Z")
    search = JavaMethod("(Ljava/lang/Object;)I")