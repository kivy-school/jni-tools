from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccessibilityGestureEvent"]

class AccessibilityGestureEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accessibilityservice/AccessibilityGestureEvent"
    __javaconstructor__ = [("(IILjava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getMotionEvents = JavaMethod("()Ljava/util/List;")
    gestureIdToString = JavaStaticMethod("(I)Ljava/lang/String;")
    getGestureId = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getDisplayId = JavaMethod("()I")