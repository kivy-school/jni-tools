from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbsSavedState"]

class AbsSavedState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/AbsSavedState"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EMPTY_STATE = JavaStaticField("Landroid/view/AbsSavedState;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSuperState = JavaMethod("()Landroid/os/Parcelable;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")