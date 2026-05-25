from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PageMatchBounds"]

class PageMatchBounds(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/models/PageMatchBounds"
    __javaconstructor__ = [("(Ljava/util/List;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getBounds = JavaMethod("()Ljava/util/List;")
    getTextStartIndex = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")