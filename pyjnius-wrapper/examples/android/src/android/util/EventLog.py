from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EventLog"]

class EventLog(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/EventLog"
    writeEvent = JavaMultipleMethod([("(II)I", True, False), ("(IJ)I", True, False), ("(IF)I", True, False), ("(ILjava/lang/String;)I", True, False), ("(I[Ljava/lang/Object;)I", True, True)])
    readEvents = JavaStaticMethod("([ILjava/util/Collection;)V")
    getTagName = JavaStaticMethod("(I)Ljava/lang/String;")
    getTagCode = JavaStaticMethod("(Ljava/lang/String;)I")

    class Event(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/util/EventLog/Event"
        getProcessId = JavaMethod("()I")
        getThreadId = JavaMethod("()I")
        getTimeNanos = JavaMethod("()J")
        getTag = JavaMethod("()I")
        getData = JavaMethod("()Ljava/lang/Object;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")