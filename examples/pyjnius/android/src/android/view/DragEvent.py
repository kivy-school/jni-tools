from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DragEvent"]

class DragEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/DragEvent"
    ACTION_DRAG_ENDED = JavaStaticField("I")
    ACTION_DRAG_ENTERED = JavaStaticField("I")
    ACTION_DRAG_EXITED = JavaStaticField("I")
    ACTION_DRAG_LOCATION = JavaStaticField("I")
    ACTION_DRAG_STARTED = JavaStaticField("I")
    ACTION_DROP = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getX = JavaMethod("()F")
    getY = JavaMethod("()F")
    getClipData = JavaMethod("()Landroid/content/ClipData;")
    getAction = JavaMethod("()I")
    getLocalState = JavaMethod("()Ljava/lang/Object;")
    getResult = JavaMethod("()Z")
    getClipDescription = JavaMethod("()Landroid/content/ClipDescription;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")