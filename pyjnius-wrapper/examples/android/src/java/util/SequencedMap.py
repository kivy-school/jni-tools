from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SequencedMap"]

class SequencedMap(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/SequencedMap"
    reversed = JavaMethod("()Ljava/util/SequencedMap;")
    firstEntry = JavaMethod("()Ljava/util/Map$Entry;")
    lastEntry = JavaMethod("()Ljava/util/Map$Entry;")
    pollFirstEntry = JavaMethod("()Ljava/util/Map$Entry;")
    pollLastEntry = JavaMethod("()Ljava/util/Map$Entry;")
    putFirst = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    putLast = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    sequencedKeySet = JavaMethod("()Ljava/util/SequencedSet;")
    sequencedValues = JavaMethod("()Ljava/util/SequencedCollection;")
    sequencedEntrySet = JavaMethod("()Ljava/util/SequencedSet;")