from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Topic"]

class Topic(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/topics/Topic"
    __javaconstructor__ = [("(JJI)V", False)]
    getModelVersion = JavaMethod("()J")
    getTaxonomyVersion = JavaMethod("()J")
    getTopicId = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")