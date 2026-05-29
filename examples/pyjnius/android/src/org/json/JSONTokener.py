from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JSONTokener"]

class JSONTokener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/json/JSONTokener"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    nextString = JavaMethod("(C)Ljava/lang/String;")
    dehexchar = JavaStaticMethod("(C)I")
    nextClean = JavaMethod("()C")
    nextTo = JavaMultipleMethod([("(C)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])
    skipPast = JavaMethod("(Ljava/lang/String;)V")
    skipTo = JavaMethod("(C)C")
    syntaxError = JavaMethod("(Ljava/lang/String;)Lorg/json/JSONException;")
    toString = JavaMethod("()Ljava/lang/String;")
    next = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("()C", False, False), ("(C)C", False, False)])
    nextValue = JavaMethod("()Ljava/lang/Object;")
    back = JavaMethod("()V")
    more = JavaMethod("()Z")