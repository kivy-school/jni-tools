from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputManager"]

class InputManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/input/InputManager"
    ACTION_QUERY_KEYBOARD_LAYOUTS = JavaStaticField("Ljava/lang/String;")
    META_DATA_KEYBOARD_LAYOUTS = JavaStaticField("Ljava/lang/String;")
    getInputDevice = JavaMethod("(I)Landroid/view/InputDevice;")
    getInputDeviceViewBehavior = JavaMethod("(I)Landroid/view/InputDevice$ViewBehavior;")
    getInputDeviceIds = JavaMethod("()[I")
    registerInputDeviceListener = JavaMethod("(Landroid/hardware/input/InputManager$InputDeviceListener;Landroid/os/Handler;)V")
    unregisterInputDeviceListener = JavaMethod("(Landroid/hardware/input/InputManager$InputDeviceListener;)V")
    getMaximumObscuringOpacityForTouch = JavaMethod("()F")
    verifyInputEvent = JavaMethod("(Landroid/view/InputEvent;)Landroid/view/VerifiedInputEvent;")
    isStylusPointerIconEnabled = JavaMethod("()Z")
    getHostUsiVersion = JavaMethod("(Landroid/view/Display;)Landroid/hardware/input/HostUsiVersion;")

    class InputDeviceListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/input/InputManager/InputDeviceListener"
        onInputDeviceAdded = JavaMethod("(I)V")
        onInputDeviceRemoved = JavaMethod("(I)V")
        onInputDeviceChanged = JavaMethod("(I)V")