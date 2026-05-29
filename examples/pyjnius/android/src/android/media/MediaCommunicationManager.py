from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaCommunicationManager"]

class MediaCommunicationManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaCommunicationManager"
    getVersion = JavaMethod("()I")
    getSession2Tokens = JavaMethod("()Ljava/util/List;")