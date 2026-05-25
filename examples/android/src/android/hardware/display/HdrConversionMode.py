from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HdrConversionMode"]

class HdrConversionMode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/display/HdrConversionMode"
    __javaconstructor__ = [("(II)V", False), ("(I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    HDR_CONVERSION_FORCE = JavaStaticField("I")
    HDR_CONVERSION_PASSTHROUGH = JavaStaticField("I")
    HDR_CONVERSION_SYSTEM = JavaStaticField("I")
    HDR_CONVERSION_UNSUPPORTED = JavaStaticField("I")
    getConversionMode = JavaMethod("()I")
    getPreferredHdrOutputType = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")