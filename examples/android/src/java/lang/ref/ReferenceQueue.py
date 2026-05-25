from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReferenceQueue"]

class ReferenceQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ref/ReferenceQueue"
    __javaconstructor__ = [("()V", False)]
    poll = JavaMethod("()Ljava/lang/ref/Reference;")
    remove = JavaMultipleMethod([("(J)Ljava/lang/ref/Reference;", False, False), ("()Ljava/lang/ref/Reference;", False, False)])