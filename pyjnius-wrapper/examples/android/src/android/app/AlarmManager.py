from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlarmManager"]

class AlarmManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/AlarmManager"
    ACTION_NEXT_ALARM_CLOCK_CHANGED = JavaStaticField("Ljava/lang/String;")
    ACTION_SCHEDULE_EXACT_ALARM_PERMISSION_STATE_CHANGED = JavaStaticField("Ljava/lang/String;")
    ELAPSED_REALTIME = JavaStaticField("I")
    ELAPSED_REALTIME_WAKEUP = JavaStaticField("I")
    INTERVAL_DAY = JavaStaticField("J")
    INTERVAL_FIFTEEN_MINUTES = JavaStaticField("J")
    INTERVAL_HALF_DAY = JavaStaticField("J")
    INTERVAL_HALF_HOUR = JavaStaticField("J")
    INTERVAL_HOUR = JavaStaticField("J")
    RTC = JavaStaticField("I")
    RTC_WAKEUP = JavaStaticField("I")
    set = JavaMultipleMethod([("(IJLandroid/app/PendingIntent;)V", False, False), ("(IJLjava/lang/String;Landroid/app/AlarmManager$OnAlarmListener;Landroid/os/Handler;)V", False, False)])
    setRepeating = JavaMethod("(IJJLandroid/app/PendingIntent;)V")
    setWindow = JavaMultipleMethod([("(IJJLandroid/app/PendingIntent;)V", False, False), ("(IJJLjava/lang/String;Landroid/app/AlarmManager$OnAlarmListener;Landroid/os/Handler;)V", False, False), ("(IJJLjava/lang/String;Ljava/util/concurrent/Executor;Landroid/app/AlarmManager$OnAlarmListener;)V", False, False)])
    setExact = JavaMultipleMethod([("(IJLandroid/app/PendingIntent;)V", False, False), ("(IJLjava/lang/String;Landroid/app/AlarmManager$OnAlarmListener;Landroid/os/Handler;)V", False, False)])
    setAlarmClock = JavaMethod("(Landroid/app/AlarmManager$AlarmClockInfo;Landroid/app/PendingIntent;)V")
    setInexactRepeating = JavaMethod("(IJJLandroid/app/PendingIntent;)V")
    setAndAllowWhileIdle = JavaMethod("(IJLandroid/app/PendingIntent;)V")
    setExactAndAllowWhileIdle = JavaMethod("(IJLandroid/app/PendingIntent;)V")
    cancel = JavaMultipleMethod([("(Landroid/app/PendingIntent;)V", False, False), ("(Landroid/app/AlarmManager$OnAlarmListener;)V", False, False)])
    cancelAll = JavaMethod("()V")
    setTime = JavaMethod("(J)V")
    setTimeZone = JavaMethod("(Ljava/lang/String;)V")
    canScheduleExactAlarms = JavaMethod("()Z")
    getNextAlarmClock = JavaMethod("()Landroid/app/AlarmManager$AlarmClockInfo;")

    class AlarmClockInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/AlarmManager/AlarmClockInfo"
        __javaconstructor__ = [("(JLandroid/app/PendingIntent;)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        getTriggerTime = JavaMethod("()J")
        getShowIntent = JavaMethod("()Landroid/app/PendingIntent;")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class OnAlarmListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/AlarmManager/OnAlarmListener"
        onAlarm = JavaMethod("()V")