from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SelectionBoundary"]

class SelectionBoundary(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/models/selection/SelectionBoundary"
    __javaconstructor__ = [("(I)V", False), ("(Landroid/graphics/Point;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getIndex = JavaMethod("()I")
    getPoint = JavaMethod("()Landroid/graphics/Point;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getIsRtl = JavaMethod("()Z")