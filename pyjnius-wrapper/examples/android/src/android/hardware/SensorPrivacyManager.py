from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SensorPrivacyManager"]

class SensorPrivacyManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/SensorPrivacyManager"
    TOGGLE_TYPE_HARDWARE = JavaStaticField("I")
    TOGGLE_TYPE_SOFTWARE = JavaStaticField("I")
    supportsSensorToggle = JavaMultipleMethod([("(I)Z", False, False), ("(II)Z", False, False)])

    class Sensors(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/SensorPrivacyManager/Sensors"
        CAMERA = JavaStaticField("I")
        MICROPHONE = JavaStaticField("I")