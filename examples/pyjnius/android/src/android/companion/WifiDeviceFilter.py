from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiDeviceFilter"]

class WifiDeviceFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/WifiDeviceFilter"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/companion/WifiDeviceFilter$Builder"
        __javaconstructor__ = [("()V", False)]
        setNamePattern = JavaMethod("(Ljava/util/regex/Pattern;)Landroid/companion/WifiDeviceFilter$Builder;")
        setBssid = JavaMethod("(Landroid/net/MacAddress;)Landroid/companion/WifiDeviceFilter$Builder;")
        setBssidMask = JavaMethod("(Landroid/net/MacAddress;)Landroid/companion/WifiDeviceFilter$Builder;")
        build = JavaMethod("()Landroid/companion/WifiDeviceFilter;")