from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VerifiedDisplayHash"]

class VerifiedDisplayHash(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/displayhash/VerifiedDisplayHash"
    __javaconstructor__ = [("(JLandroid/graphics/Rect;Ljava/lang/String;[B)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getHashAlgorithm = JavaMethod("()Ljava/lang/String;")
    getImageHash = JavaMethod("()[B")
    getTimeMillis = JavaMethod("()J")
    toString = JavaMethod("()Ljava/lang/String;")
    getBoundsInWindow = JavaMethod("()Landroid/graphics/Rect;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")