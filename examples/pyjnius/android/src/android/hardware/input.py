from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class InputManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/input/InputManager"
    ACTION_QUERY_KEYBOARD_LAYOUTS = JavaStaticField("Ljava/lang/String;")
    META_DATA_KEYBOARD_LAYOUTS = JavaStaticField("Ljava/lang/String;")
    getHostUsiVersion = JavaMethod("(Landroid/view/Display;)Landroid/hardware/input/HostUsiVersion;")
    getInputDevice = JavaMethod("(I)Landroid/view/InputDevice;")
    getInputDeviceIds = JavaMethod("()[I")
    getInputDeviceViewBehavior = JavaMethod("(I)Landroid/view/InputDevice$ViewBehavior;")
    getMaximumObscuringOpacityForTouch = JavaMethod("()F")
    isStylusPointerIconEnabled = JavaMethod("()Z")
    registerInputDeviceListener = JavaMethod("(Landroid/hardware/input/InputManager$InputDeviceListener;Landroid/os/Handler;)V")
    unregisterInputDeviceListener = JavaMethod("(Landroid/hardware/input/InputManager$InputDeviceListener;)V")
    verifyInputEvent = JavaMethod("(Landroid/view/InputEvent;)Landroid/view/VerifiedInputEvent;")

    class InputDeviceListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/input/InputManager$InputDeviceListener"
        onInputDeviceAdded = JavaMethod("(I)V")
        onInputDeviceChanged = JavaMethod("(I)V")
        onInputDeviceRemoved = JavaMethod("(I)V")

class HostUsiVersion(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/input/HostUsiVersion"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getMinorVersion = JavaMethod("()I")
    getMajorVersion = JavaMethod("()I")