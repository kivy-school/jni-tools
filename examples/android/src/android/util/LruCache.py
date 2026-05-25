from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LruCache"]

class LruCache(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/LruCache"
    __javaconstructor__ = [("(I)V", False)]
    resize = JavaMethod("(I)V")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    trimToSize = JavaMethod("(I)V")
    remove = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    entryRemoved = JavaMethod("(ZLjava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)V")
    create = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    sizeOf = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)I")
    evictAll = JavaMethod("()V")
    size = JavaMethod("()I")
    maxSize = JavaMethod("()I")
    hitCount = JavaMethod("()I")
    missCount = JavaMethod("()I")
    createCount = JavaMethod("()I")
    putCount = JavaMethod("()I")
    evictionCount = JavaMethod("()I")
    snapshot = JavaMethod("()Ljava/util/Map;")
    toString = JavaMethod("()Ljava/lang/String;")