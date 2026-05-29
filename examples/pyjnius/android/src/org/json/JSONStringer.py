from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JSONStringer"]

class JSONStringer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/json/JSONStringer"
    __javaconstructor__ = [("()V", False)]
    endArray = JavaMethod("()Lorg/json/JSONStringer;")
    endObject = JavaMethod("()Lorg/json/JSONStringer;")
    value = JavaMultipleMethod([("(Ljava/lang/Object;)Lorg/json/JSONStringer;", False, False), ("(D)Lorg/json/JSONStringer;", False, False), ("(Z)Lorg/json/JSONStringer;", False, False), ("(J)Lorg/json/JSONStringer;", False, False)])
    toString = JavaMethod("()Ljava/lang/String;")
    array = JavaMethod("()Lorg/json/JSONStringer;")
    key = JavaMethod("(Ljava/lang/String;)Lorg/json/JSONStringer;")
    object = JavaMethod("()Lorg/json/JSONStringer;")