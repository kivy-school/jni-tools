from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyedFrequencyCap"]

class KeyedFrequencyCap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/KeyedFrequencyCap"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getAdCounterKey = JavaMethod("()I")
    getMaxCount = JavaMethod("()I")
    getInterval = JavaMethod("()Ljava/time/Duration;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/common/KeyedFrequencyCap/Builder"
        __javaconstructor__ = [("(IILjava/time/Duration;)V", False)]
        setAdCounterKey = JavaMethod("(I)Landroid/adservices/common/KeyedFrequencyCap$Builder;")
        setMaxCount = JavaMethod("(I)Landroid/adservices/common/KeyedFrequencyCap$Builder;")
        setInterval = JavaMethod("(Ljava/time/Duration;)Landroid/adservices/common/KeyedFrequencyCap$Builder;")
        build = JavaMethod("()Landroid/adservices/common/KeyedFrequencyCap;")