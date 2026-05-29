from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ApplicationErrorReport"]

class ApplicationErrorReport(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/ApplicationErrorReport"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TYPE_ANR = JavaStaticField("I")
    TYPE_BATTERY = JavaStaticField("I")
    TYPE_CRASH = JavaStaticField("I")
    TYPE_NONE = JavaStaticField("I")
    TYPE_RUNNING_SERVICE = JavaStaticField("I")
    anrInfo = JavaField("Landroid/app/ApplicationErrorReport$AnrInfo;")
    batteryInfo = JavaField("Landroid/app/ApplicationErrorReport$BatteryInfo;")
    crashInfo = JavaField("Landroid/app/ApplicationErrorReport$CrashInfo;")
    installerPackageName = JavaField("Ljava/lang/String;")
    packageName = JavaField("Ljava/lang/String;")
    processName = JavaField("Ljava/lang/String;")
    runningServiceInfo = JavaField("Landroid/app/ApplicationErrorReport$RunningServiceInfo;")
    systemApp = JavaField("Z")
    time = JavaField("J")
    type = JavaField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getErrorReportReceiver = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;I)Landroid/content/ComponentName;")
    dump = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    readFromParcel = JavaMethod("(Landroid/os/Parcel;)V")
    describeContents = JavaMethod("()I")

    class RunningServiceInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/ApplicationErrorReport$RunningServiceInfo"
        __javaconstructor__ = [("()V", False), ("(Landroid/os/Parcel;)V", False)]
        durationMillis = JavaField("J")
        serviceDetails = JavaField("Ljava/lang/String;")
        dump = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class CrashInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/ApplicationErrorReport$CrashInfo"
        __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Landroid/os/Parcel;)V", False), ("()V", False)]
        exceptionClassName = JavaField("Ljava/lang/String;")
        exceptionMessage = JavaField("Ljava/lang/String;")
        stackTrace = JavaField("Ljava/lang/String;")
        throwClassName = JavaField("Ljava/lang/String;")
        throwFileName = JavaField("Ljava/lang/String;")
        throwLineNumber = JavaField("I")
        throwMethodName = JavaField("Ljava/lang/String;")
        dump = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class BatteryInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/ApplicationErrorReport$BatteryInfo"
        __javaconstructor__ = [("()V", False), ("(Landroid/os/Parcel;)V", False)]
        checkinDetails = JavaField("Ljava/lang/String;")
        durationMicros = JavaField("J")
        usageDetails = JavaField("Ljava/lang/String;")
        usagePercent = JavaField("I")
        dump = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class AnrInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/ApplicationErrorReport$AnrInfo"
        __javaconstructor__ = [("()V", False), ("(Landroid/os/Parcel;)V", False)]
        activity = JavaField("Ljava/lang/String;")
        cause = JavaField("Ljava/lang/String;")
        info = JavaField("Ljava/lang/String;")
        dump = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")