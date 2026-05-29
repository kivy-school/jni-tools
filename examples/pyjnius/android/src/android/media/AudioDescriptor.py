from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioDescriptor"]

class AudioDescriptor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioDescriptor"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    STANDARD_EDID = JavaStaticField("I")
    STANDARD_NONE = JavaStaticField("I")
    STANDARD_SADB = JavaStaticField("I")
    STANDARD_VSADB = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getEncapsulationType = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getDescriptor = JavaMethod("()[B")
    getStandard = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")