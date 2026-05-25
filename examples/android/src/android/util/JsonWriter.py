from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JsonWriter"]

class JsonWriter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/JsonWriter"
    __javaconstructor__ = [("(Ljava/io/Writer;)V", False)]
    setIndent = JavaMethod("(Ljava/lang/String;)V")
    setLenient = JavaMethod("(Z)V")
    isLenient = JavaMethod("()Z")
    beginArray = JavaMethod("()Landroid/util/JsonWriter;")
    endArray = JavaMethod("()Landroid/util/JsonWriter;")
    beginObject = JavaMethod("()Landroid/util/JsonWriter;")
    endObject = JavaMethod("()Landroid/util/JsonWriter;")
    name = JavaMethod("(Ljava/lang/String;)Landroid/util/JsonWriter;")
    value = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/util/JsonWriter;", False, False), ("(Z)Landroid/util/JsonWriter;", False, False), ("(D)Landroid/util/JsonWriter;", False, False), ("(J)Landroid/util/JsonWriter;", False, False), ("(Ljava/lang/Number;)Landroid/util/JsonWriter;", False, False)])
    nullValue = JavaMethod("()Landroid/util/JsonWriter;")
    flush = JavaMethod("()V")
    close = JavaMethod("()V")