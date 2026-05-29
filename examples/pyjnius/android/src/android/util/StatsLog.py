from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StatsLog"]

class StatsLog(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/StatsLog"
    logEvent = JavaStaticMethod("(I)Z")
    logStart = JavaStaticMethod("(I)Z")
    logBinaryPushStateChanged = JavaStaticMethod("(Ljava/lang/String;JII[J)Z")
    logStop = JavaStaticMethod("(I)Z")