from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiSsid"]

class WifiSsid(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/WifiSsid"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    fromBytes = JavaStaticMethod("([B)Landroid/net/wifi/WifiSsid;")
    getBytes = JavaMethod("()[B")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")