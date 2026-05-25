from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StatsLog"]

class StatsLog(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/StatsLog"
    logStart = JavaStaticMethod("(I)Z")
    logStop = JavaStaticMethod("(I)Z")
    logEvent = JavaStaticMethod("(I)Z")
    logBinaryPushStateChanged = JavaStaticMethod("(Ljava/lang/String;JII[J)Z")