from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccessibilityGestureEvent"]

class AccessibilityGestureEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accessibilityservice/AccessibilityGestureEvent"
    __javaconstructor__ = [("(IILjava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getDisplayId = JavaMethod("()I")
    getGestureId = JavaMethod("()I")
    getMotionEvents = JavaMethod("()Ljava/util/List;")
    toString = JavaMethod("()Ljava/lang/String;")
    gestureIdToString = JavaStaticMethod("(I)Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")