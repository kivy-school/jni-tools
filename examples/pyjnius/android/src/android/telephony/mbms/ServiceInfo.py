from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServiceInfo"]

class ServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/ServiceInfo"
    getServiceId = JavaMethod("()Ljava/lang/String;")
    getSessionEndTime = JavaMethod("()Ljava/util/Date;")
    getServiceClassName = JavaMethod("()Ljava/lang/String;")
    getSessionStartTime = JavaMethod("()Ljava/util/Date;")
    getNamedContentLocales = JavaMethod("()Ljava/util/Set;")
    getNameForLocale = JavaMethod("(Ljava/util/Locale;)Ljava/lang/CharSequence;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getLocales = JavaMethod("()Ljava/util/List;")