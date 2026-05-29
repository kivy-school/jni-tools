from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputManager"]

class InputManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/input/InputManager"
    ACTION_QUERY_KEYBOARD_LAYOUTS = JavaStaticField("Ljava/lang/String;")
    META_DATA_KEYBOARD_LAYOUTS = JavaStaticField("Ljava/lang/String;")
    getInputDeviceIds = JavaMethod("()[I")
    verifyInputEvent = JavaMethod("(Landroid/view/InputEvent;)Landroid/view/VerifiedInputEvent;")
    getInputDevice = JavaMethod("(I)Landroid/view/InputDevice;")
    getHostUsiVersion = JavaMethod("(Landroid/view/Display;)Landroid/hardware/input/HostUsiVersion;")
    getInputDeviceViewBehavior = JavaMethod("(I)Landroid/view/InputDevice$ViewBehavior;")
    getMaximumObscuringOpacityForTouch = JavaMethod("()F")
    isStylusPointerIconEnabled = JavaMethod("()Z")
    registerInputDeviceListener = JavaMethod("(Landroid/hardware/input/InputManager$InputDeviceListener;Landroid/os/Handler;)V")
    unregisterInputDeviceListener = JavaMethod("(Landroid/hardware/input/InputManager$InputDeviceListener;)V")

    class InputDeviceListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/input/InputManager$InputDeviceListener"
        onInputDeviceChanged = JavaMethod("(I)V")
        onInputDeviceRemoved = JavaMethod("(I)V")
        onInputDeviceAdded = JavaMethod("(I)V")