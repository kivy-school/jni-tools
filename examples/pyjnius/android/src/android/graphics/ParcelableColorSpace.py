from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParcelableColorSpace"]

class ParcelableColorSpace(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/ParcelableColorSpace"
    __javaconstructor__ = [("(Landroid/graphics/ColorSpace;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    isParcelable = JavaStaticMethod("(Landroid/graphics/ColorSpace;)Z")
    getColorSpace = JavaMethod("()Landroid/graphics/ColorSpace;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")