from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TetheringInterface"]

class TetheringInterface(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/TetheringInterface"
    __javaconstructor__ = [("(ILjava/lang/String;)V", False), ("(ILjava/lang/String;Landroid/net/wifi/SoftApConfiguration;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getType = JavaMethod("()I")
    getInterface = JavaMethod("()Ljava/lang/String;")
    getSoftApConfiguration = JavaMethod("()Landroid/net/wifi/SoftApConfiguration;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")