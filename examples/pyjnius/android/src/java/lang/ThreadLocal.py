from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThreadLocal"]

class ThreadLocal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ThreadLocal"
    __javaconstructor__ = [("()V", False)]
    remove = JavaMethod("()V")
    get = JavaMethod("()Ljava/lang/Object;")
    set = JavaMethod("(Ljava/lang/Object;)V")
    withInitial = JavaStaticMethod("(Ljava/util/function/Supplier;)Ljava/lang/ThreadLocal;")