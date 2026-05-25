from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrmStore"]

class DrmStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmStore"
    __javaconstructor__ = [("()V", False)]

    class Action(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmStore/Action"
        __javaconstructor__ = [("()V", False)]
        DEFAULT = JavaStaticField("I")
        DISPLAY = JavaStaticField("I")
        EXECUTE = JavaStaticField("I")
        OUTPUT = JavaStaticField("I")
        PLAY = JavaStaticField("I")
        PREVIEW = JavaStaticField("I")
        RINGTONE = JavaStaticField("I")
        TRANSFER = JavaStaticField("I")

    class ConstraintsColumns(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmStore/ConstraintsColumns"
        EXTENDED_METADATA = JavaStaticField("Ljava/lang/String;")
        LICENSE_AVAILABLE_TIME = JavaStaticField("Ljava/lang/String;")
        LICENSE_EXPIRY_TIME = JavaStaticField("Ljava/lang/String;")
        LICENSE_START_TIME = JavaStaticField("Ljava/lang/String;")
        MAX_REPEAT_COUNT = JavaStaticField("Ljava/lang/String;")
        REMAINING_REPEAT_COUNT = JavaStaticField("Ljava/lang/String;")

    class DrmObjectType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmStore/DrmObjectType"
        __javaconstructor__ = [("()V", False)]
        CONTENT = JavaStaticField("I")
        RIGHTS_OBJECT = JavaStaticField("I")
        TRIGGER_OBJECT = JavaStaticField("I")
        UNKNOWN = JavaStaticField("I")

    class Playback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmStore/Playback"
        __javaconstructor__ = [("()V", False)]
        PAUSE = JavaStaticField("I")
        RESUME = JavaStaticField("I")
        START = JavaStaticField("I")
        STOP = JavaStaticField("I")

    class RightsStatus(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmStore/RightsStatus"
        __javaconstructor__ = [("()V", False)]
        RIGHTS_EXPIRED = JavaStaticField("I")
        RIGHTS_INVALID = JavaStaticField("I")
        RIGHTS_NOT_ACQUIRED = JavaStaticField("I")
        RIGHTS_VALID = JavaStaticField("I")