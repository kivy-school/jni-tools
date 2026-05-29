from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PageSelection"]

class PageSelection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/models/selection/PageSelection"
    __javaconstructor__ = [("(ILandroid/graphics/pdf/models/selection/SelectionBoundary;Landroid/graphics/pdf/models/selection/SelectionBoundary;Ljava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getPage = JavaMethod("()I")
    getStart = JavaMethod("()Landroid/graphics/pdf/models/selection/SelectionBoundary;")
    getStop = JavaMethod("()Landroid/graphics/pdf/models/selection/SelectionBoundary;")
    getSelectedTextContents = JavaMethod("()Ljava/util/List;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")