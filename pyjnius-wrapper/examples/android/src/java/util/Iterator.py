from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Iterator"]

class Iterator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Iterator"
    hasNext = JavaMethod("()Z")
    next = JavaMethod("()Ljava/lang/Object;")
    remove = JavaMethod("()V")
    forEachRemaining = JavaMethod("(Ljava/util/function/Consumer;)V")