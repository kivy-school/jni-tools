from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyedFrequencyCap"]

class KeyedFrequencyCap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/KeyedFrequencyCap"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getMaxCount = JavaMethod("()I")
    getAdCounterKey = JavaMethod("()I")
    getInterval = JavaMethod("()Ljava/time/Duration;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/common/KeyedFrequencyCap$Builder"
        __javaconstructor__ = [("(IILjava/time/Duration;)V", False)]
        setAdCounterKey = JavaMethod("(I)Landroid/adservices/common/KeyedFrequencyCap$Builder;")
        setInterval = JavaMethod("(Ljava/time/Duration;)Landroid/adservices/common/KeyedFrequencyCap$Builder;")
        setMaxCount = JavaMethod("(I)Landroid/adservices/common/KeyedFrequencyCap$Builder;")
        build = JavaMethod("()Landroid/adservices/common/KeyedFrequencyCap;")