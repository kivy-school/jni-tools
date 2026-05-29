from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PageMatchBounds"]

class PageMatchBounds(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/models/PageMatchBounds"
    __javaconstructor__ = [("(Ljava/util/List;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getTextStartIndex = JavaMethod("()I")
    getBounds = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")