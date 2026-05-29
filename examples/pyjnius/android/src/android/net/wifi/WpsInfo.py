from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WpsInfo"]

class WpsInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/WpsInfo"
    __javaconstructor__ = [("()V", False), ("(Landroid/net/wifi/WpsInfo;)V", False)]
    BSSID = JavaField("Ljava/lang/String;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    DISPLAY = JavaStaticField("I")
    INVALID = JavaStaticField("I")
    KEYPAD = JavaStaticField("I")
    LABEL = JavaStaticField("I")
    PBC = JavaStaticField("I")
    pin = JavaField("Ljava/lang/String;")
    setup = JavaField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")