from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThreadLocal"]

class ThreadLocal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ThreadLocal"
    __javaconstructor__ = [("()V", False)]
    initialValue = JavaMethod("()Ljava/lang/Object;")
    withInitial = JavaStaticMethod("(Ljava/util/function/Supplier;)Ljava/lang/ThreadLocal;")
    get = JavaMethod("()Ljava/lang/Object;")
    set = JavaMethod("(Ljava/lang/Object;)V")
    remove = JavaMethod("()V")