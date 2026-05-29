from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioDescriptor"]

class AudioDescriptor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioDescriptor"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    STANDARD_EDID = JavaStaticField("I")
    STANDARD_NONE = JavaStaticField("I")
    STANDARD_SADB = JavaStaticField("I")
    STANDARD_VSADB = JavaStaticField("I")
    getStandard = JavaMethod("()I")
    getDescriptor = JavaMethod("()[B")
    getEncapsulationType = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")