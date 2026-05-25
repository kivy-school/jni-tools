from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JSONTokener"]

class JSONTokener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/json/JSONTokener"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    nextValue = JavaMethod("()Ljava/lang/Object;")
    nextString = JavaMethod("(C)Ljava/lang/String;")
    syntaxError = JavaMethod("(Ljava/lang/String;)Lorg/json/JSONException;")
    toString = JavaMethod("()Ljava/lang/String;")
    more = JavaMethod("()Z")
    next = JavaMultipleMethod([("()C", False, False), ("(C)C", False, False), ("(I)Ljava/lang/String;", False, False)])
    nextClean = JavaMethod("()C")
    nextTo = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(C)Ljava/lang/String;", False, False)])
    skipPast = JavaMethod("(Ljava/lang/String;)V")
    skipTo = JavaMethod("(C)C")
    back = JavaMethod("()V")
    dehexchar = JavaStaticMethod("(C)I")