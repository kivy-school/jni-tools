from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JsonReader"]

class JsonReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/JsonReader"
    __javaconstructor__ = [("(Ljava/io/Reader;)V", False)]
    beginArray = JavaMethod("()V")
    nextLong = JavaMethod("()J")
    nextName = JavaMethod("()Ljava/lang/String;")
    nextNull = JavaMethod("()V")
    nextString = JavaMethod("()Ljava/lang/String;")
    setLenient = JavaMethod("(Z)V")
    skipValue = JavaMethod("()V")
    beginObject = JavaMethod("()V")
    endArray = JavaMethod("()V")
    endObject = JavaMethod("()V")
    isLenient = JavaMethod("()Z")
    nextBoolean = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hasNext = JavaMethod("()Z")
    close = JavaMethod("()V")
    peek = JavaMethod("()Landroid/util/JsonToken;")
    nextDouble = JavaMethod("()D")
    nextInt = JavaMethod("()I")