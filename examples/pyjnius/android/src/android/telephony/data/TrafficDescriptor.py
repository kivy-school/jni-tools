from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrafficDescriptor"]

class TrafficDescriptor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/data/TrafficDescriptor"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDataNetworkName = JavaMethod("()Ljava/lang/String;")
    getOsAppId = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/data/TrafficDescriptor$Builder"
        __javaconstructor__ = [("()V", False)]
        setOsAppId = JavaMethod("([B)Landroid/telephony/data/TrafficDescriptor$Builder;")
        setDataNetworkName = JavaMethod("(Ljava/lang/String;)Landroid/telephony/data/TrafficDescriptor$Builder;")
        build = JavaMethod("()Landroid/telephony/data/TrafficDescriptor;")