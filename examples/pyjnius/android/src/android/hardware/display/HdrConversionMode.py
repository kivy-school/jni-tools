from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HdrConversionMode"]

class HdrConversionMode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/display/HdrConversionMode"
    __javaconstructor__ = [("(I)V", False), ("(II)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    HDR_CONVERSION_FORCE = JavaStaticField("I")
    HDR_CONVERSION_PASSTHROUGH = JavaStaticField("I")
    HDR_CONVERSION_SYSTEM = JavaStaticField("I")
    HDR_CONVERSION_UNSUPPORTED = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getConversionMode = JavaMethod("()I")
    getPreferredHdrOutputType = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")