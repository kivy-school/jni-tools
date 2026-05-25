from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AvailableNetworkInfo"]

class AvailableNetworkInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/AvailableNetworkInfo"
    __javaconstructor__ = [("(IILjava/util/List;Ljava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PRIORITY_HIGH = JavaStaticField("I")
    PRIORITY_LOW = JavaStaticField("I")
    PRIORITY_MED = JavaStaticField("I")
    getSubId = JavaMethod("()I")
    getPriority = JavaMethod("()I")
    getMccMncs = JavaMethod("()Ljava/util/List;")
    getBands = JavaMethod("()Ljava/util/List;")
    getRadioAccessSpecifiers = JavaMethod("()Ljava/util/List;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/AvailableNetworkInfo/Builder"
        __javaconstructor__ = [("(I)V", False)]
        setPriority = JavaMethod("(I)Landroid/telephony/AvailableNetworkInfo$Builder;")
        setMccMncs = JavaMethod("(Ljava/util/List;)Landroid/telephony/AvailableNetworkInfo$Builder;")
        setRadioAccessSpecifiers = JavaMethod("(Ljava/util/List;)Landroid/telephony/AvailableNetworkInfo$Builder;")
        build = JavaMethod("()Landroid/telephony/AvailableNetworkInfo;")