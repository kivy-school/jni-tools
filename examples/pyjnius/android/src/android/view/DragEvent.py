from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    getAction = JavaMethod("()I")
    getX = JavaMethod("()F")
    getY = JavaMethod("()F")
    getClipData = JavaMethod("()Landroid/content/ClipData;")
    getClipDescription = JavaMethod("()Landroid/content/ClipDescription;")
    getLocalState = JavaMethod("()Ljava/lang/Object;")
    getResult = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")