from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbsSavedState"]

class AbsSavedState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/AbsSavedState"
    __javaconstructor__ = [("(Landroid/os/Parcelable;)V", False), ("(Landroid/os/Parcel;)V", False), ("(Landroid/os/Parcel;Ljava/lang/ClassLoader;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EMPTY_STATE = JavaStaticField("Landroid/view/AbsSavedState;")
    getSuperState = JavaMethod("()Landroid/os/Parcelable;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")