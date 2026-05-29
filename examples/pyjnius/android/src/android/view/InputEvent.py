from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputEvent"]

class InputEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/InputEvent"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getDeviceId = JavaMethod("()I")
    getDevice = JavaMethod("()Landroid/view/InputDevice;")
    getSource = JavaMethod("()I")
    isFromSource = JavaMethod("(I)Z")
    getEventTime = JavaMethod("()J")
    describeContents = JavaMethod("()I")