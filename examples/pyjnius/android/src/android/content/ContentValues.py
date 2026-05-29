from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentValues"]

class ContentValues(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ContentValues"
    __javaconstructor__ = [("(I)V", False), ("(Landroid/content/ContentValues;)V", False), ("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TAG = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    remove = JavaMethod("(Ljava/lang/String;)V")
    size = JavaMethod("()I")
    put = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/Float;)V", False, False), ("(Ljava/lang/String;Ljava/lang/Integer;)V", False, False), ("(Ljava/lang/String;Ljava/lang/Long;)V", False, False), ("(Ljava/lang/String;Ljava/lang/Boolean;)V", False, False), ("(Ljava/lang/String;Ljava/lang/Double;)V", False, False), ("(Ljava/lang/String;Ljava/lang/Byte;)V", False, False), ("(Ljava/lang/String;[B)V", False, False), ("(Ljava/lang/String;Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;Ljava/lang/Short;)V", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    clear = JavaMethod("()V")
    isEmpty = JavaMethod("()Z")
    get = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    putAll = JavaMethod("(Landroid/content/ContentValues;)V")
    keySet = JavaMethod("()Ljava/util/Set;")
    containsKey = JavaMethod("(Ljava/lang/String;)Z")
    getAsBoolean = JavaMethod("(Ljava/lang/String;)Ljava/lang/Boolean;")
    getAsByte = JavaMethod("(Ljava/lang/String;)Ljava/lang/Byte;")
    getAsByteArray = JavaMethod("(Ljava/lang/String;)[B")
    getAsDouble = JavaMethod("(Ljava/lang/String;)Ljava/lang/Double;")
    getAsFloat = JavaMethod("(Ljava/lang/String;)Ljava/lang/Float;")
    getAsInteger = JavaMethod("(Ljava/lang/String;)Ljava/lang/Integer;")
    getAsLong = JavaMethod("(Ljava/lang/String;)Ljava/lang/Long;")
    getAsShort = JavaMethod("(Ljava/lang/String;)Ljava/lang/Short;")
    getAsString = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    putNull = JavaMethod("(Ljava/lang/String;)V")
    valueSet = JavaMethod("()Ljava/util/Set;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")