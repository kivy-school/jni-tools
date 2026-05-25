from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VerifiedDisplayHash"]

class VerifiedDisplayHash(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/displayhash/VerifiedDisplayHash"
    __javaconstructor__ = [("(JLandroid/graphics/Rect;Ljava/lang/String;[B)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getTimeMillis = JavaMethod("()J")
    getBoundsInWindow = JavaMethod("()Landroid/graphics/Rect;")
    getHashAlgorithm = JavaMethod("()Ljava/lang/String;")
    getImageHash = JavaMethod("()[B")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")