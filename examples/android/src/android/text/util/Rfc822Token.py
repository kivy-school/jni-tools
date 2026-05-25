from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Rfc822Token"]

class Rfc822Token(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/util/Rfc822Token"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    getName = JavaMethod("()Ljava/lang/String;")
    getAddress = JavaMethod("()Ljava/lang/String;")
    getComment = JavaMethod("()Ljava/lang/String;")
    setName = JavaMethod("(Ljava/lang/String;)V")
    setAddress = JavaMethod("(Ljava/lang/String;)V")
    setComment = JavaMethod("(Ljava/lang/String;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    quoteNameIfNecessary = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    quoteName = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    quoteComment = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")