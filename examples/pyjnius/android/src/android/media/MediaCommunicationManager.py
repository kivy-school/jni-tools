from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaCommunicationManager"]

class MediaCommunicationManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaCommunicationManager"
    getSession2Tokens = JavaMethod("()Ljava/util/List;")
    getVersion = JavaMethod("()I")