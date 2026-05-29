from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlarmClock"]

class AlarmClock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/provider/AlarmClock"
    __javaconstructor__ = [("()V", False)]
    ACTION_DISMISS_ALARM = JavaStaticField("Ljava/lang/String;")
    ACTION_DISMISS_TIMER = JavaStaticField("Ljava/lang/String;")
    ACTION_SET_ALARM = JavaStaticField("Ljava/lang/String;")
    ACTION_SET_TIMER = JavaStaticField("Ljava/lang/String;")
    ACTION_SHOW_ALARMS = JavaStaticField("Ljava/lang/String;")
    ACTION_SHOW_TIMERS = JavaStaticField("Ljava/lang/String;")
    ACTION_SNOOZE_ALARM = JavaStaticField("Ljava/lang/String;")
    ALARM_SEARCH_MODE_ALL = JavaStaticField("Ljava/lang/String;")
    ALARM_SEARCH_MODE_LABEL = JavaStaticField("Ljava/lang/String;")
    ALARM_SEARCH_MODE_NEXT = JavaStaticField("Ljava/lang/String;")
    ALARM_SEARCH_MODE_TIME = JavaStaticField("Ljava/lang/String;")
    EXTRA_ALARM_SEARCH_MODE = JavaStaticField("Ljava/lang/String;")
    EXTRA_ALARM_SNOOZE_DURATION = JavaStaticField("Ljava/lang/String;")
    EXTRA_DAYS = JavaStaticField("Ljava/lang/String;")
    EXTRA_HOUR = JavaStaticField("Ljava/lang/String;")
    EXTRA_IS_PM = JavaStaticField("Ljava/lang/String;")
    EXTRA_LENGTH = JavaStaticField("Ljava/lang/String;")
    EXTRA_MESSAGE = JavaStaticField("Ljava/lang/String;")
    EXTRA_MINUTES = JavaStaticField("Ljava/lang/String;")
    EXTRA_RINGTONE = JavaStaticField("Ljava/lang/String;")
    EXTRA_SKIP_UI = JavaStaticField("Ljava/lang/String;")
    EXTRA_VIBRATE = JavaStaticField("Ljava/lang/String;")
    VALUE_RINGTONE_SILENT = JavaStaticField("Ljava/lang/String;")