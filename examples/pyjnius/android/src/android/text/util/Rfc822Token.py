from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Rfc822Token"]

class Rfc822Token(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/util/Rfc822Token"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    quoteNameIfNecessary = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    setAddress = JavaMethod("(Ljava/lang/String;)V")
    quoteName = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    quoteComment = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    setName = JavaMethod("(Ljava/lang/String;)V")
    getAddress = JavaMethod("()Ljava/lang/String;")
    getComment = JavaMethod("()Ljava/lang/String;")
    setComment = JavaMethod("(Ljava/lang/String;)V")