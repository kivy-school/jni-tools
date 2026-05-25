from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TelephonyNetworkSpecifier"]

class TelephonyNetworkSpecifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/TelephonyNetworkSpecifier"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getSubscriptionId = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/TelephonyNetworkSpecifier/Builder"
        __javaconstructor__ = [("()V", False)]
        setSubscriptionId = JavaMethod("(I)Landroid/net/TelephonyNetworkSpecifier$Builder;")
        build = JavaMethod("()Landroid/net/TelephonyNetworkSpecifier;")