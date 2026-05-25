from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServiceInfo"]

class ServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/ServiceInfo"
    getNameForLocale = JavaMethod("(Ljava/util/Locale;)Ljava/lang/CharSequence;")
    getNamedContentLocales = JavaMethod("()Ljava/util/Set;")
    getServiceClassName = JavaMethod("()Ljava/lang/String;")
    getLocales = JavaMethod("()Ljava/util/List;")
    getServiceId = JavaMethod("()Ljava/lang/String;")
    getSessionStartTime = JavaMethod("()Ljava/util/Date;")
    getSessionEndTime = JavaMethod("()Ljava/util/Date;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")