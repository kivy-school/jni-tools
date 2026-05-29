from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HapticFeedbackConstants"]

class HapticFeedbackConstants(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/HapticFeedbackConstants"
    CLOCK_TICK = JavaStaticField("I")
    CONFIRM = JavaStaticField("I")
    CONTEXT_CLICK = JavaStaticField("I")
    DRAG_START = JavaStaticField("I")
    FLAG_IGNORE_GLOBAL_SETTING = JavaStaticField("I")
    FLAG_IGNORE_VIEW_SETTING = JavaStaticField("I")
    GESTURE_END = JavaStaticField("I")
    GESTURE_START = JavaStaticField("I")
    GESTURE_THRESHOLD_ACTIVATE = JavaStaticField("I")
    GESTURE_THRESHOLD_DEACTIVATE = JavaStaticField("I")
    KEYBOARD_PRESS = JavaStaticField("I")
    KEYBOARD_RELEASE = JavaStaticField("I")
    KEYBOARD_TAP = JavaStaticField("I")
    LONG_PRESS = JavaStaticField("I")
    NO_HAPTICS = JavaStaticField("I")
    REJECT = JavaStaticField("I")
    SEGMENT_FREQUENT_TICK = JavaStaticField("I")
    SEGMENT_TICK = JavaStaticField("I")
    TEXT_HANDLE_MOVE = JavaStaticField("I")
    TOGGLE_OFF = JavaStaticField("I")
    TOGGLE_ON = JavaStaticField("I")
    VIRTUAL_KEY = JavaStaticField("I")
    VIRTUAL_KEY_RELEASE = JavaStaticField("I")