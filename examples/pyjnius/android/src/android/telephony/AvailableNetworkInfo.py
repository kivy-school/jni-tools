from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AvailableNetworkInfo"]

class AvailableNetworkInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/AvailableNetworkInfo"
    __javaconstructor__ = [("(IILjava/util/List;Ljava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PRIORITY_HIGH = JavaStaticField("I")
    PRIORITY_LOW = JavaStaticField("I")
    PRIORITY_MED = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getBands = JavaMethod("()Ljava/util/List;")
    getSubId = JavaMethod("()I")
    getMccMncs = JavaMethod("()Ljava/util/List;")
    getRadioAccessSpecifiers = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getPriority = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/AvailableNetworkInfo$Builder"
        __javaconstructor__ = [("(I)V", False)]
        setMccMncs = JavaMethod("(Ljava/util/List;)Landroid/telephony/AvailableNetworkInfo$Builder;")
        setRadioAccessSpecifiers = JavaMethod("(Ljava/util/List;)Landroid/telephony/AvailableNetworkInfo$Builder;")
        setPriority = JavaMethod("(I)Landroid/telephony/AvailableNetworkInfo$Builder;")
        build = JavaMethod("()Landroid/telephony/AvailableNetworkInfo;")