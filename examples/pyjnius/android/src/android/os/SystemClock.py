from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SystemClock"]

class SystemClock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/SystemClock"
    sleep = JavaStaticMethod("(J)V")
    uptimeMillis = JavaStaticMethod("()J")
    uptimeNanos = JavaStaticMethod("()J")
    elapsedRealtime = JavaStaticMethod("()J")
    currentGnssTimeClock = JavaStaticMethod("()Ljava/time/Clock;")
    currentNetworkTimeClock = JavaStaticMethod("()Ljava/time/Clock;")
    currentThreadTimeMillis = JavaStaticMethod("()J")
    elapsedRealtimeNanos = JavaStaticMethod("()J")
    setCurrentTimeMillis = JavaStaticMethod("(J)Z")