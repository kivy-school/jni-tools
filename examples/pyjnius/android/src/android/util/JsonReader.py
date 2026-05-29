from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JsonReader"]

class JsonReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/JsonReader"
    __javaconstructor__ = [("(Ljava/io/Reader;)V", False)]
    setLenient = JavaMethod("(Z)V")
    isLenient = JavaMethod("()Z")
    beginArray = JavaMethod("()V")
    endArray = JavaMethod("()V")
    beginObject = JavaMethod("()V")
    endObject = JavaMethod("()V")
    hasNext = JavaMethod("()Z")
    peek = JavaMethod("()Landroid/util/JsonToken;")
    nextName = JavaMethod("()Ljava/lang/String;")
    nextString = JavaMethod("()Ljava/lang/String;")
    nextBoolean = JavaMethod("()Z")
    nextNull = JavaMethod("()V")
    nextDouble = JavaMethod("()D")
    nextLong = JavaMethod("()J")
    nextInt = JavaMethod("()I")
    close = JavaMethod("()V")
    skipValue = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")