from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BidiRun"]

class BidiRun(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/BidiRun"
    getStart = JavaMethod("()I")
    getLimit = JavaMethod("()I")
    getLength = JavaMethod("()I")
    getEmbeddingLevel = JavaMethod("()B")
    isOddRun = JavaMethod("()Z")
    isEvenRun = JavaMethod("()Z")
    getDirection = JavaMethod("()B")
    toString = JavaMethod("()Ljava/lang/String;")