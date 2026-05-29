from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Object"]

class Object(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Object"
    __javaconstructor__ = [("()V", False)]
    getClass = JavaMethod("()Ljava/lang/Class;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    clone = JavaMethod("()Ljava/lang/Object;")
    toString = JavaMethod("()Ljava/lang/String;")
    notify = JavaMethod("()V")
    notifyAll = JavaMethod("()V")
    wait = JavaMultipleMethod([("(J)V", False, False), ("(JI)V", False, False), ("()V", False, False)])
    finalize = JavaMethod("()V")