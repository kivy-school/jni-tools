from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EventLogTags"]

class EventLogTags(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/EventLogTags"
    __javaconstructor__ = [("()V", False), ("(Ljava/io/BufferedReader;)V", False)]
    get = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/util/EventLogTags$Description;", False, False), ("(I)Landroid/util/EventLogTags$Description;", False, False)])

    class Description(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/util/EventLogTags/Description"
        mName = JavaField("Ljava/lang/String;")
        mTag = JavaField("I")