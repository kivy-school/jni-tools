from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputEvent"]

class InputEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/InputEvent"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDeviceId = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    getEventTime = JavaMethod("()J")
    getSource = JavaMethod("()I")
    getDevice = JavaMethod("()Landroid/view/InputDevice;")
    isFromSource = JavaMethod("(I)Z")