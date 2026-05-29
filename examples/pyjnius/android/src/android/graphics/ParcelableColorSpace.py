from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParcelableColorSpace"]

class ParcelableColorSpace(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/ParcelableColorSpace"
    __javaconstructor__ = [("(Landroid/graphics/ColorSpace;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    isParcelable = JavaStaticMethod("(Landroid/graphics/ColorSpace;)Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getColorSpace = JavaMethod("()Landroid/graphics/ColorSpace;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")