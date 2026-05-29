from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AmbientBacklightMetadata"]

class AmbientBacklightMetadata(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/quality/AmbientBacklightMetadata"
    __javaconstructor__ = [("(Ljava/lang/String;IIIII[I)V", False)]
    ALGORITHM_NONE = JavaStaticField("I")
    ALGORITHM_RLE = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getColorFormat = JavaMethod("()I")
    getHorizontalZonesCount = JavaMethod("()I")
    getVerticalZonesCount = JavaMethod("()I")
    getCompressionAlgorithm = JavaMethod("()I")
    getZoneColors = JavaMethod("()[I")
    toString = JavaMethod("()Ljava/lang/String;")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSource = JavaMethod("()I")