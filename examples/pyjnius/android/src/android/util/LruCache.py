from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LruCache"]

class LruCache(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/LruCache"
    __javaconstructor__ = [("(I)V", False)]
    createCount = JavaMethod("()I")
    evictAll = JavaMethod("()V")
    evictionCount = JavaMethod("()I")
    hitCount = JavaMethod("()I")
    missCount = JavaMethod("()I")
    putCount = JavaMethod("()I")
    remove = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    size = JavaMethod("()I")
    maxSize = JavaMethod("()I")
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    toString = JavaMethod("()Ljava/lang/String;")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    trimToSize = JavaMethod("(I)V")
    snapshot = JavaMethod("()Ljava/util/Map;")
    resize = JavaMethod("(I)V")