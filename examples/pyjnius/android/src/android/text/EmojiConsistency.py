from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EmojiConsistency"]

class EmojiConsistency(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/EmojiConsistency"
    getEmojiConsistencySet = JavaStaticMethod("()Ljava/util/Set;")