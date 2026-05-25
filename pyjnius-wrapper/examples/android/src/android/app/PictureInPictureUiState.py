from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PictureInPictureUiState"]

class PictureInPictureUiState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/PictureInPictureUiState"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    isStashed = JavaMethod("()Z")
    isTransitioningToPip = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")