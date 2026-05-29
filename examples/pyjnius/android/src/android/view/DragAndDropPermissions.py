from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DragAndDropPermissions"]

class DragAndDropPermissions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/DragAndDropPermissions"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    release = JavaMethod("()V")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")