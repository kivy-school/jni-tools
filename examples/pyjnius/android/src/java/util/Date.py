from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Date"]

class Date(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Date"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(IIIIII)V", False), ("(IIIII)V", False), ("()V", False), ("(J)V", False), ("(III)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    compareTo = JavaMultipleMethod([("(Ljava/util/Date;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])
    from = JavaStaticMethod("(Ljava/time/Instant;)Ljava/util/Date;")
    parse = JavaStaticMethod("(Ljava/lang/String;)J")
    getMonth = JavaMethod("()I")
    before = JavaMethod("(Ljava/util/Date;)Z")
    after = JavaMethod("(Ljava/util/Date;)Z")
    getDate = JavaMethod("()I")
    setDate = JavaMethod("(I)V")
    setMonth = JavaMethod("(I)V")
    getHours = JavaMethod("()I")
    setHours = JavaMethod("(I)V")
    getMinutes = JavaMethod("()I")
    setMinutes = JavaMethod("(I)V")
    setSeconds = JavaMethod("(I)V")
    setYear = JavaMethod("(I)V")
    getDay = JavaMethod("()I")
    toLocaleString = JavaMethod("()Ljava/lang/String;")
    toGMTString = JavaMethod("()Ljava/lang/String;")
    getTimezoneOffset = JavaMethod("()I")
    getTime = JavaMethod("()J")
    getYear = JavaMethod("()I")
    getSeconds = JavaMethod("()I")
    toInstant = JavaMethod("()Ljava/time/Instant;")
    UTC = JavaStaticMethod("(IIIIII)J")
    setTime = JavaMethod("(J)V")