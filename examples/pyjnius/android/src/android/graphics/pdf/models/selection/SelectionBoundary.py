from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SelectionBoundary"]

class SelectionBoundary(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/models/selection/SelectionBoundary"
    __javaconstructor__ = [("(Landroid/graphics/Point;)V", False), ("(I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPoint = JavaMethod("()Landroid/graphics/Point;")
    getIsRtl = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getIndex = JavaMethod("()I")