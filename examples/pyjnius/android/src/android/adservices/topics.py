from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class TopicsManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/topics/TopicsManager"
    getTopics = JavaMethod("(Landroid/adservices/topics/GetTopicsRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    get = JavaStaticMethod("(Landroid/content/Context;)Landroid/adservices/topics/TopicsManager;")

class GetTopicsResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/topics/GetTopicsResponse"
    getEncryptedTopics = JavaMethod("()Ljava/util/List;")
    getTopics = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/topics/GetTopicsResponse$Builder"
        __javaconstructor__ = [("(Ljava/util/List;)V", False), ("(Ljava/util/List;Ljava/util/List;)V", False)]
        build = JavaMethod("()Landroid/adservices/topics/GetTopicsResponse;")

class EncryptedTopic(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/topics/EncryptedTopic"
    __javaconstructor__ = [("([BLjava/lang/String;[B)V", False)]
    getEncapsulatedKey = JavaMethod("()[B")
    getEncryptedTopic = JavaMethod("()[B")
    getKeyIdentifier = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")

class Topic(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/topics/Topic"
    __javaconstructor__ = [("(JJI)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getModelVersion = JavaMethod("()J")
    getTaxonomyVersion = JavaMethod("()J")
    getTopicId = JavaMethod("()I")

class GetTopicsRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/topics/GetTopicsRequest"
    getAdsSdkName = JavaMethod("()Ljava/lang/String;")
    shouldRecordObservation = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/topics/GetTopicsRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setAdsSdkName = JavaMethod("(Ljava/lang/String;)Landroid/adservices/topics/GetTopicsRequest$Builder;")
        setShouldRecordObservation = JavaMethod("(Z)Landroid/adservices/topics/GetTopicsRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/topics/GetTopicsRequest;")