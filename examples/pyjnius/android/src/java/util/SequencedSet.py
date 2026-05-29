from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SequencedSet"]

class SequencedSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/SequencedSet"
    reversed = JavaMultipleMethod([("()Ljava/util/SequencedSet;", False, False), ("()Ljava/util/SequencedCollection;", False, False)])