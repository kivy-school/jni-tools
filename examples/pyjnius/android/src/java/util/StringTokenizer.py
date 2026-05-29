from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringTokenizer"]

class StringTokenizer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/StringTokenizer"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Z)V", False), ("(Ljava/lang/String;)V", False)]
    countTokens = JavaMethod("()I")
    hasMoreTokens = JavaMethod("()Z")
    nextToken = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("()Ljava/lang/String;", False, False)])
    hasMoreElements = JavaMethod("()Z")
    nextElement = JavaMethod("()Ljava/lang/Object;")