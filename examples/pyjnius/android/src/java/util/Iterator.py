from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Iterator"]

class Iterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Iterator"
    remove = JavaMethod("()V")
    forEachRemaining = JavaMethod("(Ljava/util/function/Consumer;)V")
    hasNext = JavaMethod("()Z")
    next = JavaMethod("()Ljava/lang/Object;")