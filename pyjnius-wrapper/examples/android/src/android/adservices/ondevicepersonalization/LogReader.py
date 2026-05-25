from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LogReader"]

class LogReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/LogReader"
    getRequests = JavaMethod("(Ljava/time/Instant;Ljava/time/Instant;)Ljava/util/List;")
    getJoinedEvents = JavaMethod("(Ljava/time/Instant;Ljava/time/Instant;)Ljava/util/List;")