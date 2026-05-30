from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class SelectionBoundary(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/models/selection/SelectionBoundary"
    __javaconstructor__ = [("(Landroid/graphics/Point;)V", False), ("(I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPoint = JavaMethod("()Landroid/graphics/Point;")
    getIsRtl = JavaMethod("()Z")
    getIndex = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class PageSelection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/models/selection/PageSelection"
    __javaconstructor__ = [("(ILandroid/graphics/pdf/models/selection/SelectionBoundary;Landroid/graphics/pdf/models/selection/SelectionBoundary;Ljava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSelectedTextContents = JavaMethod("()Ljava/util/List;")
    getPage = JavaMethod("()I")
    getStop = JavaMethod("()Landroid/graphics/pdf/models/selection/SelectionBoundary;")
    getStart = JavaMethod("()Landroid/graphics/pdf/models/selection/SelectionBoundary;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")