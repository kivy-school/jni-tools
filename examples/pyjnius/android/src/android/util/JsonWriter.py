from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JsonWriter"]

class JsonWriter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/JsonWriter"
    __javaconstructor__ = [("(Ljava/io/Writer;)V", False)]
    beginArray = JavaMethod("()Landroid/util/JsonWriter;")
    setLenient = JavaMethod("(Z)V")
    beginObject = JavaMethod("()Landroid/util/JsonWriter;")
    endArray = JavaMethod("()Landroid/util/JsonWriter;")
    endObject = JavaMethod("()Landroid/util/JsonWriter;")
    isLenient = JavaMethod("()Z")
    name = JavaMethod("(Ljava/lang/String;)Landroid/util/JsonWriter;")
    value = JavaMultipleMethod([("(J)Landroid/util/JsonWriter;", False, False), ("(D)Landroid/util/JsonWriter;", False, False), ("(Ljava/lang/Number;)Landroid/util/JsonWriter;", False, False), ("(Ljava/lang/String;)Landroid/util/JsonWriter;", False, False), ("(Z)Landroid/util/JsonWriter;", False, False)])
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    setIndent = JavaMethod("(Ljava/lang/String;)V")
    nullValue = JavaMethod("()Landroid/util/JsonWriter;")