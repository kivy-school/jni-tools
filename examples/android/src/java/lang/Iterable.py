from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Iterable"]

class Iterable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Iterable"
    iterator = JavaMethod("()Ljava/util/Iterator;")
    forEach = JavaMethod("(Ljava/util/function/Consumer;)V")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")