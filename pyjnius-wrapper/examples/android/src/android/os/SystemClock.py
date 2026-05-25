from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SystemClock"]

class SystemClock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/SystemClock"
    sleep = JavaStaticMethod("(J)V")
    setCurrentTimeMillis = JavaStaticMethod("(J)Z")
    uptimeMillis = JavaStaticMethod("()J")
    uptimeNanos = JavaStaticMethod("()J")
    elapsedRealtime = JavaStaticMethod("()J")
    elapsedRealtimeNanos = JavaStaticMethod("()J")
    currentThreadTimeMillis = JavaStaticMethod("()J")
    currentNetworkTimeClock = JavaStaticMethod("()Ljava/time/Clock;")
    currentGnssTimeClock = JavaStaticMethod("()Ljava/time/Clock;")