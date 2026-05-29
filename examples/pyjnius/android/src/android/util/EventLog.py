from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EventLog"]

class EventLog(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/EventLog"
    writeEvent = JavaMultipleMethod([("(IJ)I", True, False), ("(II)I", True, False), ("(I[Ljava/lang/Object;)I", True, True), ("(ILjava/lang/String;)I", True, False), ("(IF)I", True, False)])
    readEvents = JavaStaticMethod("([ILjava/util/Collection;)V")
    getTagCode = JavaStaticMethod("(Ljava/lang/String;)I")
    getTagName = JavaStaticMethod("(I)Ljava/lang/String;")

    class Event(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/util/EventLog$Event"
        getTimeNanos = JavaMethod("()J")
        getProcessId = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getTag = JavaMethod("()I")
        getData = JavaMethod("()Ljava/lang/Object;")
        getThreadId = JavaMethod("()I")