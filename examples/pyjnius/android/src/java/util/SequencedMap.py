from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SequencedMap"]

class SequencedMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/SequencedMap"
    sequencedKeySet = JavaMethod("()Ljava/util/SequencedSet;")
    sequencedValues = JavaMethod("()Ljava/util/SequencedCollection;")
    sequencedEntrySet = JavaMethod("()Ljava/util/SequencedSet;")
    putFirst = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    putLast = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    firstEntry = JavaMethod("()Ljava/util/Map$Entry;")
    lastEntry = JavaMethod("()Ljava/util/Map$Entry;")
    pollFirstEntry = JavaMethod("()Ljava/util/Map$Entry;")
    pollLastEntry = JavaMethod("()Ljava/util/Map$Entry;")
    reversed = JavaMethod("()Ljava/util/SequencedMap;")