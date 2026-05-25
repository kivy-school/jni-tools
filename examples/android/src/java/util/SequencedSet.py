from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SequencedSet"]

class SequencedSet(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/SequencedSet"
    reversed = JavaMethod("()Ljava/util/SequencedSet;")