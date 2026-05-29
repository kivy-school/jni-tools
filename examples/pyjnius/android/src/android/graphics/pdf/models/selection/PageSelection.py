from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PageSelection"]

class PageSelection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/models/selection/PageSelection"
    __javaconstructor__ = [("(ILandroid/graphics/pdf/models/selection/SelectionBoundary;Landroid/graphics/pdf/models/selection/SelectionBoundary;Ljava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getStart = JavaMethod("()Landroid/graphics/pdf/models/selection/SelectionBoundary;")
    getStop = JavaMethod("()Landroid/graphics/pdf/models/selection/SelectionBoundary;")
    getPage = JavaMethod("()I")
    getSelectedTextContents = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")