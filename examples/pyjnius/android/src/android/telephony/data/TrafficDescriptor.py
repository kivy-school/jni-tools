from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrafficDescriptor"]

class TrafficDescriptor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/data/TrafficDescriptor"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getDataNetworkName = JavaMethod("()Ljava/lang/String;")
    getOsAppId = JavaMethod("()[B")
    describeContents = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/data/TrafficDescriptor/Builder"
        __javaconstructor__ = [("()V", False)]
        setDataNetworkName = JavaMethod("(Ljava/lang/String;)Landroid/telephony/data/TrafficDescriptor$Builder;")
        setOsAppId = JavaMethod("([B)Landroid/telephony/data/TrafficDescriptor$Builder;")
        build = JavaMethod("()Landroid/telephony/data/TrafficDescriptor;")