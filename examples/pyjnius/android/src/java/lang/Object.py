from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Object"]

class Object(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Object"
    __javaconstructor__ = [("()V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getClass = JavaMethod("()Ljava/lang/Class;")
    notify = JavaMethod("()V")
    notifyAll = JavaMethod("()V")
    wait = JavaMultipleMethod([("(J)V", False, False), ("(JI)V", False, False), ("()V", False, False)])