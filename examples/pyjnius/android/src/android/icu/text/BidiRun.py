from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BidiRun"]

class BidiRun(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/BidiRun"
    getDirection = JavaMethod("()B")
    getStart = JavaMethod("()I")
    getLimit = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getLength = JavaMethod("()I")
    getEmbeddingLevel = JavaMethod("()B")
    isEvenRun = JavaMethod("()Z")
    isOddRun = JavaMethod("()Z")