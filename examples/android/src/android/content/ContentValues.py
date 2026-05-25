from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentValues"]

class ContentValues(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ContentValues"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(Landroid/content/ContentValues;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TAG = JavaStaticField("Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    put = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;Ljava/lang/Byte;)V", False, False), ("(Ljava/lang/String;Ljava/lang/Short;)V", False, False), ("(Ljava/lang/String;Ljava/lang/Integer;)V", False, False), ("(Ljava/lang/String;Ljava/lang/Long;)V", False, False), ("(Ljava/lang/String;Ljava/lang/Float;)V", False, False), ("(Ljava/lang/String;Ljava/lang/Double;)V", False, False), ("(Ljava/lang/String;Ljava/lang/Boolean;)V", False, False), ("(Ljava/lang/String;[B)V", False, False)])
    putAll = JavaMethod("(Landroid/content/ContentValues;)V")
    putNull = JavaMethod("(Ljava/lang/String;)V")
    size = JavaMethod("()I")
    isEmpty = JavaMethod("()Z")
    remove = JavaMethod("(Ljava/lang/String;)V")
    clear = JavaMethod("()V")
    containsKey = JavaMethod("(Ljava/lang/String;)Z")
    get = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    getAsString = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getAsLong = JavaMethod("(Ljava/lang/String;)Ljava/lang/Long;")
    getAsInteger = JavaMethod("(Ljava/lang/String;)Ljava/lang/Integer;")
    getAsShort = JavaMethod("(Ljava/lang/String;)Ljava/lang/Short;")
    getAsByte = JavaMethod("(Ljava/lang/String;)Ljava/lang/Byte;")
    getAsDouble = JavaMethod("(Ljava/lang/String;)Ljava/lang/Double;")
    getAsFloat = JavaMethod("(Ljava/lang/String;)Ljava/lang/Float;")
    getAsBoolean = JavaMethod("(Ljava/lang/String;)Ljava/lang/Boolean;")
    getAsByteArray = JavaMethod("(Ljava/lang/String;)[B")
    valueSet = JavaMethod("()Ljava/util/Set;")
    keySet = JavaMethod("()Ljava/util/Set;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")