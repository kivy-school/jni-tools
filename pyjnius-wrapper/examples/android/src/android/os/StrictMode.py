from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StrictMode"]

class StrictMode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/StrictMode"
    setThreadPolicy = JavaStaticMethod("(Landroid/os/StrictMode$ThreadPolicy;)V")
    getThreadPolicy = JavaStaticMethod("()Landroid/os/StrictMode$ThreadPolicy;")
    allowThreadDiskWrites = JavaStaticMethod("()Landroid/os/StrictMode$ThreadPolicy;")
    allowThreadDiskReads = JavaStaticMethod("()Landroid/os/StrictMode$ThreadPolicy;")
    setVmPolicy = JavaStaticMethod("(Landroid/os/StrictMode$VmPolicy;)V")
    getVmPolicy = JavaStaticMethod("()Landroid/os/StrictMode$VmPolicy;")
    enableDefaults = JavaStaticMethod("()V")
    noteSlowCall = JavaStaticMethod("(Ljava/lang/String;)V")

    class OnThreadViolationListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/StrictMode/OnThreadViolationListener"
        onThreadViolation = JavaMethod("(Landroid/os/strictmode/Violation;)V")

    class OnVmViolationListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/StrictMode/OnVmViolationListener"
        onVmViolation = JavaMethod("(Landroid/os/strictmode/Violation;)V")

    class ThreadPolicy(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/StrictMode/ThreadPolicy"
        LAX = JavaStaticField("Landroid/os/StrictMode$ThreadPolicy;")
        toString = JavaMethod("()Ljava/lang/String;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/os/StrictMode/ThreadPolicy/Builder"
            __javaconstructor__ = [("()V", False), ("(Landroid/os/StrictMode$ThreadPolicy;)V", False)]
            detectAll = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            permitAll = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            detectNetwork = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            permitNetwork = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            detectDiskReads = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            permitDiskReads = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            detectCustomSlowCalls = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            permitCustomSlowCalls = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            permitResourceMismatches = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            detectUnbufferedIo = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            permitUnbufferedIo = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            detectResourceMismatches = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            detectDiskWrites = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            permitDiskWrites = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            detectExplicitGc = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            permitExplicitGc = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            penaltyDialog = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            penaltyDeath = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            penaltyDeathOnNetwork = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            penaltyFlashScreen = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            penaltyLog = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            penaltyDropBox = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy$Builder;")
            penaltyListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/StrictMode$OnThreadViolationListener;)Landroid/os/StrictMode$ThreadPolicy$Builder;")
            build = JavaMethod("()Landroid/os/StrictMode$ThreadPolicy;")

    class VmPolicy(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/StrictMode/VmPolicy"
        LAX = JavaStaticField("Landroid/os/StrictMode$VmPolicy;")
        toString = JavaMethod("()Ljava/lang/String;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/os/StrictMode/VmPolicy/Builder"
            __javaconstructor__ = [("()V", False), ("(Landroid/os/StrictMode$VmPolicy;)V", False)]
            setClassInstanceLimit = JavaMethod("(Ljava/lang/Class;I)Landroid/os/StrictMode$VmPolicy$Builder;")
            detectActivityLeaks = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            detectNonSdkApiUsage = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            permitNonSdkApiUsage = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            detectAll = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            detectLeakedSqlLiteObjects = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            detectLeakedClosableObjects = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            detectLeakedRegistrationObjects = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            detectFileUriExposure = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            detectCleartextNetwork = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            detectContentUriWithoutPermission = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            detectUntaggedSockets = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            detectImplicitDirectBoot = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            detectCredentialProtectedWhileLocked = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            detectIncorrectContextUse = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            detectUnsafeIntentLaunch = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            permitUnsafeIntentLaunch = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            penaltyDeath = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            penaltyDeathOnCleartextNetwork = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            penaltyDeathOnFileUriExposure = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            penaltyLog = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            penaltyDropBox = JavaMethod("()Landroid/os/StrictMode$VmPolicy$Builder;")
            penaltyListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/StrictMode$OnVmViolationListener;)Landroid/os/StrictMode$VmPolicy$Builder;")
            build = JavaMethod("()Landroid/os/StrictMode$VmPolicy;")