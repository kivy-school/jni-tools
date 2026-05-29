from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DhcpInfo"]

class DhcpInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/DhcpInfo"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    dns1 = JavaField("I")
    dns2 = JavaField("I")
    gateway = JavaField("I")
    ipAddress = JavaField("I")
    leaseDuration = JavaField("I")
    netmask = JavaField("I")
    serverAddress = JavaField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")